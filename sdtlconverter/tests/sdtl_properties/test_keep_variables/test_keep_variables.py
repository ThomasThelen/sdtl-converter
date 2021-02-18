from sdtlconverter.ConverterV03 import ConverterV03

import rdflib


def test_get_kept_variables():
    """
    Test that the identifier is expected and that the variable
    kept is also expected.
    :return: None
    """

    converter = ConverterV03("./sdtl_properties/test_keep_variables/sdtl.json")
    converter.convert_sdtl_to_rdf()

    # What is one variable name that is kept?
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT ?keep_var_id ?var_name
    WHERE {
        ?keep_var_id rdf:type sdtl:KeepVariables .
        ?keep_var_id sdtl:Variables ?var_inventory_id .
        ?var_inventory_id rdf:_1 ?var_symbol_expression_id .
        ?var_symbol_expression_id sdtl:variableName ?var_name .
    }
    """
    res = converter.graph.query(query)
    assert len(res) > 0
    for row in res:
        assert row[0] == rdflib.URIRef("#KeepVariables/1")
        assert row[1] == rdflib.Literal("A")
