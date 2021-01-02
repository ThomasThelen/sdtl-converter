from sdtlconverter.ConverterV1 import ConverterV1

import rdflib

def test_load():

    converter = ConverterV1("./sdtl.json")
    converter.convert_sdtl_to_rdf()
    converter.write_turtle()