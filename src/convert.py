import rdflib
import json
from typing import Union, List
import logging

import schemas.generated.sdtl as sdtl
from src.IdentifierManager import IdentifierManager
class Converter:
    """
    A class that handles the conversion from SDTL to ProvONE.
    """

    def __init__(self, file_path: str):
        """
        Creates and runs the converter

        :param file_path: A path to an SDTL JSON file
        """

        self.id_manager = IdentifierManager()

        self.graph = rdflib.Graph()
        self.graph.bind("sdtl", self.id_manager.sdtl_namespace)
        self.graph.bind("provone", self.id_manager.provone_ns)
        self.sdtl = None
        self.store_sdtl(file_path)

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

    def store_sdtl(self, file_path: str):
        """
        Opens an SDTL json file and store it in memory
        :param file_path:
        :return:
        """
        with open(file_path) as json_file:
            self.sdtl = json.load(json_file)

    def parse_outer_sdtl(self, prospective=True) -> str:
        """
        Parses the top level SDTL
        :return:
        """
        # If there is at least one command present, create the workflow and
        # provone:program that represents the script
        if len(self.sdtl['commands']):
            name = 'Workflow'
            workflow_uri = self.id_manager.get_id(name)
            self.create_workflow(workflow_uri)

            if prospective:
                name = "Program"
                script_uri = self.id_manager.get_id(name)
                script_description = "A script file that contains source code."
                self.create_script_program(script_uri,script_description)

                # Add the provone:hasSubProgram relation
                self.graph.add((workflow_uri, self.id_manager.provone_ns.hasSubProgram, script_uri))
                return script_uri

    def create_workflow(self, workflow_uri: rdflib.URIRef):
        """
        Creates an outer provone:Workflow object that holds all of the scripts

        The description and label are deterministic and hard coded; there should only be one top level
        workflow object.

        :param workflow_uri: The URI of the workflow (the subject)
        :return: None
        """
        workflow_comment = rdflib.Literal("The top level workflow that holds any number of scripts")
        workflow_label = rdflib.Literal("Researcher workflow")

        self.graph.add((workflow_uri , rdflib.RDF.type, self.id_manager.provone_ns.Workflow))
        self.graph.add((workflow_uri , rdflib.RDFS.comment, workflow_comment))
        self.graph.add((workflow_uri , rdflib.RDFS.label, workflow_label))

    def create_script_program(self, identifier: rdflib.URIRef,
                              description: str = None):
        """
        Creates a provone Program that represents a script containing code

        :param identifier: The identifier for the progrogram
        :param description: An optional description of the script
        :return: None
        """

        # Create the node
        self.graph.add((identifier, rdflib.RDF.type, self.id_manager.provone_ns.Program))

        # Add the optional description
        if description:
            script_comment = rdflib.Literal(description)
            self.graph.add((identifier, rdflib.RDFS.comment, script_comment))

        # There are a number of top level SDTL properties; we only want a few propeties,
        # so use the filter list.
        for prop in self.desired_script_properties:
            # Use URIRef instead of Namespace because of the way namespace propertiess are set
            # ie sdtl_namespace.prop will create "sdtl#prop"
            predicate = self.id_manager.get_property_id(prop)

            if prop in self.sdtl:
                self.graph.add((identifier, rdflib.URIRef(predicate), rdflib.Literal(self.sdtl[prop])))

    def add_command_property(self, command: dict, parent_id=None, child_id=None) -> Union[str, List[str]]:
        """
        A recursive method that creates the appropriate provone objects and embeds the SDTL
        inside.

        :param command:
        :param parent_id:
        :param child_id:
        :return:
        """

        # Identifiers of child objects that the parent links to.
        object_identifiers = []
        # Loop over all the things in the command

        for prop in command:
            is_dict=isinstance(command[prop], dict)
            is_list = isinstance(command[prop], list)

            # If it's a an SDTL object ie {'$type': 'VariableSymbolExpression', 'variableName': 'Interest'}
            if is_dict:
                if prop == 'Comment':
                    return
                object_identifier = self.id_manager.get_id(prop)
                prop_type = self.id_manager.get_property_id(prop)
                self.graph.add((object_identifier, rdflib.RDF.type, prop_type))
                new_identifiers = self.add_command_property(command[prop], object_identifier)
                if parent_id:
                    # Add a relation to the parent, connecting the two nodes
                    self.graph.add(
                        (parent_id, prop_type, rdflib.URIRef(object_identifier)))

            # If it's a list of SDTL objects
            elif is_list:
                # Check if its a list of strings or a list of objects
                if isinstance(command[prop], dict):
                    1+1
                for sdtl_expression in command[prop]:
                    parent_id = self.id_manager.get_property_id(prop)
                    self.add_command_property(sdtl_expression, parent_id)

            # Otherwise it's just a property that belongs to an existing object
            else:
                prop_type= self.id_manager.get_property_id(prop)
                if len(object_identifiers):
                    for identifier in object_identifiers:
                        self.graph.add((parent_id, prop_type, identifier))
                else:
                    self.graph.add((parent_id, prop_type, rdflib.Literal(command[prop])))

            if prop == 'variable':
                self.create_port(parent_id, 'hasOutPort')

        return object_identifiers

    def create_port(self, parent_id, relation: str):
        """
        Creates a provone:Port

        :param parent_id: The ID of the provone:Program using or creating it
        :param relation: Should be hasInPort or hasOutPort
        :return:
        """
        name = "Port"
        port_id = self.id_manager.get_id(name)
        self.graph.add((port_id, rdflib.RDF.type, self.id_manager.provone_ns.Port))

        if parent_id:
            predicate = rdflib.URIRef(f'{self.id_manager.provone_ns}{relation}')
            self.graph.add((parent_id, predicate, port_id))

    def add_command(self, command_uri: rdflib.URIRef, command: json):
        """
        Adds a command and its sdtl to the graph

        :param command_uri:
        :param command:
        :return:
        """
        logging.info("Adding command")
        self.graph.add((command_uri, rdflib.RDF.type, self.id_manager.provone_ns.Program))
        self.add_command_property(command, command_uri)

    def __str__(self) -> str:
        """
        Returns the graph as a turtle string
        :return:
        """
        return self.graph.serialize(format='turtle').decode('utf-8')

    def construct_prospective_provenance(self):
        """
        Creates a prospective provenance model.

        :return:
        """

        # Parse the outer most SDTL (adds provone:Workflow & provone:Program)
        parent_uri: str = self.parse_outer_sdtl()
        # Parse and add each SDTL command to the graph
        for command in self.sdtl['commands']:
            # Prepare to create the provenance by gernerating an identifier for the
            # provone:Program that will hold the SDTL
            name = "Program"
            command_id = self.id_manager.get_id(name)
            self.add_command(command_id, command)
            if parent_uri:
                self.graph.add((parent_uri, self.id_manager.provone_ns.hasSubProgram, command_id))

    def schema_to_name(self, schema_class) -> str:
        name = schema_class.__qualname__
        name = name[0].lower() + name[1:]
        return name


converter = Converter('../examples/compute_drop/sdtl.json')
converter.construct_prospective_provenance()
print(str(converter))