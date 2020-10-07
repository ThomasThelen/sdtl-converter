import json

import rdflib

from src.IdentifierManager import IdentifierManager
class Converter:

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

    def store_sdtl(self, file_path: str):
        """
        Opens an SDTL json file and store it in memory
        :param file_path:
        :return:
        """
        with open(file_path) as json_file:
            self.sdtl = json.load(json_file)

    def schema_to_name(self, schema_class) -> str:
        name = schema_class.__qualname__
        name = name[0].lower() + name[1:]
        return name

    def __str__(self) -> str:
        """
        Returns the graph as a turtle string
        :return:
        """
        return self.graph.serialize(format='turtle').decode('utf-8')
