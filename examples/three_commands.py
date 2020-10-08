from src.converters.ConverterV1 import ConverterV1

# Creates ProvONE from two SDTL files

converter = ConverterV1('../tests/scripts/three_commands/sdtl.json')
converter.construct_provenance()

# Print the RDF
print(str(converter))

print('##########################################')
print('############## Retrospective #############')
print('##########################################\n\n')

converter = ConverterV1('../tests/scripts/three_commands/sdtl.json')
# Construct retrospective + prospective
converter.construct_provenance(retrospective=True)

# Print the RDF
print(str(converter))
