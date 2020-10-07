from typing import Union, List
import rdflib
import json

from .Converter import Converter
import schemas.generated.sdtl as sdtl


class ConverterV1(Converter):
    """
    A converter that takes SDTL 1.0 and produces a ProvONE representation.
    """

    def __init__(self, file_path: str):
        """
        Creates and runs the converter

        :param file_path: A path to an SDTL JSON file
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

        super().__init__(file_path)


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
                    pass
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
        self.graph.add((command_uri, rdflib.RDF.type, self.id_manager.provone_ns.Program))
        self.add_command_property(command, command_uri)

    def construct_provenance(self, prospective=True, retrospective=False):
        """
        Creates a prospective provenance model.

        :return:
        """

        # Parse the outer most SDTL (adds provone:Workflow & provone:Program)
        parent_uri: str = self.parse_outer_sdtl()
        # Parse and add each SDTL command to the graph
        for command in self.sdtl['commands']:
            # Prepare to create the provenance by generating an identifier for the
            # provone:Program that will hold the SDTL
            name = "Program"
            command_id = self.id_manager.get_id(name)
            self.add_command(command_id, command)
            if parent_uri:
                self.graph.add((parent_uri, self.id_manager.provone_ns.hasSubProgram, command_id))

        if retrospective:
            workflow_id = self.get_workflow_identifier()
            self.add_workflow_execution(workflow_id)

    def get_workflow_identifier(self) -> rdflib.URIRef:
        """
        Gets the identifier of the top level Workflow object

        :return: The workflow's identifier
        """

        query = """
        PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT ?workflow_id
        WHERE
        {
          ?workflow_id rdf:type <http://purl.dataone.org/provone/2015/01/15/ontology#Workflow> .
        }
        """

        query_res: rdflib.query.Result = self.graph.query(query)
        # Return the identifier
        try:
            for res in query_res:
                return res.asdict()['workflow_id']
        except KeyError:
            pass

    def add_workflow_execution(self, workflow_id: rdflib.URIRef) -> rdflib.URIRef:
        """
        Creates a node that represents the execution of the workflow

        :param workflow_id: The identifier of the workflow object
        :return: The URI of the execution object
        """
        # Create a new identifier for the execution
        execution_id = self.id_manager.get_id('Execution')
        self.graph.add((execution_id, rdflib.RDF.type, self.id_manager.provone_ns.Execution))

        # Recall that provone:Execution connects back to the workflow via an intermediate provone:Association object.
        association_id = self.id_manager.get_id('Association')
        self.graph.add((association_id, rdflib.RDF.type, self.id_manager.provone_ns.Association))

        # Connect the Workflow to the Association
        self.graph.add((execution_id, self.id_manager.provone_ns.qualifiedAssociation, association_id))

        # Connect the Association to the Workflow
        self.graph.add((association_id, self.id_manager.provone_ns.hadPlan, workflow_id))

        return execution_id

    def get_program_identifiers(self):

        query = """
        PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT ?program_identifier
        WHERE
        {
          ?program_identifier rdf:type ?type .
          FILTER exists { ?program_identifier rdf:type <http://purl.dataone.org/provone/2015/01/15/ontology#Program> }
        }
        """

        query_res = self.graph.query(query)
        print(f'Queried!')
        for row in query_res:
            # I
            print(row)