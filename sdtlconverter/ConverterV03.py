from typing import Union, List
import rdflib
import json

from sdtlconverter.Converter import Converter


class ConverterV03(Converter):
    """
    Take SDTL conforming to version ___ and converts it into a format compatible with the
    SDTL OWL specification.
    """

    def __init__(self, file_paths: Union[List, str]):
        """
        Creates a converter instance. It can take any number of SDTL file paths as a list,
        or a single file path as a string. When using a list of files, they're combined into a single
        graph.

        :param file_paths: A path to an SDTL JSON file
        """

        self.dataframes = {}
        self.variable_names = {}
        # SDTL properties that are not ordered. These are mapped to rdf:bag
        self.unordered_properties = ["renames"]
        # SDTL properties that are are ordered. These are mapped to rdf:seq
        self.ordered_properties = ["SourceInformation", "sortCriteria", "mergeFiles", "dropVariables",
                                  "variables", "collapse", "arguments", "appendFiles", "renameVariables",
                                  "messageText", "aggregateVariables"]

        super().__init__(file_paths)

    def process_sdtl(self, sdtl: json) -> json:
        """
        Adds $type to all of the SDTL objects that are missing it

        :return: The SDTL documennt with type annotations
        """

        typeless_properties = """{ "noType": [
                {"command": "Aggregate", "property": "aggregateVariables", "reqType": "Compute"   },
                {"command": "AppendDatasets", "property": "appendFiles", "reqType": "AppendFileDescription"   },
                {"command": "AppendFileDescription", "property": "renameVariables", "reqType": "RenamePair"   },
                {"command": "Collapse", "property": "aggregateVariables", "reqType": "Compute" },
                {"command": "FunctionCallExpression", "property": "arguments", "reqType": "FunctionArgument"  },
                {"command": "LoopOverList", "property": "iterators", "reqType": "IteratorDescription"  },
                {"command": "MergeDatasets", "property": "mergeFiles", "reqType": "MergeFileDescription" },
                {"command": "MergeFileDescription", "property": "renameVariables", "reqType": "RenamePair" },
                {"command": "Recode", "property": "recodedVariables", "reqType": "RecodeVariable" },
                {"command": "Recode", "property": "rules", "reqType": "RecodeRule" },
                {"command": "Rename", "property": "renames", "reqType": "RenamePair" },
                {"command": "ReshapeLong", "property": "makeItems", "reqType": "ReshapeItemDescription" },
                {"command": "ReshapeWide", "property": "makeItems", "reqType": "ReshapeItemDescription" },
                {"command": "SetValueLabels", "property": "labels", "reqType": "ValueLabel" },
                {"command": "SortCases", "property": "sortCriteria", "reqType": "SortCriterion" }
                ]
            }"""

        #with open("schemas/NoType.json") as f:
        noTypejson = json.loads(typeless_properties)
        noTypeCnt = len(noTypejson['noType'])

        ##  Add $type to sourceInformation property
        cmndCnt = len(sdtl['commands'])
        ##  iterate over commands
        for key1 in range(cmndCnt):

            ## iterate within sourceInformation
            propCnt = len(sdtl['commands'][key1]['sourceInformation'])
            for key2 in range(propCnt):
                if '$type' not in sdtl['commands'][key1]['sourceInformation'][key2]:
                    sdtl['commands'][key1]['sourceInformation'][key2].update({"$type": "SourceInformation"})

            ## iterate within producesDataframe
            if 'producesDataframe' in sdtl['commands'][key1]:
                propCnt = len(sdtl['commands'][key1]['producesDataframe'])
                for key2 in range(propCnt):
                    if 'producesDataframe' in sdtl['commands'][key1]:
                        if '$type' not in sdtl['commands'][key1]['producesDataframe'][key2]:
                            sdtl['commands'][key1]['producesDataframe'][key2].update(
                                {"$type": "DataframeDescription"})

            ## iterate within consumesDataframe
            if 'consumesDataframe' in sdtl['commands'][key1]:
                propCnt = len(sdtl['commands'][key1]['consumesDataframe'])
                for key2 in range(propCnt):
                    if 'consumesDataframe' in sdtl['commands'][key1]:
                        if '$type' not in sdtl['commands'][key1]['consumesDataframe'][key2]:
                            sdtl['commands'][key1]['consumesDataframe'][key2].update(
                                {"$type": "DataframeDescription"})

            ##  iterate over properties that do not require $type ---
            noTypeCnt = len(noTypejson['noType'])
            for key3 in range(noTypeCnt):
                ntCommand = noTypejson['noType'][key3]['command']
                ntProperty = noTypejson['noType'][key3]['property']

                ## check for command in noTypejson
                if sdtl['commands'][key1]["command"] == ntCommand and ntProperty in sdtl['commands'][key1]:

                    ## iterate over array within property
                    propCnt = len(sdtl['commands'][key1][ntProperty])
                    for key4 in range(propCnt):

                        ## check for presence of $type
                        if '$type' not in sdtl['commands'][key1][ntProperty][key4]:
                            sdtl['commands'][key1][ntProperty][key4].update(
                                {"$type": noTypejson['noType'][key3]['reqType']})
        return sdtl


    def sdtl_to_rdf(self, sdtl: json, parent_id: rdflib.URIRef) -> Union[rdflib.URIRef, list]:
        """
        Turns a block of SDTL into RDF, recursively.

        :param sdtl: The SDTL being turned into RDF
        :param parent_id: The identifier of the parent object that this object/property belongs to
        :return: The identifier of the node created to represennt the SDTL
        """

        # Identifiers of child objects that the parent links to.
        object_identifiers = []
        if isinstance(sdtl, List):

            for sdtl_object in sdtl:
                # Create a new object
                object_identifier = self.id_manager.get_id(sdtl_object['$type'])

                prop_type = self.id_manager.get_property_id(self.id_manager.to_upper(sdtl_object['$type']))
                self.graph.add((object_identifier, rdflib.RDF.type, prop_type))
                if parent_id:
                    # Add a relation to the parent, connecting the two nodes
                    self.graph.add((parent_id, self.id_manager.prop_type, rdflib.URIRef(object_identifier)))
                new_parent = object_identifier
                self.sdtl_to_rdf(sdtl_object, new_parent)
            return parent_id

        # Loop over all the things in the sdtl
        for prop in sdtl:
            # Skip any of the top level properties that have already been created
            if prop == "producesDataframe" or prop == "consumesDataframe":
                continue
            elif prop in self.ordered_properties:
                child_type = None
                if prop == "SourceInformation":
                    child_type ="SourceInformation"
                self.create_sdtl_object(prop, parent_id, sdtl, True, child_type=child_type)
            elif prop in self.unordered_properties:
                self.create_sdtl_object(prop, parent_id, sdtl, False)

            # Check to see if it's a an SDTL object ie {'$type': 'VariableSymbolExpression', 'variableName': 'Interest'}
            elif isinstance(sdtl[prop], dict):
                # Create a new RDF object
                sdtl_type = sdtl[prop]["$type"]
                object_identifier = self.id_manager.get_id(sdtl_type)
                prop_type = self.id_manager.get_property_id(self.id_manager.to_upper(prop))
                uri_type = rdflib.URIRef(f'{self.id_manager.sdtl_namespace}{self.id_manager.to_upper(sdtl_type)}')
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
                    uri_type = rdflib.URIRef(f'{self.id_manager.sdtl_namespace}{self.id_manager.to_upper(sdtl_expression["$type"])}')
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

    def create_sdtl_object(self, name, parent_id, sdtl, ordered, child_type=None):
        """

        :param name: The name of the property
        :param parent_id: The node ID that this property belongs to
        :param sdtl: The SDTL that the property is referring to
        :param ordered: Whether or not the property is ordered
        :param child_type: The SDTL type that the child is
        :return:
        """
        # Create the rdf:Seq that will contain all of the objects
        upper_name = self.id_manager.to_upper(name)
        namespace_name = rdflib.URIRef(f'{self.id_manager.sdtl_namespace}{upper_name}')
        inventory_id = self.id_manager.get_id(f'{upper_name}Inventory')
        self.create_sequence(inventory_id, parent_id, namespace_name, ordered)

        # Loop over each node. Add a node for each one and add it to the rdf:Seq
        child_count = 0
        if isinstance(sdtl[name][0], str):
            # Create the node
            for string_property in sdtl[name]:
                child_count = child_count+1
                node_id = self.id_manager.get_id(name)
                node_type = rdflib.URIRef(f'{self.id_manager.sdtl_namespace}{name}')

                predicate = rdflib.URIRef(f'http://www.w3.org/1999/02/22-rdf-syntax-ns#_{child_count}')
                self.graph.add((inventory_id, predicate, rdflib.Literal(string_property)))
        else:
            for source_info in sdtl[name]:
                child_count += 1
                if child_type is None:
                    node_id = self.id_manager.get_id(source_info["$type"])
                    argument_type = rdflib.URIRef(f'{self.id_manager.sdtl_namespace}{source_info["$type"]}')
                else:
                    node_id = self.id_manager.get_id(child_type)
                    argument_type = rdflib.URIRef(f'{self.id_manager.sdtl_namespace}{child_type}')
                self.graph.add((node_id, rdflib.RDF.type, argument_type))

                # Attach the ArgumentsInventory to it
                predicate = rdflib.URIRef(f'http://www.w3.org/1999/02/22-rdf-syntax-ns#_{child_count}')
                self.graph.add((inventory_id, predicate, node_id))
                self.sdtl_to_rdf(source_info, node_id)

    def add_program(self) -> rdflib.URIRef:
        """
        Creates an sdtl:Program node to the graph.
        :return The node identifier for the Program
        """
        # Get the identifier for the node
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
        # unsupported = ["Unsupported", "NoTransformOp"]

        for sdtl_file in self.sdtl_files:
            with open(sdtl_file) as json_file:
                self.sdtl = json.load(json_file)
                self.sdtl = self.process_sdtl(self.sdtl)
                # Create the sdtl:Program that represents the script
                script_id = self.add_program()

                if 'commands' in self.sdtl:
                    # Create the node for the commands list inside the sdtl:Program
                    commands_id = self.id_manager.get_id("CommandInventory")
                    # 'commands' is an ordered sequence, use rdf:seq
                    self.graph.add((commands_id, rdflib.RDF.type, rdflib.RDF.Seq))

                    # Connect the Program to the commands rdf:seq via sdtl:commands
                    self.graph.add((script_id, self.id_manager.sdtl_namespace.Commands, commands_id))

                    command_count = 0
                    for command in self.sdtl['commands']:
                        command_count += 1
                        # Create the new command node
                        command_id = self.id_manager.get_id(command["$type"])
                        predicate = f'{self.id_manager.sdtl_namespace}{self.id_manager.to_upper(command["$type"])}'
                        self.graph.add((command_id,
                                        rdflib.RDF.type,
                                        rdflib.URIRef(predicate)))
                        # Connect it to the 'commands' node using rdf:_n
                        predicate = f'http://www.w3.org/1999/02/22-rdf-syntax-ns#_{command_count}'
                        self.graph.add((commands_id,
                                        rdflib.URIRef(predicate),
                                        command_id))
                        if 'producesDataframe' in command:
                            inventory_id = self.create_dataframe_inventory(command_id,
                                                                           command['producesDataframe'],
                                                                           'ProducesDataframe')
                            # Connect each DataframeDescription to the newly created rdf:Seq
                            self.process_dataframe_descriptions(inventory_id, command['producesDataframe'])

                        if 'consumesDataframe' in command:
                            inventory_id = self.create_dataframe_inventory(command_id,
                                                                           command['consumesDataframe'],
                                                                           'ConsumesDataframe')
                            self.parse_dataframe_usage(inventory_id, command['consumesDataframe'])
                        self.sdtl_to_rdf(command, command_id)

    def parse_dataframe_usage(self, dataframe_inventory_id, sdtl):
        """

        :return: None
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
        Creates DataframeInventory nodes.

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
                                self.id_manager.sdtl_namespace.DataframeName,
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
            new_variable_id = self.id_manager.get_id("VariableSymbolExpression")
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
        """
        Creates an rdf:Seq or rdf:Bag and connects a node to it.

        :param identifier: The identifier of the new node
        :param domain_identifier: The identifier of the node being attached
        :param predicate: The verb used to attach the node to the collection
        :param ordered: Boolean as to whether the collection is ordered or not
        :return: None
        """
        sequence_type = rdflib.RDF.Seq if ordered else rdflib.RDF.Bag

        self.graph.add((identifier,
                        rdflib.RDF.type,
                        sequence_type))

        # Connect the domain object to the sequence
        self.graph.add((domain_identifier,
                        predicate,
                        identifier))
