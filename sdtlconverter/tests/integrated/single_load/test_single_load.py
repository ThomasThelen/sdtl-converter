from sdtlconverter.ConverterV1 import ConverterV1
import rdflib
import json


def test_program_node():
    """
    Test that the sdtl:Program node is properly represented
    """

    converter = ConverterV1("./sdtl.json")
    converter.convert_sdtl_to_rdf()
    converter.write_turtle()
    converter.write_jsonld()

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
        ?program_id sdtl:commands ?commands_inventory
    }
    """

    res = converter.graph.query(query)
    with open("./sdtl.json") as json_file:
        sdtl = json.load(json_file)
        for row in res:
            assert rdflib.URIRef("#Program/1") == row[0]
            assert rdflib.Literal(sdtl["SourceFileName"]) == row[1]
            assert rdflib.Literal(sdtl["SourceLanguage"]) == row[2]
            assert rdflib.Literal(sdtl["CommandCount"]) == row[3]
            assert rdflib.Literal(sdtl["Parser"]) == row[4]
            assert rdflib.Literal(sdtl["ParserVersion"]) == row[5]
            assert rdflib.URIRef("#CommandInventory/1") == row[6]


def test_load_properties():
    """
    Test that the 'Program' node has the correct properties.
    """

    converter = ConverterV1("./sdtl.json")
    converter.convert_sdtl_to_rdf()

    # Create a query that retrieves the Program level metadata
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT DISTINCT ?program_id ?load_command
            ?load_filename ?software ?is_compressed
    WHERE {
        ?program_id rdf:type sdtl:Program .
        ?program_id sdtl:Command ?load_command .
        ?program_id sdtl:FileName ?load_filename .
        ?program_id sdtl:Software ?software .
        ?program_id sdtl:IsCompressed ?is_compressed .
    }
    """

    res = converter.graph.query(query)
    with open("./sdtl.json") as json_file:
        sdtl = json.load(json_file)
        load_command = sdtl["commands"][0]
        # Test that the values are present and expected
        for row in res:
            # The order comes from the SELECT order
            assert rdflib.URIRef("#Load/1") == row[0]
            assert rdflib.Literal(load_command["Command"]) == row[1]
            assert rdflib.Literal(load_command["FileName"]) == row[2]
            assert rdflib.Literal(load_command["Software"]) == row[3]
            assert rdflib.Literal(load_command["IsCompressed"]) == row[4]


def test_load_sourceinformation():
    """
    Test that the SourceInformation node is correctly connected to the Load command
    and that the properties of the SourceInformation node are correct.
    """
    converter = ConverterV1("./sdtl.json")
    converter.convert_sdtl_to_rdf()

    # Create a query to check that there's a node holding the only SourceInformation
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT DISTINCT ?source_info_id
    WHERE {
    ?program_id sdtl:commands ?sequence_id.
    ?sequence rdf:type rdf:Seq.
    }
    """
    res = converter.graph.query(query)
    for row in res:
        assert rdflib.URIRef("CommandInventory/1") == row[0]


def test_load_command():
    """
    Test that the node representing the 'Load' command has expected properties.
    """
    converter = ConverterV1("./sdtl.json")
    converter.convert_sdtl_to_rdf()
    # Check that the ID of the Load command is correct
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT DISTINCT ?source_info_id
    WHERE {
    ?program sdtl:commands ?command_inventory.
    ?command_inventory rdf:type rdf:Seq.
    ?command_inventory rdf:_1 ?source_info_id.
    }
    """
    res = converter.graph.query(query)
    for row in res:
        assert rdflib.URIRef("#Load/1") == row[0]

    # Check that the properties of the node are the expected values from the SDTL
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
    with open("./sdtl.json") as json_file:
        sdtl = json.load(json_file)
        load_command = sdtl["commands"][0]
        for row in res:
            assert rdflib.URIRef("#Load/1") == row[0]
            assert rdflib.Literal(load_command["Command"]) == row[1]
            assert rdflib.Literal(load_command["FileName"]) == row[2]
            assert rdflib.Literal(load_command["Software"]) == row[3]
            assert rdflib.Literal(load_command["IsCompressed"]) == row[4]


def test_dataframe_creation():
    """
    Tests that the DataframeDescription and VariableInventory are the
    expected values.
    """
    converter = ConverterV1("./sdtl.json")
    converter.convert_sdtl_to_rdf()
    # Queries for the Load, DataframeInventory, DataframeDescription
    # and VariableInventory properties
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT DISTINCT ?load_command ?bag_id ?loaded_dataframe_id ?dataframe_name
            ?variable_inventory_id
    WHERE {
    ?load_command rdf:type sdtl:Load.
    ?load_command sdtl:ProducesDataframe ?bag_id.
    ?bag_id rdf:type rdf:Bag.
    ?bag_id rdf:_1 ?loaded_dataframe_id.
    ?loaded_dataframe_id sdtl:dataframeName ?dataframe_name.
    ?loaded_dataframe_id sdtl:VariableInventory ?variable_inventory_id.
    }
    """

    res = converter.graph.query(query)
    with open("./sdtl.json") as json_file:
        sdtl = json.load(json_file)

        for row in res:
            assert rdflib.URIRef("#Load/1") == row[0]
            assert rdflib.URIRef("#DataframeInventory/1") == row[1]
            assert rdflib.URIRef("#DataframeDescription/1") == row[2]
            assert rdflib.Literal("Active") == row[3]
            assert rdflib.URIRef("#VariableInventory/1") == row[4]


def test_dataframe_variable_inventroy():
    """
    Tests that the values of the variable inventory are correct.
    """
    converter = ConverterV1("./sdtl.json")
    converter.convert_sdtl_to_rdf()

    # Get each variable and value
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT DISTINCT ?person ?born ?died ?name ?refarea ?sex ?age
    WHERE {
    ?loaded_dataframe_i sdtl:VariableInventory ?variable_inventory_id.
    ?variable_inventory_id rdf:type rdf:Seq.
    ?variable_inventory_id  rdf:_1 ?person.
    ?variable_inventory_id  rdf:_2 ?born.
    ?variable_inventory_id  rdf:_3 ?died.
    ?variable_inventory_id  rdf:_4 ?name.
    ?variable_inventory_id  rdf:_5 ?refarea.
    ?variable_inventory_id  rdf:_6 ?sex.
    ?variable_inventory_id  rdf:_7 ?age.
    }
    """

    res = converter.graph.query(query)
    # Check that the Identifiers are correct
    for row in res:
        position = 1
        for id in row:
            assert rdflib.URIRef(f'#dataframeVariable/{position}') == id
            position +=1


def test_variable_contents():
    """
    Tests that the variables are the correct value
    """
    converter = ConverterV1("./sdtl.json")
    converter.convert_sdtl_to_rdf()

    # Add rdfs:member. From https://ontology2.com/notebooks/local/Inference_Over_RDF_Containers.html
    update_query = """
            INSERT { 
            ?p a rdfs:ContainerMembershipProperty .
        } WHERE { 
            ?s ?p ?o .
            FILTER(REGEX(STR(?p),"^http://www[.]w3[.]org/1999/02/22-rdf-syntax-ns#_[1-9]([0-9])*$"))
        }"""

    converter.graph.update(update_query)
    update_query = """
            INSERT { 
            ?container rdfs:member ?member .
        } WHERE { 
            ?container ?containerMembershipProperty ?member .
            ?containerMembershipProperty a rdfs:ContainerMembershipProperty .
        }"""
    converter.graph.update(update_query)

    # Gets all of the variables, in order
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT DISTINCT ?variable_name
    WHERE {
    
    ?dataframe_description rdf:type sdtl:DataframeDescription.
    ?dataframe_description sdtl:VariableInventory ?variable_inventory.
    ?variable_inventory rdfs:member ?variable.
    ?variable sdtl:VariableName ?variable_name.
    }
    """

    res = converter.graph.query(query)
    with open("./sdtl.json") as json_file:
        sdtl = json.load(json_file)

        expected_strings = sdtl["commands"][0]["producesDataframe"][0]["variableInventory"]
        actual = []
        for row in res:
            for value in row:
                actual.append(value)
        expected_ids = []
        for expected_var in expected_strings:
            expected_ids.append(rdflib.Literal(expected_var))
        for actual_value in actual:
            assert actual_value in expected_ids
