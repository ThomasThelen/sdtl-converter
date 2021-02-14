from sdtlconverter.ConverterV1 import ConverterV1
import rdflib
import os


def test_write_read():
    """
    Tests that the RDF produce can be read back by rdflib. If there's an
    error while parsing the file back, let the exception throw and fail the test.

    """

    converter = ConverterV1("./integrated/single_load/sdtl.json")
    converter.convert_sdtl_to_rdf()
    converter.write_jsonld("test_jsonld.jsonld")
    try:
        with open("test_jsonld.jsonld") as temp_file:
            rdflib.Graph().parse(data=temp_file.read(), format="json-ld")
    except Exception:
        assert False
    finally:
        os.remove("test_jsonld.jsonld")


def test_namespaces():
    """
    Tests that the namespaces are correctly prefixed
    """
    converter = ConverterV1("./integrated/single_load/sdtl.json")
    converter.convert_sdtl_to_rdf()
    converter.write_jsonld("test_jsonld.jsonld")
    try:
        with open("test_jsonld.jsonld") as temp_file:
            graph = rdflib.Graph().parse(data=temp_file.read(), format="json-ld")
            for namespace in graph.namespaces():
                if namespace[1] == rdflib.URIRef("https://rdf-vocabulary.ddialliance.org/sdtl#"):
                    assert namespace[0] == "sdtl"
                elif namespace[1] == rdflib.URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#"):
                    assert namespace[0] == "rdf"
    except Exception:
        assert False
    finally:
        os.remove("test_jsonld.jsonld")

