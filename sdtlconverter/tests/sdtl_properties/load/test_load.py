from sdtlconverter.ConverterV1 import ConverterV1
import rdflib


def test_load_command():
    """
    Test that the load command is properly represented
    """

    converter = ConverterV1("./sdtl.json")
    converter.convert_sdtl_to_rdf()
    converter.write_turtle()
    converter.write_jsonld()

    # Get the sdtl:Load nodes and the load properties
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT ?load_id ?file_format ?filename
    WHERE {
        ?load_id rdf:type sdtl:Load .
        ?load_id sdtl:fileFormat ?file_format .
        ?load_id sdtl:fileName ?filename .
    }
    """

    res = converter.graph.query(query)
    assert len(res) > 0
    load_ids = []
    file_formats = []
    filenames = []
    for row in res:
        load_ids.append(row[0])
        file_formats.append(row[1])
        filenames.append(row[2])

    assert len(load_ids) == 4
    assert len(file_formats) == 4
    assert len(filenames) == 4

    for i in range(1, 3):
        assert rdflib.URIRef(f"#Load/{i}") in load_ids

    for file_format in file_formats:
        assert str(file_format) in ["csv", "xlsx", "dta", "sas7bdat"]

    for filename in filenames:
        assert str(filename) in ["data.xlsx", "data.csv", "data.dta", "data.sas7bdat"]
