from typing import Union, List
import rdflib
import json

from collections import OrderedDict
from .Converter import Converter
import schemas.generated.sdtl as sdtl


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
        self.desired_script_properties = [
            self.schema_to_name(sdtl.Id),
            self.schema_to_name(sdtl.SourceFileName),
            self.schema_to_name(sdtl.FileName),
            self.schema_to_name(sdtl.SourceLanguage),
            self.schema_to_name(sdtl.ScriptMD5),
            self.schema_to_name(sdtl.ScriptSHA1),
            self.schema_to_name(sdtl.SourceFileLastUpdate),
            self.schema_to_name(sdtl.SourceFileSize),
            self.schema_to_name(sdtl.LineCount),
            self.schema_to_name(sdtl.CommandCount),
            self.schema_to_name(sdtl.Parser),
            self.schema_to_name(sdtl.ModelCreatedTime)
        ]

        super().__init__(file_paths)

    def create_workflow(self) -> rdflib.URIRef:
        """
        Creates an outer provone:Workflow object that holds all of the scripts

        The description and label are deterministic and hard coded; there should only be one top level
        workflow object.

        :return: The URI of the workflow object
        """
        name = 'Workflow'
        workflow_uri = self.id_manager.get_id(name)

        workflow_comment = rdflib.Literal("The top level workflow that holds a number of scripts.")
        workflow_label = rdflib.Literal("Researcher workflow")

        self.graph.add((workflow_uri, rdflib.RDF.type, self.id_manager.provone_ns.Workflow))
        self.graph.add((workflow_uri, rdflib.RDFS.comment, workflow_comment))
        self.graph.add((workflow_uri, rdflib.RDFS.label, workflow_label))

        return workflow_uri

    def create_script_program(self, identifier: rdflib.URIRef,
                              description: str = None):
        """
        Creates a provone Program that represents a script containing code. The script is
        a file with the expected extensions (R, py, sps, etc).

        :param identifier: The identifier for the program
        :param description: An optional description of the script
        :return: None
        """

        # Create the RDF node that represents the script
        self.graph.add((identifier, rdflib.RDF.type, self.id_manager.provone_ns.Program))

        # Add the optional description
        if description:
            script_comment = rdflib.Literal(description)
            self.graph.add((identifier, rdflib.RDFS.comment, script_comment))

        # There are a number of top level SDTL properties; we only want a few properties,
        # so use the filter list.
        for prop in self.desired_script_properties:
            predicate = self.id_manager.get_property_id(prop)
            if prop in self.sdtl:
                self.graph.add((identifier, rdflib.URIRef(predicate), rdflib.Literal(self.sdtl[prop])))

    def parse(self):
        """
        The main method that iterates over the top level SDTL

        :return: None
        """
        for sdtl_file in self.sdtl_files:
            with open(sdtl_file) as json_file:
                self.sdtl = json.load(json_file) #, object_pairs_hook=OrderedDict)
                for command in self.sdtl['commands']:
                    if command["$type"] == "Comment":
                        pass
                    elif command["$type"] == "NoTransformOp":
                        pass
                    elif command["$type"] == "Load":
                        self.parse_load_command(command)
                    elif command["$type"] == "Save":
                        self.parse_save_command(command)
                    elif command["$type"] == "Compute":
                        self.parse_compute_command(command)

    def parse_dataframe_creation(self, produces_dataframe_command: json, program_id: rdflib.URIRef):
        """
        Takes a list of objects in a "producesDataframe" SDTL chunk and creates the appropriate ports
        and SDTL-RDF.

        :param produces_dataframe_command: A list of dataframes defined in the SDTL-JSON
        :param program_id: The identifier of the provone:Program that's creating the dataframes
        :return: None
        """

        # Loop over each data frame object in the list
        for new_dataframe in produces_dataframe_command:
            # Create the outport representing the new dataframe
            out_port_id = self.id_manager.get_id("Port")
            self.graph.add((out_port_id, rdflib.RDF.type, self.id_manager.provone_ns.Port))
            # Connect the provone:Program to the new port
            self.graph.add((program_id, self.id_manager.provone_ns.hasOutPort, out_port_id))
            # Update the dict of dataframes so that it contains the most recent identifier
            self.dataframes[new_dataframe["dataframeName"]] = out_port_id
            # Add the SDTL data frame name to the port
            self.graph.add((out_port_id, self.id_manager.sdtl_namespace.dataframeName,
                            rdflib.Literal(new_dataframe["dataframeName"])))

            # Create and attach any potential variables to the port
            if "variableInventory" in new_dataframe:
                # Create an rdf:seq to hold the variable inventory
                inventory_id = self.id_manager.get_id("variableInventory")
                self.graph.add((inventory_id, rdflib.RDF.type, rdflib.RDF.Seq))
                self.graph.add((out_port_id, self.id_manager.sdtl_namespace.variableInventory, inventory_id))
                item_count = 1
                for new_variable in new_dataframe["variableInventory"]:
                    variable_id = self.id_manager.get_id("variable")
                    self.graph.add((variable_id, rdflib.RDF.type, self.id_manager.schema_ns.Thing))
                    self.graph.add((variable_id, self.id_manager.schema_ns.name, rdflib.Literal(new_variable)))
                    # Connect the rdf:Bag to it
                    self.graph.add((inventory_id,
                                    rdflib.URIRef(f'http://www.w3.org/1999/02/22-rdf-syntax-ns#rdf:_{item_count}'),
                                    variable_id))
                    item_count += 1

    def parse_dataframe_usage(self, program_id, usage_sdtl: json):
        """
        Called when the parser runs across a command that uses a dataframe.

        :param program_id: The identifier of the provone:Program that is using the data frame
        :param usage_sdtl: The SDTL list of data frames that are being used
        :return: None
        """

        # Loop over each data frame object in the list of data frames
        for frame in usage_sdtl:

            # Create the provone:Channel
            channel_id = self.id_manager.get_id("Channel")
            self.graph.add((channel_id,
                            rdflib.RDF.type,
                            self.id_manager.provone_ns.Channel))
            # Get the most recent identifier of the data frame
            try:
                existing_id = self.dataframes[frame["dataframeName"]]
                self.graph.add((existing_id,
                                    self.id_manager.provone_ns.connectsTo,
                                    channel_id))
            except KeyError:
                raise ValueError('Error: The data frame with name {frame["dataframeName"]} is being '
                                 'used before it was created. Aborting.')
            # Create the new port
            new_port_id = self.id_manager.get_id("Port")
            self.graph.add((new_port_id,
                            rdflib.RDF.type,
                            self.id_manager.provone_ns.Port))
            # Connect it to the channel
            self.graph.add((new_port_id,
                            self.id_manager.provone_ns.connectsTo,
                            channel_id))
            # Connect the program to it
            self.graph.add((program_id,
                            self.id_manager.provone_ns.hasInPort,
                            rdflib.Literal(new_port_id)))

            self.dataframes[frame["dataframeName"]] = new_port_id

    def parse_load_command(self, command):
        """
        Parses an sdtl Load command
        :param command:
        :return: None
        """

        # Create the program representing the load command
        program_id = self.id_manager.get_id("Program")
        self.graph.add((program_id, rdflib.RDF.type, self.id_manager.provone_ns.Program))
        # Create the port representing the input (the file)
        in_port_id = self.id_manager.get_id("Port")
        self.graph.add((in_port_id, rdflib.RDF.type, self.id_manager.provone_ns.Port))
        # Connect the program to the port
        self.graph.add((program_id, self.id_manager.provone_ns.hasInPort, in_port_id))

        # Add load-command properties
        self.graph.add((in_port_id, self.id_manager.sdtl_namespace.FileName, rdflib.Literal(command['fileName'])))

        if 'producesDataframe' not in command:
            raise ValueError("Loading is only supported for SDTL that has producesDataFrame annotated")

        self.parse_dataframe_creation(command['producesDataframe'], program_id)
        # Create the port representing the dataframe that waas created
        #self.add_output_dataframes(command['producesDataframe'], program_id)
        # Add the SDTL SourceInformation to the command
        self.parse_source_information(command['sourceInformation'], program_id)

    def parse_save_command(self, command):
        """
        Parses an sdtl save command
        :param command:
        :return:
        """
        # Create the program representing the save command
        program_id = self.id_manager.get_id("Program")
        self.graph.add((program_id, rdflib.RDF.type, self.id_manager.provone_ns.Program))

        # Create the outport
        out_port_id = self.id_manager.get_id("Port")
        self.graph.add((out_port_id, rdflib.RDF.type, self.id_manager.provone_ns.Program))

        # Put the filename in the port
        self.graph.add((out_port_id, self.id_manager.sdtl_namespace.FileName, rdflib.Literal(command['fileName'])))

        # Connect the outport to the program
        self.graph.add((program_id, self.id_manager.provone_ns.hasOutPort, out_port_id))

        if 'consumesDataframe' not in command:
            raise ValueError("The Save command only supports saving dataframes")

        if 'consumesDataframe' in command:
            self.parse_dataframe_usage(program_id, command['consumesDataframe'])

        # Add the relevant SDTL SourceInformation blocks
        self.parse_source_information(command['sourceInformation'], program_id)

    def parse_compute_command(self, command: json):
        """
        Parses an SDTL command of type 'compute'

        :param command: The SDTL-JSON containing the command
        :return: None
        """
        # Create the program representing the command
        program_id = self.id_manager.get_id("Program")
        self.graph.add((program_id, rdflib.RDF.type, self.id_manager.provone_ns.Program))

        # Add its source information
        self.parse_source_information(command['sourceInformation'], program_id)

        if 'consumesDataframe' in command:
            self.parse_dataframe_usage(program_id, command['consumesDataframe'])

        if 'producesDataframe' in command:
            self.parse_dataframe_creation(command['producesDataframe'], program_id)

        if 'variable' in command:
            # Create a new variable object
            variable_id = self.id_manager.get_id("variable")
            self.graph.add((variable_id, rdflib.RDF.type, self.id_manager.sdtl_namespace.Variable))
            # Add it to the parent program
            self.graph.add((program_id, self.id_manager.sdtl_namespace.variable, variable_id))
            self.sdtl_to_rdf(command['variable'], variable_id)

        if "expression" in command:
            # Convert to SDTL and add back to the program
            expresion_id = self.id_manager.get_id("expression")
            self.graph.add((expresion_id, rdflib.RDF.type, self.id_manager.sdtl_namespace.Expression))
            # Add it to the parent program
            self.graph.add((program_id, self.id_manager.sdtl_namespace.expression, expresion_id))
            self.sdtl_to_rdf(command['expression'], expresion_id)

    def parse_source_information(self, source_information: List, program_id: rdflib.URIRef):
        """
        Turns an sdtl:SourceInformation block into RDF and attaches it to the associated provone:Program

        :param source_information: A list of sdtl:SourceInformation blocks
        :param program_id: The identifier of the provone:Program that represents this source code
        :return: None
        """
        for source_info in source_information:
            source_information_id = self.id_manager.get_id("sourceInformation")
            self.graph.add((source_information_id, rdflib.RDF.type, self.id_manager.sdtl_namespace.SourceInformation))
            for key in source_info.keys():
                source_info_item = f'sdtl#{key}'
                self.graph.add((source_information_id, rdflib.URIRef(source_info_item), rdflib.Literal(source_info[key])))
            self.graph.add((program_id, rdflib.URIRef('sdtl#sourceInformation'), source_information_id))

    def sdtl_to_rdf(self, sdtl, parent_id: rdflib.URIRef):
        """
        Turns a block of SDTL into RDF, recursively.

        :param sdtl: The SDTL being turned into RDF
        :param parent_id: The identifier of the parent object that this object/property belongs to
        :return:
        """

        # Identifiers of child objects that the parent links to.
        object_identifiers = []

        # Loop over all the things in the sdtl
        for prop in sdtl:
            # Check to see if it's a an SDTL object ie {'$type': 'VariableSymbolExpression', 'variableName': 'Interest'}
            if isinstance(sdtl[prop], dict):
                # Create a new RDF object
                object_identifier = self.id_manager.get_id(prop)
                prop_type = self.id_manager.get_property_id(prop)
                self.graph.add((object_identifier, rdflib.RDF.type, prop_type))
                # Loop over each object inside and add it to the graph
                self.sdtl_to_rdf(sdtl[prop], object_identifier)
                if parent_id:
                    # Add a relation to the parent, connecting the two nodes
                    self.graph.add(
                        (parent_id, prop_type, rdflib.URIRef(object_identifier)))

            # If it's a list of SDTL objects [{prop1: "someVal", prop2: "someVal2"}, {}, {}]
            elif isinstance(sdtl[prop], list):
                # Loop over each object inside the list
                for sdtl_expression in sdtl[prop]:
                    # Create a new
                    object_identifier = self.id_manager.get_id(prop)
                    prop_type = self.id_manager.get_property_id(prop)
                    self.graph.add((object_identifier, rdflib.RDF.type, prop_type))
                    if parent_id:
                            # Add a relation to the parent, connecting the two nodes
                        self.graph.add((parent_id, prop_type, rdflib.URIRef(object_identifier)))
                    new_parent = object_identifier
                    self.sdtl_to_rdf(sdtl_expression, new_parent)

            # Otherwise it's just a property that belongs to an existing object
            else:
                prop_type= self.id_manager.get_property_id(prop)
                if len(object_identifiers):
                    for identifier in object_identifiers:
                        self.graph.add((parent_id, prop_type, identifier))
                else:
                    self.graph.add((parent_id, prop_type, rdflib.Literal(sdtl[prop])))

        return object_identifiers
