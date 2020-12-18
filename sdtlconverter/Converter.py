from typing import List, Union
import rdflib
from sdtlconverter.IdentifierManager import IdentifierManager


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

    def __str__(self) -> str:
        """
        Returns the graph as a turtle
        :return:
        """
        return self.graph.serialize(format='turtle').decode('utf-8')

    def write_turtle(self, filepath: str = "./rdf.ttl"):
        """
        Writes the graph to disk in turtle format

        :param filepath: The path to the file being written to
        :return:
        """
        with open(filepath, 'wb') as turtle_file:
            turtle_file.write(self.graph.serialize(format='turtle'))

    def write_jsonld(self, filepath: str = "./rdf.jsonld"):
        """
        Writes the graph to disk in JSON-LD

        :param filepath: The path to the file being written to
        :return:
        """
        with open(filepath, 'wb') as turtle_file:
            context = {"rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
                       "schema": "http://www.schema.org/#",
                       "sdtl": "https://rdf-vocabulary.ddialliance.org/sdtl#"}

            turtle_file.write(self.graph.serialize(format='json-ld', context=context))
