from sdtlconverter.ConverterV03 import ConverterV03
import rdflib


def test_identifiers():
    """
    Test that the proper number of renames nodes exist and that they have
    the expected identifiers
    :return: None
    """

    converter = ConverterV03("./sdtl_properties/test_renames/sdtl.json")
    converter.convert_sdtl_to_rdf()
    converter.write_turtle()
    converter.write_jsonld()

    # Get the identifiers of all of the Rename nodes
    query = """
        PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
                SELECT ?rename_ids ?rename_inventory_id ?first_rename_pair
        WHERE {
            ?rename_ids rdf:type sdtl:Rename .
            ?rename_ids sdtl:Renames ?rename_inventory_id .
            ?rename_inventory_id rdf:_1 ?first_rename_pair .
        }
    """
    res = converter.graph.query(query)
    assert len(res) > 0
    merged_dataset_ids = []
    rename_inventory_ids = []
    rename_pair_ids = []
    for row in res:
        merged_dataset_ids.append(row[0])
        rename_inventory_ids.append(row[1])
        rename_pair_ids.append(row[2])

    # Make sure that the correct 4 Rename nodes are present
    assert len(merged_dataset_ids) == 4
    assert len(rename_inventory_ids) == 4
    assert len(rename_pair_ids) == 4
    for i in range(1, 4):
        assert rdflib.URIRef(f"#Rename/{i}") in merged_dataset_ids
        assert rdflib.URIRef(f"#RenamesInventory/{i}") in rename_inventory_ids


def test_variable_names():
    """
    Tests that all of the variable names that were renamed are in the graph
    :return: None
    """

    converter = ConverterV03("./sdtl_properties/test_renames/sdtl.json")
    converter.convert_sdtl_to_rdf()
    # Get the identifiers of all of the Rename nodes
    query = """
        PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
                SELECT ?variable_expression_id ?variable_name
        WHERE {
            ?variable_expression_id rdf:type sdtl:VariableSymbolExpression .
            ?variable_expression_id sdtl:variableName ?variable_name .
        }
    """
    res = converter.graph.query(query)
    assert len(res) > 0
    expression_ids = []
    variable_names = []
    for row in res:
        expression_ids.append(row[0])
        variable_names.append(row[1])
    assert len(expression_ids) == 14
    assert len(variable_names) == 14
    variables = ["A", "x", "one", "b", "two", "a", "B", "y"]
    for i in range(1, 13):
        assert rdflib.URIRef(f"#VariableSymbolExpression/{i}") in expression_ids

    for var_name in variable_names:
        assert str(var_name) in variables
