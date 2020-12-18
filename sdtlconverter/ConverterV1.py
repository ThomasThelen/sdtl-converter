from typing import Union, List
import rdflib
import json

from sdtlconverter.Converter import Converter

class DataFrame:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


class ConverterV1(Converter):
    """
    A converter that takes SDTL 1.0 and produces a ProvONE representation.
    """

    def __init__(self, file_paths: Union[List, str]):
        """
        Creates a converter instance. It can take any number of SDTL file paths as a list,
        or a single file path as a string.

        :param file_paths: A path to an SDTL JSON file
        """

        self.dataframes= {}
        self.variable_names = {}

        # A list of the sub-properties of the top level provone:Programs (ie scripts, things that have
        # extensions like .py, .R, etc) that
        # we want to include in the RDF
        self.desired_script_properties = ["id",
                                          "sourceFileName", "fileName", "sourceLanguage",
                                          "ScriptMD5", "ScriptSHA1", "SourceFileLastUpdate",
                                          "SourceFileSize", "LineCount", "CommandCount",
                                          "Parser", "ModelCreatedTime"
                                          ]

        super().__init__(file_paths)

    def sdtl_to_rdf(self, sdtl, parent_id: rdflib.URIRef):
        """
        Turns a block of SDTL into RDF, recursively.

        :param sdtl: The SDTL being turned into RDF
        :param parent_id: The identifier of the parent object that this object/property belongs to
        :return:
        """

        # Identifiers of child objects that the parent links to.
        object_identifiers = []
        if isinstance(sdtl, List):

            for sdtl_object in sdtl:
                # Create a new object
                object_identifier = self.id_manager.get_id(sdtl_object['$type'])
                prop_type = self.id_manager.get_property_id(sdtl_object['$type'])

                self.graph.add((object_identifier, rdflib.RDF.type, prop_type))
                if parent_id:
                    # Add a relation to the parent, connecting the two nodes
                    self.graph.add((parent_id, prop_type, rdflib.URIRef(object_identifier)))
                new_parent = object_identifier
                self.sdtl_to_rdf(sdtl_object, new_parent)
            return parent_id

        # Loop over all the things in the sdtl
        for prop in sdtl:
            if prop == "producesDataframe" or prop == "consumesDataframe":
                continue
            if prop == "SourceInformation":
                # Create the rdf:Seq that will contain all of the SourceInformation objects
                information_inventory_id = self.id_manager.get_id("SourceInformationInventory")
                predicate = self.id_manager.sdtl_namespace.SourceInformation
                self.create_sequence(information_inventory_id, parent_id, predicate)

                # Loop over each SourceInformation. Add a node for each one and add it to the rdf:Seq
                source_info_count = 0
                for source_info in sdtl[prop]:
                    source_info_count += 1
                    source_information_id = self.id_manager.get_id("SourceInformation")
                    self.graph.add((source_information_id, rdflib.RDF.type,
                                    self.id_manager.sdtl_namespace.SourceInformation))
                    # Add it to the SourceInformationInventory
                    predicate = rdflib.URIRef(f'http://www.w3.org/1999/02/22-rdf-syntax-ns#rdf:_{source_info_count}')
                    self.graph.add((information_inventory_id, predicate, source_information_id))
                    self.sdtl_to_rdf(source_info, source_information_id)

            elif prop == "Arguments":
                # Create the rdf:Seq that will contain all of the SourceInformation objects
                arguments_inventory_id = self.id_manager.get_id("ArgumentsInventory")
                predicate = self.id_manager.sdtl_namespace.Arguments
                self.create_sequence(arguments_inventory_id, parent_id, predicate, False)

                # Loop over each 'Argumets'. Add a node for each one and add it to the rdf:Seq
                arguments_count = 0
                for source_info in sdtl[prop]:
                    arguments_count += 1
                    argument_id = self.id_manager.get_id(source_info["$type"])
                    argument_type = rdflib.URIRef(f'{self.id_manager.sdtl_namespace}{source_info["$type"]}')
                    self.graph.add((argument_id, rdflib.RDF.type, argument_type))

                    # Attach the ArgumentsInventory to it
                    predicate = rdflib.URIRef(f'http://www.w3.org/1999/02/22-rdf-syntax-ns#rdf:_{arguments_count}')
                    self.graph.add((arguments_inventory_id, predicate, argument_id))
                    self.sdtl_to_rdf(source_info, argument_id)

            # Check to see if it's a an SDTL object ie {'$type': 'VariableSymbolExpression', 'variableName': 'Interest'}
            if isinstance(sdtl[prop], dict):
                # Create a new RDF object
                sdtl_type = sdtl[prop]["$type"]
                object_identifier = self.id_manager.get_id(sdtl_type)
                prop_type = self.id_manager.get_property_id(prop)
                uri_type = rdflib.URIRef(f'{self.id_manager.sdtl_namespace}{sdtl_type}')
                self.graph.add((object_identifier, rdflib.RDF.type, uri_type))
                # Loop over each object inside and add it to the graph
                self.sdtl_to_rdf(sdtl[prop], object_identifier)
                if parent_id:
                    # Add a relation to the parent, connecting the two nodes
                    self.graph.add(
                        (parent_id, prop_type, rdflib.URIRef(object_identifier)))

            # If it's a list of SDTL objects [{prop1: "someVal", prop2: "someVal2"}, {}, {}]
            elif isinstance(sdtl[prop], list):
                if prop == 'SourceInformation' or prop == "Arguments":
                    continue
                # Loop over each object inside the list
                for sdtl_expression in sdtl[prop]:
                    # Create a new object
                    object_identifier = self.id_manager.get_id(prop)
                    prop_type = self.id_manager.get_property_id(prop)
                    uri_type = rdflib.URIRef(f'{self.id_manager.sdtl_namespace}{sdtl_expression["$type"]}')

                    self.graph.add((object_identifier, rdflib.RDF.type, uri_type))
                    if parent_id:
                            # Add a relation to the parent, connecting the two nodes
                        self.graph.add((parent_id, prop_type, rdflib.URIRef(object_identifier)))
                    new_parent = object_identifier
                    self.sdtl_to_rdf(sdtl_expression, new_parent)

            # Otherwise it's just a property that belongs to an existing object
            else:
                prop_type = self.id_manager.get_property_id(prop)
                if prop == "$type":
                    # Don't add sdtl:$type to the RDF
                    continue

                if len(object_identifiers):
                    for identifier in object_identifiers:
                        self.graph.add((parent_id, prop_type, identifier))
                else:
                    self.graph.add((parent_id, prop_type, rdflib.Literal(sdtl[prop])))

        return object_identifiers

    def add_program(self):
        """
        Adds a sdtl:Program node to the graph.
        :return:
        """
        program_id = self.id_manager.get_id("Program")
        self.graph.add((program_id, rdflib.RDF.type, self.id_manager.sdtl_namespace.Program))
        # Add all of the program level metadata
        for program_predicate in self.sdtl:
            if isinstance(self.sdtl[program_predicate], List):
                continue
            if program_predicate == "$type":
                # Don't add sdtl:$type to the RDF
                continue
            prop_type = self.id_manager.get_property_id(program_predicate)
            self.graph.add((program_id, prop_type, rdflib.Literal(self.sdtl[program_predicate])))
        return program_id

    def convert_sdtl_to_rdf(self):
        # A list of unsupported SDTL commands
        unsupported = ["Comment", "Unsupported", "NoTransformOp"]

        for sdtl_file in self.sdtl_files:
            with open(sdtl_file) as json_file:
                self.sdtl = json.load(json_file)

                # Create the node for the script, it should be sdtl:Program
                script_id = self.add_program()

                if 'Commands' in self.sdtl:
                    # Create the node for the commands list inside the sdtl:Program
                    commands_id = self.id_manager.get_id("CommandInventory")
                    # 'Commands' is an ordered sequence, use rdf:seq
                    self.graph.add((commands_id, rdflib.RDF.type, rdflib.RDF.Seq))

                    # Connect the Program to the Commands rdf:seq via sdtl:Commands
                    self.graph.add((script_id, self.id_manager.sdtl_namespace.Commands, commands_id))

                    command_count = 0
                    for command in self.sdtl['Commands']:
                        if command["$type"] in unsupported:
                            continue
                        command_count += 1
                        # Create the new command node
                        command_id = self.id_manager.get_id(command["$type"])
                        predicate = f'{self.id_manager.sdtl_namespace}{command["$type"]}'
                        self.graph.add((command_id,
                                        rdflib.RDF.type,
                                        rdflib.URIRef(predicate)))
                        # Connect it to the 'Commands' node using rdf:_n
                        predicate = f'http://www.w3.org/1999/02/22-rdf-syntax-ns#_{command_count}'
                        self.graph.add((commands_id,
                                        rdflib.URIRef(predicate),
                                        command_id))
                        if 'consumesDataframe' in command:
                            inventory_id = self.create_dataframe_inventory(command_id,
                                                                           command['consumesDataframe'],
                                                                           'ConsumesDataframe')
                            self.parse_dataframe_usage(inventory_id, command['consumesDataframe'])
                        if 'producesDataframe' in command :
                            inventory_id = self.create_dataframe_inventory(command_id,
                                                                           command['producesDataframe'],
                                                                           'ProducesDataframe')
                            # Connect each DataframeDescription to the newly created rdf:Seq
                            self.process_dataframe_descriptions(inventory_id, command['producesDataframe'])



                        self.sdtl_to_rdf(command, command_id)

    def parse_dataframe_usage(self, dataframe_inventory_id, sdtl):
        """

        :return:
        """
        dataframe_count = 0
        for dataframe in sdtl:
            dataframe_count += 1
            if 'dataframeName' not in dataframe:
                raise ValueError(f'A dataframe was used before being created.')

            dataframe_identifier = self.dataframes[dataframe['dataframeName']]
            # Connect the ProducesDataframe node to it with rdf:_n
            self.graph.add((dataframe_inventory_id,
                            rdflib.URIRef(f'http://www.w3.org/1999/02/22-rdf-syntax-ns#_{dataframe_count}'),
                            dataframe_identifier))

    def create_dataframe_inventory(self, command_id, sdtl: json, dataframe_relation: str):
        """
        Called when the parser runs across a command that creates a data frame.

        :param command_id: The identifier of the command creating the data frame
        :param sdtl: The SDTL list of data frames that are being used
        :param dataframe_relation: Either 'ProducesDataframe' or 'ConsumesDataframe'
        :return: None
        """

        # Create the rdf:Seq that will contain all of the data frames.
        # This object has a one to many relation between itself and each data frame, respectively
        dataframe_id = self.id_manager.get_id("DataframeInventory")

        self.graph.add((dataframe_id,
                        rdflib.RDF.type,
                        rdflib.RDF.Bag))

        # Connect the command to the rdf:Seq.
        predicate = rdflib.URIRef(f'{self.id_manager.sdtl_namespace}{dataframe_relation}')
        self.graph.add((command_id,
                        predicate,
                        dataframe_id))

        return dataframe_id

    def process_dataframe_descriptions(self, parent_id: rdflib.URIRef, dataframe_sdtl: json):
        """
        Handles the creation and linking of the DataframeDescription nodes.

        :param parent_id: The identifier of the rdf:Seq containing the data frames
        :param dataframe_sdtl: SDTL that holds the DataframeDescription JSON objects
        :return:
        """
        dataframe_count = 0
        for dataframe in dataframe_sdtl:
            dataframe_count += 1
            # Create a new DataframeDescription node to hold the data frame name and variables
            dataframe_description_id = self.id_manager.get_id("DataframeDescription")
            self.graph.add((dataframe_description_id,
                            rdflib.RDF.type,
                            self.id_manager.sdtl_namespace.DataframeDescription))

            # Connect the ProducesDataframe node to it with rdf:_n
            self.graph.add((parent_id,
                            rdflib.URIRef(f'http://www.w3.org/1999/02/22-rdf-syntax-ns#_{dataframe_count}'),
                            dataframe_description_id))

            # Add the dataframeName
            if 'dataframeName' in dataframe:
                self.dataframes[dataframe['dataframeName']] = dataframe_description_id
                self.graph.add((dataframe_description_id,
                                self.id_manager.sdtl_namespace.dataframeName,
                                rdflib.Literal(dataframe['dataframeName'])))

            # Create & add the variables to the 'ProducesDataFrame' node
            if 'variableInventory' in dataframe:
                self.parse_variable_inventory(dataframe_description_id, dataframe)

    def parse_variable_inventory(self, dataframe_description_id: rdflib.URIRef, dataframe: json):
        """
        Handles creating and connecting

        :param dataframe_description_id: The identifier of the parent DataframeDescription node
        :param dataframe: The SDTL describing the dataframe
        :return:
        """

        variable_inventory_id = self.id_manager.get_id("VariableInventory")
        predicate = self.id_manager.sdtl_namespace.VariableInventory
        self.create_sequence(variable_inventory_id, dataframe_description_id, predicate)
        self.add_variables_to_inventory(variable_inventory_id, dataframe)

    def add_variables_to_inventory(self, variable_inventory_id: rdflib.URIRef, dataframe: json):
        """
        Creates RDF objects for each variable in a VariableInventory object. It links the
        parent rdf:Seq to it.

        :param variable_inventory_id: The identifier of the VariableInventry node holding the variables
        :param dataframe: The SDTL describing the data frame
        :return:
        """
        variable_count = 0
        for dataframe_variable in dataframe['variableInventory']:
            variable_count += 1
            # dataframeVariable is made up by me
            new_variable_id = self.id_manager.get_id("dataframeVariable")
            self.graph.add((new_variable_id,
                            rdflib.RDF.type,
                            self.id_manager.sdtl_namespace.VariableSymbolExpression))
            self.graph.add((new_variable_id,
                            self.id_manager.sdtl_namespace.VariableName,
                            rdflib.Literal(dataframe_variable)))
            self.graph.add((variable_inventory_id,
                            rdflib.URIRef(f'http://www.w3.org/1999/02/22-rdf-syntax-ns#_{variable_count}'),
                            new_variable_id))

    def create_sequence(self, identifier, domain_identifier, predicate, ordered=True):

        sequence_type = rdflib.RDF.Seq if ordered else rdflib.RDF.Bag

        self.graph.add((identifier,
                        rdflib.RDF.type,
                        sequence_type))

        # Connect the domain object to the sequence
        self.graph.add((domain_identifier,
                        predicate,
                        identifier))

