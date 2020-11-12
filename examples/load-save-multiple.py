from src.converters.test_converter import ConverterV1
# Demonstrates how the Load command is handled

converter = ConverterV1('../tests/scripts/load-save-multiple/sdtl.json')

# Construct the prospective provenance

converter.parse()

# Print the RDF
print(str(converter))
