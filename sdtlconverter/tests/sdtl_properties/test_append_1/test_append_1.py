from sdtlconverter.ConverterV03 import ConverterV03
import rdflib
import json


def test_program_node():
    """
    Test that the sdtl:Program node is properly represented
    """

    converter = ConverterV03("sdtl_properties/test_append_1/sdtl.json")
    converter.convert_sdtl_to_rdf()

    # Check that sdtl:Program node exists and is properly named
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT ?program_id
    WHERE {
        ?program_id rdf:type sdtl:Program .
    }
    """

    res = converter.graph.query(query)
    assert len(res) > 0
    for row in res:
        assert row[0] == rdflib.URIRef("#Program/1")

    # Check that the program node has the expected properties
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT DISTINCT ?program_id ?source_filename
            ?source_language ?command_count ?parser ?parser_version ?commands_inventory
    WHERE {
        ?program_id rdf:type sdtl:Program .
        ?program_id sdtl:SourceFileName ?source_filename .
        ?program_id sdtl:SourceLanguage ?source_language .
        ?program_id sdtl:CommandCount ?command_count .
        ?program_id sdtl:Parser ?parser .
        ?program_id sdtl:ParserVersion ?parser_version .
        ?program_id sdtl:Commands ?commands_inventory
    }
    """

    res = converter.graph.query(query)
    with open("./sdtl_properties/test_append_1/sdtl.json") as json_file:
        sdtl = json.load(json_file)
        for row in res:
            assert rdflib.URIRef("#Program/1") == row[0]
            assert rdflib.Literal(sdtl["SourceFileName"]) == row[1]
            assert rdflib.Literal(sdtl["SourceLanguage"]) == row[2]
            assert rdflib.Literal(sdtl["CommandCount"]) == row[3]
            assert rdflib.Literal(sdtl["Parser"]) == row[4]
            assert rdflib.Literal(sdtl["ParserVersion"]) == row[5]
            assert rdflib.URIRef("#CommandInventory/1") == row[6]


def test_identifiers():
    """
    Test that the expected identifiers are present
    """
    converter = ConverterV03("./sdtl_properties/test_append/sdtl.json")
    converter.convert_sdtl_to_rdf()

    # Get all of the AppendDatasets identifiers
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT ?append_id
    WHERE {
        ?append_id rdf:type sdtl:AppendDatasets .
    }
    """

    res = converter.graph.query(query)
    assert len(res) > 0

    results = []
    for row in res:
        results.append(row[0])
    assert rdflib.URIRef("#AppendDatasets/1") in results
    assert rdflib.URIRef("#AppendDatasets/2") in results
    assert rdflib.URIRef("#AppendDatasets/3") in results

    # Check that there are three AppendFilesInventory nodes
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT DISTINCT ?append_files_id
    WHERE {
        ?append_dataset_id rdf:type sdtl:AppendDatasets .
        ?append_dataset_id sdtl:AppendFiles ?append_files_id .
    }
    """

    res = converter.graph.query(query)
    assert len(res) > 0

    results = []
    for row in res:
        results.append(row[0])

    for i in range(1, 3):
        assert rdflib.URIRef(f"#AppendFilesInventory/{i}") in results

    # Check that there are six AppendFileDescription nodes
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT DISTINCT ?append_file_desc
    WHERE {
        ?append_file_desc rdf:type sdtl:AppendFileDescription .
    }
    """

    res = converter.graph.query(query)
    assert len(res) > 0

    results = []
    for row in res:
        results.append(row[0])
    for i in range(1, 6):
        assert rdflib.URIRef(f"#AppendFileDescription/{i}") in results

