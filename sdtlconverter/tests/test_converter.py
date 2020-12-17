
import rdflib

from sdtlconverter.Converter import Converter

def test_init():
    """
    Test that when a new converter, the input file
    is properly saved and that the graph is initialized.
    :return:
    """
    converter = Converter('test_sdtl.json')
    assert converter.sdtl is None
    assert len(converter.sdtl_files) == 1
    assert converter.graph is not None


def test_new_graph():
    """
    Test that when the graph is initialized, the sdtl & provone
    namespaces are present.
    :return:
    """
    converter = Converter('test_sdtl.json')
    namespaces = [x[0] for x in converter.graph.namespaces()]
    assert 'sdtl' in namespaces
    assert 'provone' in namespaces
