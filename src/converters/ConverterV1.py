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

    def add_command_property(self, command: dict, parent_id=None) -> Union[str, List[str]]:
        """
        A recursive method that creates the appropriate provone objects and embeds the SDTL
        inside.

        :param command: The chunk of SDTL being processed. This can be a string, List of dicts, List of strings,
        or a dict.
        :param parent_id: The identifier of the parent that the SDTL chunk belongs to. This is
        used when connecting properties to their parents.
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
                self.add_command_property(command[prop], object_identifier)
                if parent_id:
                    # Add a relation to the parent, connecting the two nodes
                    self.graph.add(
                        (parent_id, prop_type, rdflib.URIRef(object_identifier)))

            # If it's a list of SDTL objects
            elif is_list:
                # Create a node to represent the list
                new_list = rdflib.BNode()
                # Check if its a list of strings or a list of dicts
                for sdtl_expression in command[prop]:
                    listItem1 = rdflib.BNode()

                    print(sdtl_expression)
                    if isinstance(sdtl_expression, dict):
                        parent_id = self.id_manager.get_property_id(prop)
                        self.add_command_property(sdtl_expression, parent_id)
                    elif isinstance(sdtl_expression, str):
                        print("It's a string!")


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

    def construct_provenance(self, retrospective=False, new_graph=True):
        """
        The main user-facing method that will create the complete provenance model. By default, it will produce
        retrospective provenance. Toggling the 'retrospective' flag will produce retrospective provenance
        alongside.

        :param retrospective: A flag to generate retrospective provenance
        :param new_graph: Flag to use a new graph
        :return:
        """
        # Create a new graph instance
        if new_graph:
            self.new_graph()
        # Parse the outer most SDTL (adds provone:Workflow & provone:Program)
        workflow_uri: str = self.create_workflow()
        # Parse and add each SDTL command in the program
        for sdtl_file in self.sdtl_files:
            with open(sdtl_file) as json_file:
                self.sdtl = json.load(json_file)
                name = "Program"
                script_uri = self.id_manager.get_id(name)
                script_description = "A script file that contains source code."
                self.create_script_program(script_uri, description=script_description)
                # Add the provone:hasSubProgram relation
                self.graph.add((workflow_uri, self.id_manager.provone_ns.hasSubProgram, script_uri))
                # Add the commands within the file
                for command in self.sdtl['commands']:
                    # Prepare to create the provenance by generating an identifier for the
                    # provone:Program that will hold the SDTL
                    name = "Program"
                    command_id = self.id_manager.get_id(name)
                    self.add_command(command_id, command)
                    if script_uri:
                        self.graph.add((script_uri, self.id_manager.provone_ns.hasSubProgram, command_id))

                if retrospective:
                    workflow_id: rdflib.URIRef  = self.get_workflow_identifier()
                    self.add_execution(workflow_id)
                    # Get all of the scripts that belong to the top level workflow
                    sub_programs = self.get_program_identifiers(workflow_id)
                    # Loop over each one and add provone:Execution
                    for sub_program in sub_programs:
                        self.add_retrospective(sub_program)

    def add_retrospective(self, parent_program_id):
        """

        :param parent_program_id:
        :return:
        """

        # Get all of the scripts that belong to the top level workflow
        sub_programs = self.get_program_identifiers(parent_program_id)
        for sub_program in sub_programs:
            self.add_execution(sub_program)
            # Process each of the commands in the script
            command_ids = self.get_command_identifiers(sub_program)
            for command_id in command_ids:
                self.add_execution(command_id)

    def add_program_execution(self, parent_execution):
        """
        Adds a provone:Execution that's associated with a provone:Program. The provone:Execution
        may be associated with a parent provone:Execution. If this is the case, it should be stated
        in the RDF.

        :return:
        """
        execution_id = self.id_manager.get_id('Execution')
        self.graph.add((execution_id, rdflib.RDF.type, self.id_manager.provone_ns.Execution))

        if parent_execution:
            self.graph.add((execution_id, self.id_manager.provone_ns.wasPartOf, parent_execution))

    def add_execution(self, program_id: rdflib.URIRef) -> rdflib.URIRef:
        """
        Creates a node that represents the execution of a provone:Program

        :param program_id: The identifier of the workflow object
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
        self.graph.add((association_id, self.id_manager.provone_ns.hadPlan, program_id))

        return execution_id

    def get_program_identifiers(self, workflow_id):
        """
        Get the identifiers of script-level programs (there should only be one).

        :param workflow_id: The identifier of the workflow holding the programs
        :return:
        """
        query = """
        PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?workflow_id ?sub_programs
        WHERE
        {
            ?workflow_id provone:hasSubProgram ?sub_programs .
        }
        """
        ids = []
        query_res = self.graph.query(query)
        try:
            for res in query_res:
                id = res.asdict()['workflow_id']
                if id == workflow_id:
                    ids.append(res.asdict()['sub_programs'])
        except KeyError:
            pass

        return ids

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

    def get_command_identifiers(self, script_id) -> list:
        """
        Gets the identifier of the command objects
        :param script_id: The identifier of the script (provone:Program) holding commands
        :return: The workflow's identifier
        """

        query = """
        PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?script_id ?sub_commands
        WHERE
        {
            ?script_id provone:hasSubProgram ?sub_commands.
        }
        """
        ids = []
        query_res = self.graph.query(query)
        try:
            for res in query_res:
                id = res.asdict()['script_id ']
                if id == script_id:
                    ids.append(res.asdict()['sub_commands'])
        except KeyError:
            pass

        return ids
