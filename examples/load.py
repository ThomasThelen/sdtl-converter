from src.converters.ConverterV1 import ConverterV1
# Demonstrates how the Load command is handled

converter = ConverterV1('../tests/scripts/load_file/sdtl.json')

# Construct the prospective provenance

converter.construct_provenance()

# Print the RDF
print(str(converter))

print('##########################################')
print('##########################################\n\n')

converter = ConverterV1('../tests/scripts/load_file/sdtl.json')
# Construct retrospective + prospective
converter.construct_provenance(retrospective=True)

# Print the RDF
print(str(converter))