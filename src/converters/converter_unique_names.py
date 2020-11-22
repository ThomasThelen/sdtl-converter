from typing import Union, List
import rdflib
import json

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

        # A list of the sub-properties of the top level provone:Programs (has extension like .py, .R, etc) that
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

    def create_workflow(self):
        """
        Creates an outer provone:Workflow object that holds all of the scripts

        The description and label are deterministic and hard coded; there should only be one top level
        workflow object.

        :return:
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

        # Create the node
        self.graph.add((identifier, rdflib.RDF.type, self.id_manager.provone_ns.Program))

        # Add the optional description
        if description:
            script_comment = rdflib.Literal(description)
            self.graph.add((identifier, rdflib.RDFS.comment, script_comment))

        # There are a number of top level SDTL properties; we only want a few properties,
        # so use the filter list.
        for prop in self.desired_script_properties:
            # Use URIRef instead of Namespace because of the way namespace propertiess are set
            # ie sdtl_namespace.prop will create "sdtl#prop"
            predicate = self.id_manager.get_property_id(prop)

            if prop in self.sdtl:
                self.graph.add((identifier, rdflib.URIRef(predicate), rdflib.Literal(self.sdtl[prop])))

    def parse(self):
        for sdtl_file in self.sdtl_files:
            with open(sdtl_file) as json_file:
                self.sdtl = json.load(json_file)
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
                    elif command["$type"] == "DropVariables":
                        self.parse_drop_command(command)

    def add_output_dataframes(self, command, program_id):
        """

        :param command:
        :param program_id: The identifier of the provone:Program creating the data frames
        :return:
        """
        # Create the outport
        out_port_id = self.id_manager.get_id("Port")
        self.graph.add((out_port_id, rdflib.RDF.type, self.id_manager.provone_ns.Port))
        # Connect the outport to the program
        self.graph.add((program_id, self.id_manager.provone_ns.hasOutPort, out_port_id))
        for data_frame in command:
            # Create a new object for the data frame
            self.dataframes[data_frame["dataframeName"]] = out_port_id
            # Add the SDTL data frame name to it
            self.graph.add((out_port_id, self.id_manager.sdtl_namespace.dataframeName,
                            rdflib.Literal(data_frame["dataframeName"])))



    def parse_variable_usage(self, program_id, variable, is_dataframe=False):
        """

        :param program_id:
        :param commands:
        :return:
        """
        # Create the channel
        channel_id = self.id_manager.get_id("Channel")
        self.graph.add((channel_id,
                        rdflib.RDF.type,
                        self.id_manager.provone_ns.Channel))
        # Connect the original inport
        existing_id = None
        if is_dataframe:
            existing_id = self.dataframes[variable["dataframeName"]]
            self.graph.add((existing_id,
                            self.id_manager.provone_ns.connectsTo,
                            channel_id))
        elif variable["argumentValue"]["$type"] == "VariableSymbolExpression":
            existing_id = self.variable_names[variable["argumentValue"]["variableName"]]
            self.graph.add((existing_id,
                            self.id_manager.provone_ns.connectsTo,
                            channel_id))
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

        if is_dataframe:
            self.dataframes[variable["dataframeName"]] = new_port_id
        elif variable["argumentValue"]["$type"] == "VariableSymbolExpression":
            self.variable_names[variable["argumentValue"]["variableName"]] = new_port_id

    def parse_load_command(self, command):
        """
        Parses an sdtl Load command
        :param command:
        :return:
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

        if command['producesDataframe']:
            self.add_output_dataframes(command['producesDataframe'], program_id)

        source_info_ids = self.parse_source_information(command['sourceInformation'])
        for source_id in source_info_ids:
            self.graph.add((program_id, rdflib.URIRef('sdtl#sourceInformation'), source_id))

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

        if command['consumesDataframe']:
            for frame in command['consumesDataframe']:
                self.parse_variable_usage(program_id, frame, is_dataframe=True)
            # Connect the program to the port

            source_info_ids = self.parse_source_information(command['sourceInformation'])
            for source_id in source_info_ids:
                self.graph.add((program_id, rdflib.URIRef('sdtl#sourceInformation'), source_id))

    def parse_compute_command(self, command):
        # Create the program representing the command
        program_id = self.id_manager.get_id("Program")
        self.graph.add((program_id, rdflib.RDF.type, self.id_manager.provone_ns.Program))
        # Add its source information
        source_info_ids = self.parse_source_information(command['sourceInformation'])
        for source_id in source_info_ids:
            self.graph.add((program_id, rdflib.URIRef('sdtl#sourceInformation'), source_id))

        # Check if the command is using a dataframe
        if "consumesDataframe" in command:
            for frame in command['consumesDataframe']:
                self.parse_variable_usage(program_id, frame, is_dataframe=True)

        # See if a variable is being created
        if "variable" in command:
            self.add_output_variable(program_id, command["variable"])

        if "expression" in command:
            if command["expression"]["$type"] == "NumericConstantExpression":
                # Create the RDF object for it
                expression_id = self.id_manager.get_id("expression")
                # Connect it to the parent
                self.graph.add((program_id, self.id_manager.sdtl_namespace.expression, expression_id))
                self.add_sdtl_properties(expression_id, command["expression"])
            elif command["expression"]["$type"] == "FunctionCallExpression":
                self.parse_function_call(program_id, command["expression"])

    def add_output_variable(self, program_id, variable):
        # Create a port representing the variable
        out_port_id = self.id_manager.get_id("Port")
        self.graph.add((out_port_id, rdflib.RDF.type, self.id_manager.provone_ns.Port))
        # Connect the outport to the program
        self.graph.add((program_id, self.id_manager.provone_ns.hasOutPort, out_port_id))
        # Add the variable properties to the object
        self.add_sdtl_properties(out_port_id, variable)
        self.variable_names[variable["variableName"]] = out_port_id

    def add_sdtl_properties(self, object_id, object_json):
        for key in object_json.keys():
            source_info = f'sdtl#{key}'
            self.graph.add((object_id, rdflib.URIRef(source_info), rdflib.Literal(object_json[key])))

    def parse_function_call(self, program_id, expression):
        if "arguments" in expression:
            for argument in expression["arguments"]:
                self.parse_variable_usage(program_id, argument)
            # Create an in port for each argument


    def parse_drop_command(self, command):
        # Create the program representing the command
        program_id = self.id_manager.get_id("Program")
        self.graph.add((program_id, rdflib.RDF.type, self.id_manager.provone_ns.Program))
        # Add its source information
        source_info_ids = self.parse_source_information(command['sourceInformation'])
        for source_id in source_info_ids:
            self.graph.add((program_id, rdflib.URIRef('sdtl#sourceInformation'), source_id))

        # Create the port representing the input data frame
        if command['consumesDataframe']:
            item_count = 1
            for data_frame in command["consumesDataframe"]:
                in_port_id = self.id_manager.get_id("Port")
                self.graph.add((in_port_id, rdflib.RDF.type, self.id_manager.provone_ns.Port))
                self.graph.add((in_port_id, self.id_manager.provone_ns.dataframeName, rdflib.Literal(data_frame["dataframeName"])))
                existing_id = self.dataframes[data_frame["dataframeName"]]
                if existing_id is not None:
                    # Connect the program to it
                    self.graph.add((program_id,
                                    self.id_manager.provone_ns.hasInPort,
                                    rdflib.Literal(in_port_id)))
                    item_count += 1
                else:
                    raise ValueError("Using a dataframe that hasn't been defined! Exiting.")
        if command["variables"]:
            # Create the variable object
            variable_id = self.id_manager.get_id("variable")
            self.graph.add((variable_id, rdflib.RDF.type, self.id_manager.sdtl_namespace.variable))
            # Connect it to the parent program
            self.graph.add(
                (program_id, self.id_manager.sdtl_namespace.variable, rdflib.URIRef(variable_id)))
            for variable in command["variables"]:
                for key in variable.keys():
                    source_info = f'sdtl#{key}'
                    self.graph.add(
                        (variable_id, rdflib.URIRef(source_info), rdflib.Literal(variable[key])))

    def parse_source_information(self, source_information):
        # Create a new SourceInformation object
        source_ids = []
        if isinstance(source_information, list):
            for source_info in source_information:
                source_id = self.parse_single_source_information(source_info)
                source_ids.append(source_id)
        else:
            source_id = self.parse_single_source_information(source_information)
            source_ids.append(source_id)
        return source_ids

    def parse_single_source_information(self, source_info):
        source_information_id = self.id_manager.get_id("sourceInformation")
        self.graph.add((source_information_id, rdflib.RDF.type, self.id_manager.sdtl_namespace.SourceInformation))
        for key in source_info.keys():
            sdtl_predicate = f'sdtl#{key}'
            self.graph.add((source_information_id, rdflib.URIRef(sdtl_predicate), rdflib.Literal(source_info[key])))
        return source_information_id