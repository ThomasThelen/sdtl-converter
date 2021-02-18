from sdtlconverter.ConverterV03 import ConverterV03

import rdflib


def test_identifiers():
    """
    Test that the proper number of KeepCases nodes exist and that they have
    the expected identifiers
    :return:
    """

    converter = ConverterV03("./sdtl_properties/test_keep_cases/sdtl.json")
    converter.convert_sdtl_to_rdf()
    converter.write_turtle()
    converter.write_jsonld()

    # Get the identifiers of all of the KeepCases nodes, their conditions, and
    # the attached argument nodes. Note that the last KeepCases doesn't have an rdf:_2
    query = """
        PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
                SELECT ?keep_cases_id ?condition_id ?argument_ids ?first_function_argument
        WHERE {
            ?keep_cases_id rdf:type sdtl:KeepCases .
            ?keep_cases_id sdtl:condition ?condition_id .
            ?condition_id sdtl:Arguments ?argument_ids .
            ?argument_ids rdf:_1 ?first_function_argument .
        }
        """
    res = converter.graph.query(query)
    assert len(res) > 0
    cases = []
    conditions = []
    arguments = []
    first_f_arguments = []
    second_f_arguments = []
    for row in res:
        cases.append(row[0])
        conditions.append(row[1])
        arguments.append(row[2])
        first_f_arguments.append(row[3])
        second_f_arguments.append(row[3])

    for i in range(1, 4):
        assert rdflib.URIRef(f"#KeepCases/{i}") in cases

    # There are other FunctionCallExpression nodes that aren't related to the
    # KeepCases nodes, so just make sure that there's one for each KeepCases node
    # rather than checking the ID (because it may change each time the graph is created)
    assert len(conditions) == 4
    assert len(arguments) == 4
    assert len(first_f_arguments) == 4


def test_keep_cases_functioncallexpression():
    """
    Tests that the first KeepCases object has the expected FunctionCallExpression
    properties
    :return: None
    """

    converter = ConverterV03("./sdtl_properties/test_keep_cases/sdtl.json")
    converter.convert_sdtl_to_rdf()
    converter.write_turtle()
    converter.write_jsonld()

    # Get all of the variable values that are kept
    query = """
        PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
                SELECT ?arg_name ?var_name
        WHERE {
            ?keep_cases_id rdf:type sdtl:KeepCases .
            ?keep_cases_id sdtl:condition ?condition_id .
            ?condition_id sdtl:Arguments ?argument_ids .
            ?argument_ids rdf:_1 ?first_function_argument .
            ?first_function_argument sdtl:argumentName ?arg_name .
            ?first_function_argument sdtl:argumentValue ?arg_value_id .
            ?arg_value_id sdtl:variableName ?var_name .
        }
        """
    res = converter.graph.query(query)
    assert len(res) > 0
    values = []
    names = []
    for row in res:
        names.append(row[0])
        values.append(row[1])

    assert rdflib.Literal("EXP1") in names
    assert rdflib.Literal("A") in values
