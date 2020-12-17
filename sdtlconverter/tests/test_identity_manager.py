import rdflib

from sdtlconverter.IdentifierManager import IdentifierManager


def test_init():
    id_manager = IdentifierManager()
    assert len(id_manager.counts) > 0


def test_get_id():
    id_manager = IdentifierManager()
    identifier = id_manager.get_id('Program')
    assert identifier == rdflib.URIRef('#Program/1')


def test_get_property_id():
    id_manager = IdentifierManager()
    identifier = id_manager.get_id('fileName')
    assert identifier == rdflib.URIRef('#fileName/1')


def test_to_lower():
    id_manager = IdentifierManager()
    input_string = "Uppercase"
    expected_string = "uppercase"
    assert id_manager.to_lower(input_string) == expected_string
