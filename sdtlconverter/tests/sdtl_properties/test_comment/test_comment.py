from sdtlconverter.ConverterV1 import ConverterV1

import rdflib


def test_comment_identifiers():
    """
    Test that there are the expected number of comment nodes and that they have the expected
    identifiers.
    :return: None
    """
    converter = ConverterV1("./sdtl.json")
    converter.convert_sdtl_to_rdf()

    # Get the comment identifiers
    query = """
    PREFIX sdtl: <https://rdf-vocabulary.ddialliance.org/sdtl#>
            SELECT ?comment_id
    WHERE {
        ?comment_id rdf:type sdtl:Comment.
    }
    """

    res = converter.graph.query(query)
    assert len(res) > 0
    comment_ids = []
    for row in res:
        comment_ids.append(row[0])
    for i in range(1, 7):
        assert rdflib.URIRef(f"#Comment/{i}") in comment_ids
