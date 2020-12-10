from src.converters.ConverterV1 import ConverterV1
# Demonstrates how the Load command is handled

converter = ConverterV1('./rename.json')

# Construct the prospective provenance

converter.parse()

# Print the RDF
print(str(converter))
