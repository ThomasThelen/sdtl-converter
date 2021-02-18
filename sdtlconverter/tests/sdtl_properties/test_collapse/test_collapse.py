from sdtlconverter.ConverterV03 import ConverterV03


def test_program_node():
    """
    Test that the sdtl:Program node is properly represented
    """

    converter = ConverterV03("./sdtl_properties/test_collapse/sdtl.json")
    converter.convert_sdtl_to_rdf()
    converter.write_turtle()
    converter.write_jsonld()


def test_collapse():
    """
    Check that the collapse node is correct
    :return:
    """
    converter = ConverterV03("./sdtl_properties/test_collapse/sdtl.json")
    converter.convert_sdtl_to_rdf()

    # Get all of the AppendDatasets identifiers
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT ?collapse_id
    WHERE {
        ?collapse_id rdf:type sdtl:Collapse .
    }
    """

    res = converter.graph.query(query)
    assert len(res) > 0

    collapse_nodes = []
    for row in res:
        collapse_nodes.append(row[0])

    assert len(collapse_nodes) == 6
