from sdtlconverter.ConverterV1 import ConverterV1
import rdflib
import json


def add_member_relations(converter: ConverterV1):
    """

    :param converter:
    :return:
    """
    item_count = rdflib.URIRef("#Program/1")
    for i in range(0, 9):
        item_id = f'rdf:_{i}'

        converter.graph.add((rdflib.URIRef((item_count,
                                           rdflib.RDFS.subPropertyOf,
                                           rdflib.RDFS.member))))


def test_program_node():
    """
    Test that the sdtl:Program node is properly represented
    :return:
    """

    converter = ConverterV1("./load.json")
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

    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT DISTINCT ?program_id ?source_filename
            ?source_language ?command_count ?parser ?parser_version
    WHERE {
        ?program_id rdf:type sdtl:Program .
        ?program_id sdtl:SourceFileName ?source_filename .
        ?program_id sdtl:SourceLanguage ?source_language .
        ?program_id sdtl:CommandCount ?command_count .
        ?program_id sdtl:Parser ?parser .
        ?program_id sdtl:ParserVersion ?parser_version.
    }
    """

    res = converter.graph.query(query)
    with open("./load.json") as json_file:
        sdtl = json.load(json_file)
        for row in res:
            assert row[0] == rdflib.URIRef("#Program/1")
            assert row[1] == rdflib.Literal(sdtl["SourceFileName"])
            assert row[2] == rdflib.Literal(sdtl["SourceLanguage"])
            assert row[3] == rdflib.Literal(sdtl["CommandCount"])
            assert row[4] == rdflib.Literal(sdtl["Parser"])
            assert row[5] == rdflib.Literal(sdtl["ParserVersion"])


def test_load_node():
    """
    Test that the 'Load' node correctly stored the SDTL
    """

    converter = ConverterV1("./load.json")
    converter.convert_sdtl_to_rdf()

    # Create a query that retrieves the Program level metadata
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT DISTINCT ?program_id ?load_command
            ?load_filename ?software ?is_compressed
    WHERE {
        ?program_id rdf:type sdtl:Program .
        ?program_id sdtl:Command ?load_command .
        ?program_id sdtl:FileName ?load_filename.
        ?program_id sdtl:Software ?software .
        ?program_id sdtl:IsCompressed ?is_compressed .
    }
    """

    res = converter.graph.query(query)
    with open("./load.json") as json_file:
        sdtl = json.load(json_file)
        load_command = sdtl["Commands"][0]
        # Test that the values are present and expected
        for row in res:
            # The order comes from the SELECT order
            assert row[0] == rdflib.URIRef("#Load/1")
            assert row[1] == rdflib.Literal(load_command["Command"])
            assert row[2] == rdflib.Literal(load_command["FileName"])
            assert row[3] == rdflib.Literal(load_command["Software"])
            assert row[4] == rdflib.Literal(load_command["IsCompressed"])

    # Create a query to check that there's a node holding the only SourceInformation node
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT DISTINCT ?source_info_id
    WHERE {
    ?program_id sdtl:Commands ?sequence_id.
    ?sequence rdf:type rdf:Seq.
    }
    """
    res = converter.graph.query(query)
    for row in res:
        assert row[0] == rdflib.URIRef("CommandInventory/1")

    # Check that the ID of the Load command is correct
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT DISTINCT ?source_info_id
    WHERE {
    ?program sdtl:Commands ?command_inventory.
    ?command_inventory rdf:type rdf:Seq.
    ?command_inventory rdf:_1 ?source_info_id.
    }
    """
    res = converter.graph.query(query)
    for row in res:
        assert row[0] == rdflib.URIRef("#Load/1")

# Check that the contents of the Load command are correct
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT DISTINCT ?load_command ?command ?filename ?software ?is_compressed
    WHERE {
    ?load_command rdf:type sdtl:Load.
    ?load_command sdtl:Command ?command.
    ?load_command sdtl:FileName ?filename.
    ?load_command sdtl:Software ?software.
    ?load_command sdtl:IsCompressed ?is_compressed.
    }
    """
    res = converter.graph.query(query)
    with open("./load.json") as json_file:
        sdtl = json.load(json_file)
        load_command = sdtl["Commands"][0]
        for row in res:
            assert row[0] == rdflib.URIRef("#Load/1")
            assert row[1] == rdflib.Literal(load_command["Command"])
            assert row[2] == rdflib.Literal(load_command["FileName"])
            assert row[3] == rdflib.Literal(load_command["Software"])
            assert row[4] == rdflib.Literal(load_command["IsCompressed"])
