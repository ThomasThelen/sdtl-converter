from src.converters.ConverterV1 import ConverterV1


# Demonstrates how the compute command is handled
converter = ConverterV1('../tests/scripts/single_command/sdtl.json')
converter.construct_provenance()
# Print the RDF
print(str(converter))

print('##########################################')
print('##########################################\n\n')

# Construct retrospective + prospective
converter = ConverterV1('../tests/scripts/single_command/sdtl.json')
converter.construct_provenance(retrospective=True)

# Print the RDF
print(str(converter))
