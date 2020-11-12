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
        if isinstance(file_paths, str):
            self.sdtl_files = [file_paths]
        else:
            self.sdtl_files: List[str] = file_paths

    def new_graph(self):
        self.graph = rdflib.Graph()
        self.graph.bind("sdtl", self.id_manager.sdtl_namespace)
        self.graph.bind("provone", self.id_manager.provone_ns)

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
