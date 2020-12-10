from src.converters.ConverterV1 import ConverterV1
# Demonstrates how the Load command is handled

converter = ConverterV1('./sdtl.json')

# Construct the prospective provenance

converter.convert_sdtl_to_rdf()
# Print the RDF
print(str(converter))
converter.write_jsonld()
converter.write_turtle()