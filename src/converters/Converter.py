from typing import List, Union
import rdflib
from src.IdentifierManager import IdentifierManager


class Converter:

    def __init__(self, file_paths: Union[List[str], str]):
        """
        Creates and runs the converter

        :param file_path: A path to an SDTL JSON file
        """
        self.id_manager = IdentifierManager()
        self.sdtl_files: List[str] = None
        self.new_graph()
        self.sdtl = None
        self.is_prospective=False
        self.is_retrospective = False
        if isinstance(file_paths, str):
            self.sdtl_files = [file_paths]
        else:
            self.sdtl_files: List[str] = file_paths

    def new_graph(self):
        self.graph = rdflib.Graph()
        self.graph.bind("sdtl", self.id_manager.sdtl_namespace)
        self.graph.bind("provone", self.id_manager.provone_ns)
        self.graph.bind("schema", self.id_manager.schema_ns)
        self.graph.bind("sdtl", rdflib.Namespace('sdtl#$'))

    @staticmethod
    def schema_to_name(schema_class) -> str:
        """
        Lowercases the first letter in a string. This is used to map the SDTL generated
        from the SDTLL parsers(lowercase first letter) to the schema (which has an uppercase letter)

        :param schema_class: The class name of an SDTL schema binding
        :return:
        """
        name = schema_class.__qualname__
        name = name[0].lower() + name[1:]
        return name

    def __str__(self) -> str:
        """
        Returns the graph as a turtle
        :return:
        """
        return self.graph.serialize(format='turtle').decode('utf-8')

    def write_turtle(self, filepath: str = "./turtle.ttl"):
        """
        Writes the graph to disk in turtle format

        :param filepath: The path to the file being written to
        :return:
        """
        with open(filepath, 'wb') as turtle_file:
            turtle_file.write(self.graph.serialize(format='turtle'))

    def write_jsonld(self, filepath: str = "./jsonld.jsonld"):
        """
        Writes the graph to disk in JSON-LD

        :param filepath: The path to the file being written to
        :return:
        """
        with open(filepath, 'wb') as turtle_file:
            turtle_file.write(self.graph.serialize(format='json-ld'))
