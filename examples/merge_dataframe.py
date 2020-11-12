from src.converters.converter_unique_names import ConverterV1

# Creates ProvONE from two SDTL files

converter = ConverterV1('../tests/scripts/compute_drop/sdtl.json')
converter.parse()

# Print the RDF
print(str(converter))
