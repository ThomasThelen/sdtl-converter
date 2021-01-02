from sdtlconverter.ConverterV1 import ConverterV1
import rdflib
import json


def test_program_node():
    """
    Test that the sdtl:Program node is properly represented
    """

    converter = ConverterV1("./load.json")
    converter.convert_sdtl_to_rdf()
    converter.write_turtle()