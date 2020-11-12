converter = ConverterV1('../tests/scripts/merge_compute_r/sdtl.json')
converter.parse()

# Print the RDF
print(str(converter))