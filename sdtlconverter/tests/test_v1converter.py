from sdtlconverter.ConverterV1 import ConverterV1
import rdflib
import os


def test_write_read():
    """
    Tests that the RDF produce can be read back by rdflib.

    """

    converter = ConverterV1("./integrated/single_load/load.json")
    converter.convert_sdtl_to_rdf()


    try:
        with open("test_jsonld.jsonld") as temp_file:
            rdflib.Graph().parse(data=temp_file.read(), format="json-ld")
    except Exception:
        assert False
    finally:
        os.remove("test_jsonld.jsonld")
