from src.converters.ConverterV1 import ConverterV1

# Creates ProvONE from two SDTL files

paths = ['../tests/scripts/compute_accounts/sdtl.json', '../tests/scripts/compute_drop/sdtl.json']
converter = ConverterV1(paths)
converter.construct_provenance()

# Print the RDF
print(str(converter))

print('##########################################')
print('############## Retrospective #############')
print('##########################################\n\n')

paths = ['../tests/scripts/compute_accounts/sdtl.json', '../tests/scripts/compute_drop/sdtl.json']
converter = ConverterV1(paths)
# Construct retrospective + prospective
converter.construct_provenance(retrospective=True)

# Print the RDF
print(str(converter))