from sdtlconverter.ConverterV03 import ConverterV03
import rdflib


def test_identifiers():
    """
    Test that the proper number of MergeDatasets nodes exist and that they have
    the expected identifiers
    :return: None
    """

    converter = ConverterV03("./sdtl_properties/test_merge/sdtl.json")
    converter.convert_sdtl_to_rdf()
    converter.write_turtle()
    converter.write_jsonld()

    # Get the identifiers of all of the MergeDatasets identifiers
    query = """
        PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
                SELECT ?merge_datasets_id
        WHERE {
            ?merge_datasets_id rdf:type sdtl:MergeDatasets .
        }
        """
    res = converter.graph.query(query)
    assert len(res) > 0
    merged_dataset_ids = []
    for row in res:
        merged_dataset_ids.append(row[0])

    # Make sure that the correct 11 MergeDatasets nodes are present
    for i in range(1, 11):
        assert rdflib.URIRef(f"#MergeDatasets/{i}") in merged_dataset_ids
