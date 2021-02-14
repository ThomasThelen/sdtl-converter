from sdtlconverter.ConverterV1 import ConverterV1


def test_sort():
    """
    Test that the proper number of Sort nodes exist, that they have
    the expected identifiers
    :return: None
    """

    converter = ConverterV1("./sdtl.json")
    converter.convert_sdtl_to_rdf()
    converter.write_turtle()
    converter.write_jsonld()

    # Get the identifiers of all of the Rename nodes
    query = """
        PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
                SELECT ?sort_cases_ids ?sort_criteria_inventory_ids
                ?sort_criterion_ids ?sort_direction ?var_exp_ids
                ?var_name
        WHERE {
            ?sort_cases_ids rdf:type sdtl:SortCases .
            ?sort_cases_ids sdtl:SortCriteria ?sort_criteria_inventory_ids .
            ?sort_criteria_inventory_ids rdf:_1 ?sort_criterion_ids .
            ?sort_criterion_ids sdtl:sortDirection ?sort_direction .
            ?sort_criterion_ids sdtl:variable ?var_exp_ids .
            ?var_exp_ids sdtl:variableName ?var_name .
        }
    """
    res = converter.graph.query(query)
    assert len(res) > 0

    sort_cases_ids = []
    criteria_inventory_ids = []
    criteria_ids = []
    sort_direction = []
    var_exp_ids = []
    variable_names = []

    for row in res:
        sort_cases_ids.append(row[0])
        criteria_inventory_ids.append(row[1])
        criteria_ids.append(row[2])
        sort_direction.append(row[3])
        var_exp_ids.append(row[4])
        variable_names.append(row[5])

    sort_directionn_values = ["ascending", "descending"]
    assert len(sort_cases_ids) == 8
    assert len(criteria_inventory_ids) == 8
    assert len(criteria_ids) == 8
    assert len(var_exp_ids) == 8
    assert len(variable_names) == 8

    for sort_dir in sort_direction:
        assert str(sort_dir) in sort_directionn_values

    for variable_name in variable_names:
        assert str(variable_name) in ["A", "B", "C"]
