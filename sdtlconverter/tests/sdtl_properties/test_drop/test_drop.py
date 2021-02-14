from sdtlconverter.ConverterV1 import ConverterV1

import rdflib


def test_drop_identifiers():
    """
    Check that there are the expected number of DropVariables nodes and that they
    have the expected identifiers.
    :return: None
    """

    converter = ConverterV1("./sdtl.json")
    converter.convert_sdtl_to_rdf()
    converter.write_turtle()

    # Get the drop identifiers
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT ?drop_var_id
    WHERE {
        ?drop_var_id rdf:type sdtl:DropVariables.
    }
    """

    res = converter.graph.query(query)
    assert len(res) > 0
    comment_ids = []
    for row in res:
        comment_ids.append(row[0])

    for i in range(1, 4):
        assert rdflib.URIRef(f"#DropVariables/{i}") in comment_ids


def test_drop_variables_content():
    """
    Test that the contents of DropVariables is expected
    :return: None
    """
    converter = ConverterV1("./sdtl.json")
    converter.convert_sdtl_to_rdf()
    # Get the ID of the command that references #VariablesInventory/1
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT ?drop_id
    WHERE {
        ?drop_id sdtl:Variables <#VariablesInventory/1>.
    }
    """
    res = converter.graph.query(query)
    assert len(res) > 0
    for row in res:
        assert row[0] == rdflib.URIRef("#DropVariables/1")

    # Get the ID of the command that references #VariablesInventory/1
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT ?var_name
    WHERE {
        <#DropVariables/1> sdtl:Variables ?data_var_inventory_id .
        ?data_var_inventory_id rdf:_1 ?symbol_expression_id .
        ?symbol_expression_id sdtl:variableName ?var_name .
    }
    """
    res = converter.graph.query(query)
    assert len(res) > 0
    for row in res:
        print(row)
        assert row[0] == rdflib.Literal("A")

