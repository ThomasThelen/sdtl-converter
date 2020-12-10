# SDTLConverter
[![Build Status](https://travis-ci.org/ThomasThelen/sdtl-converter.svg?branch=master)](https://travis-ci.org/ThomasThelen/sdtl-converter)
[![codecov](https://codecov.io/gh/ThomasThelen/sdtl-converter/branch/master/graph/badge.svg?token=FHBM1I1R5H)](undefined)

A python library for turning SDTL in JSON-LD format into ProvONE/Prov.

### Features


### Installing

This isn't on PyPI, so use pip to install from this repository. 
 
`python3 -m pip install 
git+https://github.com/ThomasThelen/sdtl-converter.git`
 

### Using


#### Converting SDTL to RDF

Turn turn an SDTL JSON file into RDF, start by constructing a
`ConverterV1` class, passing the path to the sdtl into the constructor.
 
```
converter = ConverterV1('path_to/sdtl.json')
```

Next, call `convert_sdtl_to_rdf` to perform the conversion. Either print
the ConverterV1 object or write the output to disk.
```
converter.convert_sdtl_to_rdf()
print(str(converter))
converter.write_jsonld()
converter.write_turtle()
```


### Examples

Examples that use this library can be found in the
[examples](https://github.com/ThomasThelen/sdtl-rdf-examples)
repository.
