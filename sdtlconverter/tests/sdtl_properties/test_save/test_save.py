from sdtlconverter.ConverterV03 import ConverterV03
import rdflib


def test_save_command():
    """
    Test that the save command is being properly represented
    """

    converter = ConverterV03("./sdtl_properties/test_save/sdtl.json")
    converter.convert_sdtl_to_rdf()
    converter.write_turtle()
    converter.write_jsonld()

    # Check that sdtl:Program node exists and is properly named
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT ?save_id ?file_format ?filename
    WHERE {
        ?save_id rdf:type sdtl:Save .
        ?save_id sdtl:fileFormat ?file_format .
        ?save_id sdtl:fileName ?filename
    }
    """

    res = converter.graph.query(query)
    assert len(res) > 0
    save_ids = []
    file_formats = []
    filenames = []
    for row in res:
        save_ids.append(row[0])
        file_formats.append(row[1])
        filenames.append(row[2])

    assert len(save_ids) == 3
    assert len(file_formats) == 3
    assert len(filenames) == 3

    for i in range(1, 3):
        assert rdflib.URIRef(f"#Save/{i}") in save_ids

    for file_format in file_formats:
        assert str(file_format) in ["csv", "xlsx", "dta"]

    for filename in filenames:
        assert str(filename) in ["data.xlsx", "data.csv", "data.dta"]
