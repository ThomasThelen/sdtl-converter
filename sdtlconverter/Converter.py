from typing import List, Union
import rdflib
from sdtlconverter.IdentifierManager import IdentifierManager


class Converter:
    """
    A base class for converting SDTL JSON files into a graph representation
    that can be serialized as turtle or JSON-LD.
    """

    def __init__(self, file_paths: Union[List[str], str]):
        """
        Creates an instance of the converter.

        :param file_paths: A path or list of paths to an SDTL JSON file
        """
        self.sdtl_files: List[str] = [file_paths] if isinstance(file_paths, str) else file_paths
        self.id_manager: IdentifierManager = IdentifierManager()
        self.sdtl = None
        self.graph: rdflib.Graph = rdflib.Graph()
        self.bind_namespaces()

    def bind_namespaces(self):
        """
        Adds relevant namespaces to the graph.
        """
        self.graph.bind("sdtl", self.id_manager.sdtl_namespace)

    def __str__(self) -> str:
        """
        Returns the graph as a turtle.
        :return: A string representation of the graph
        """
        return self.graph.serialize(format='turtle').decode('utf-8')

    def write_turtle(self, filepath: str = "./sdtl.ttl"):
        """
        Writes the graph to disk in turtle format.

        :param filepath: The path to the file being written to
        :return: None
        """
        with open(filepath, 'wb') as turtle_file:
            turtle_file.write(self.graph.serialize(format='turtle'))

    def write_jsonld(self, filepath: str = "./sdtl.jsonld"):
        """
        Writes the graph to disk in JSON-LD.

        :param filepath: The path to the file being written to
        :return: None
        """
        with open(filepath, 'wb') as turtle_file:
            context = {"rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
                       "sdtl": "https://rdf-vocabulary.ddialliance.org/sdtl#"}
            turtle_file.write(self.graph.serialize(format='json-ld', context=context))
