from typing import Union, List
import rdflib
import json

from .Converter import Converter
import schemas.generated.sdtl as sdtl


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

    def create_workflow(self) -> rdflib.URIRef:
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

    def parse_load_command(self, command):

        # Create the program representing the load command
        program_id = self.id_manager.get_id("Program")
        self.graph.add((program_id, rdflib.RDF.type, self.id_manager.provone_ns.Program))

        # Create the port representing the input (the file)
        in_port_id = self.id_manager.get_id("Port")
        self.graph.add((in_port_id, rdflib.RDF.type, self.id_manager.provone_ns.Port))

        # Connect the program to the port

        self.graph.add((program_id, self.id_manager.provone_ns.hasInPort, in_port_id))

        # Put the filename in the port (NOTE: THIS MIGHT *TECHNICALLY* BE ILLEGAL (check domain of the fileName)
        self.graph.add((in_port_id, self.id_manager.sdtl_namespace.FileName, rdflib.Literal(command['fileName'])))

        # Create the outport
        out_port_id = self.id_manager.get_id("Port")
        self.graph.add((out_port_id, rdflib.RDF.type, self.id_manager.provone_ns.Port))
        self.graph.add((out_port_id, rdflib.RDF.type, rdflib.RDF.Bag))

        # Connect the outport to the program
        self.graph.add((program_id, self.id_manager.provone_ns.hasOutPort, out_port_id))

        if command['producesDataframe']:
            item_count=1
            for data_frame in command["producesDataframe"]:
                # Create a new object for the data frame
                data_frame_id = self.id_manager.get_id("dataFrame")
                self.graph.add((data_frame_id, rdflib.RDF.type, rdflib.Literal("schema:Thing")))
                # Add the SDTL data frame name to it
                self.graph.add((data_frame_id, self.id_manager.sdtl_namespace.dataframeName, rdflib.Literal(data_frame["dataframeName"])))
                # Connect the rdf:Bag to it
                self.graph.add((out_port_id, rdflib.URIRef(f'http://www.w3.org/1999/02/22-rdf-syntax-ns#rdf:_{item_count}'), data_frame_id))
                item_count+=1

        source_info_id = self.parse_source_information(command['sourceInformation'])
        self.graph.add((program_id, rdflib.URIRef('sdtl#sourceInformation'), source_info_id))

    def parse_save_command(self, command):
        # Create the program representing the load command
        program_id = self.id_manager.get_id("Program")
        self.graph.add((program_id, rdflib.RDF.type, self.id_manager.provone_ns.Program))

        # Create the port representing the input
        in_port_id = self.id_manager.get_id("Port")
        self.graph.add((in_port_id, rdflib.RDF.type, self.id_manager.provone_ns.Port))
        self.graph.add((in_port_id, rdflib.RDF.type, rdflib.RDF.Bag))

        # Connect the program to the port
        self.graph.add((program_id, self.id_manager.provone_ns.hasInPort, in_port_id))

        # Create the outport
        out_port_id = self.id_manager.get_id("Port")
        self.graph.add((out_port_id, rdflib.RDF.type, self.id_manager.provone_ns.Program))

        # Put the filename in the port
        self.graph.add((out_port_id, self.id_manager.sdtl_namespace.FileName, rdflib.Literal(command['fileName'])))

        # Connect the outport to the program
        self.graph.add((program_id, self.id_manager.provone_ns.hasOutPort, out_port_id))

        if command['consumesDataframe']:
            item_count=1
            for data_frame in command["consumesDataframe"]:
                # Create a new object for the data frame
                data_frame_id = self.id_manager.get_id("dataFrame")
                self.graph.add((data_frame_id, rdflib.RDF.type, rdflib.Literal("schema:Thing")))
                # Add the SDTL data frame name to it
                self.graph.add((data_frame_id, self.id_manager.sdtl_namespace.dataframeName, rdflib.Literal(data_frame["dataframeName"])))
                # Connect the rdf:Bag to it
                self.graph.add((in_port_id, rdflib.URIRef(f'http://www.w3.org/1999/02/22-rdf-syntax-ns#rdf:_{item_count}'), data_frame_id))
                item_count+=1

        source_info_id = self.parse_source_information(command['sourceInformation'])
        self.graph.add((program_id, rdflib.URIRef('sdtl#sourceInformation'), source_info_id))





    def parse_source_information(self, source_information):
        # Create a new SourceInformation object
        source_information_id = self.id_manager.get_id("sourceInformation")
        self.graph.add((source_information_id, rdflib.RDF.type, self.id_manager.sdtl_namespace.SourceInformation))
        for key in source_information.keys():
            source_info = f'sdtl#{key}'
            self.graph.add((source_information_id, rdflib.URIRef(source_info), rdflib.Literal(source_information[key])))

        return source_information_id



























