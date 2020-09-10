import rdflib
import json
from typing import Union
from uuid import uuid4


class Converter:

    def __init__(self, file_path):
        """
        Creates and runs the converter

        :param file_path: A path to an SDTL JSON file
        """

        # Counts used for creating sensible URIs
        self.sourceInformation_count = 0
        self.workflow_count = 0
        self.program_count = 0
        self.sourceInformation_count = 0
        self.port_count = 0
        self.expression_count = 0
        self.variable_count = 0

        # Create the ProvONE and SDTL namespaces. rdflib has the common ontologies already defined
        self.provone_ns = rdflib.Namespace("http://purl.dataone.org/provone/2015/01/15/ontology#")
        self.sdtl_namespace = rdflib.Namespace("sdtl#")

        self.graph = rdflib.Graph()
        self.sdtl = None
        self.store_sdtl(file_path)

        self.construct_prospective_provenance()

    def store_sdtl(self, file_path: str):
        """
        Opens an SDTL json file and store it in memory
        :param file_path:
        :return:
        """
        with open(file_path) as json_file:
            self.sdtl = json.load(json_file)

    def parse_outer_sdtl(self):
        # If there is at least one command present, create the workflow and
        # provone:program that represents the script
        if len(self.sdtl['commands']):
            self.workflow_count += 1
            workflow_uri = rdflib.URIRef("#workflow/{}".format(self.workflow_count))
            self.create_workflow(workflow_uri)

            self.program_count += 1
            script_uri = rdflib.URIRef("#program/{}".format(self.program_count))
            script_description = "A script that contains source code."
            self.create_script_program(script_uri,script_description)

            # Add the provone:hasSubProgram relation
            self.graph.add((workflow_uri, self.provone_ns.hasSubProgram, script_uri))
            return script_uri

    def create_workflow(self,
                        workflow_uri: rdflib.URIRef):
        """
        Creates an outer provone:Workflow object that holds all of the scripts

        The description and label are deterministic and hard coded; there should only be one top level
        workflow object.

        :param workflow_uri: The URI of the workflow
        :return: None
        """
        workflow_comment = rdflib.Literal("The top level workflow that holds all of the parsed scripts")
        workflow_label = rdflib.Literal("Top level workflow")

        self.graph.add((workflow_uri , rdflib.RDF.type, self.provone_ns.Workflow))
        self.graph.add((workflow_uri , rdflib.RDFS.comment, workflow_comment))
        self.graph.add((workflow_uri , rdflib.RDFS.label, workflow_label))

    def create_script_program(self,
                              identifer: rdflib.URIRef,
                              description: Union[str, None] = None):
        """
        Creates a provone record that represents a scrip containing code

        :param identifer: The identifier for the progrogram
        :param description: An optional description of the script
        :return: None
        """

        # Create the node
        self.graph.add((identifer, rdflib.RDF.type, self.provone_ns.Program))

        # Add the optional description
        if description:
            script_comment = rdflib.Literal(description)
            self.graph.add((identifer, rdflib.RDFS.comment, script_comment))

        # Add the SDTL
        wanted_properties = [
            "id",
            "sourceFileName",
            "sourceLanguage",
            "scriptMD5",
            "scriptSHA1",
            "sourceFileLastUpdate",
            "sourceFileSize",
            "lineCount",
            "commandCount",
            "parser",
            "modelCreatedTime"]

        for prop in wanted_properties:
            # Use URIRef instead of Namespace because of the way namespace props are set
            # ie sdtl_namespace.prop will create "sdtl#prop"
            self.graph.add((identifer, rdflib.term.URIRef('sdtl#{}'.format(prop)), rdflib.Literal(self.sdtl[prop])))

    def add_command_property(self, command: dict, parent_id=None):
        # Loop over all the things in the command
        for prop in command:
            # Create an identifier that may be used to define nested properties
            # THIS NEEDS TO BE HANDLED DIFFERENTLY. Probably by adding these to a list
            prop_identifer = rdflib.URIRef(str(uuid4()))
            if str(prop) == 'sourceInformation':
                self.sourceInformation_count += 1
                prop_identifer = rdflib.URIRef('{}{}/{}'.format('#', prop, str(self.sourceInformation_count)))
            if str(prop) == 'variable':
                self.variable_count += 1
                prop_identifer = rdflib.URIRef('{}{}/{}'.format('#', prop, str(self.variable_count)))
            if str(prop) == 'expression':
                self.expression_count += 1
                prop_identifer = rdflib.URIRef('{}{}/{}'.format('#', prop, str(self.expression_count)))
            is_dict=False

            if type(prop) == dict:
                is_dict=True
                self.add_command_property(prop, prop_identifer)
            try:
                sub_prop = command[str(prop)]
                if type(sub_prop) == dict or type(sub_prop) == list:
                    # Then there's a sub-object that needs to be created
                    object_type = rdflib.URIRef("#sdtl:{}".format(prop))
                    self.graph.add((prop_identifer, rdflib.RDF.type, object_type))
                    self.add_command_property(sub_prop, prop_identifer)
            except TypeError as e:
                print("! {}".format(e))
                pass

            if parent_id and not is_dict:
                # Add a relation to the parent, connecting the two nodes
                object = rdflib.URIRef("sdtl:{}".format(prop))
                is_dict = False
                try:
                    sub_prop = command[str(prop)]
                    if type(sub_prop) == dict or type(sub_prop) == list:
                        is_dict = True
                        object = rdflib.term.URIRef('#sdtl:{}'.format(prop))
                        self.graph.add((parent_id, object, rdflib.URIRef(prop_identifer)))
                except TypeError as e:
                    pass
                if not is_dict:
                    self.graph.add((parent_id, object, rdflib.Literal(command[prop])))
            if prop == 'variable':
                self.create_port(parent_id, 'hasOutPort')

    def create_port(self, parent_id, relation: str):
        """
        Creates a provone:Port

        :param parent_id: The ID of the provone:Program using or creating it
        :param relation: Should be hasInPort or hasOutPort
        :return:
        """
        self.port_count += 1
        port_id = rdflib.URIRef("#port/{}".format(self.port_count))
        self.graph.add((port_id, rdflib.RDF.type, self.provone_ns.Port))

        if parent_id:
            predicate = rdflib.URIRef("provone:{}".format(relation))
            self.graph.add((parent_id, predicate, port_id))

    def add_command(self, command_uri: rdflib.URIRef, command: json):
        """
        Adds a command and its sdtl to the graph

        :param command_uri:
        :param command:
        :return:
        """
        self.graph.add((command_uri, rdflib.RDF.type, self.provone_ns.Program))
        self.add_command_property(command, command_uri)

    def __str__(self) -> str:
        """
        Returns the graph as a turtle string
        :return:
        """
        return self.graph.serialize(format='turtle').decode('utf-8')

    def construct_prospective_provenance(self):
        """
        Creates a prospective representation of the SDTL
        :return:
        """

        # Parse and add information about the script
        parent_uri = self.parse_outer_sdtl()

        # Parse the commands
        program_ids = []
        for command in self.sdtl['commands']:
            # Come up with a new ID
            self.program_count += 1
            command_id = rdflib.URIRef("#program/{}".format(self.program_count))
            program_ids.append(command_id)
            self.add_command(command_id, command)

        # Add the new commands to the parent
        if parent_uri:
            for uri in program_ids:
                self.graph.add((parent_uri, self.provone_ns.hasSubProgram, uri))


converter = Converter('examples/three_commands/sdtl.json')
print(str(converter))
