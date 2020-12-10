# SDTLConverter
[![Build Status](https://travis-ci.org/ThomasThelen/sdtl-converter.svg?branch=master)](https://travis-ci.org/ThomasThelen/sdtl-converter)
[![codecov](https://codecov.io/gh/ThomasThelen/sdtl-converter/branch/master/graph/badge.svg?token=FHBM1I1R5H)](undefined)

A python library for turning SDTL in JSON-LD format into ProvONE/Prov.

### Features


### Installing

This isn't on PyPI, so use pip to install from this repository. 
 
`pip3 install git+https://github.com/ThomasThelen/sdtl-converter.git`
 

### Using

#### Loading SDTL
 
 To parse a single file, create a converter object and pass the path to
 the constructor.
 
 `converter = ConverterV1('path_to/sdtl.json')`


To parse more than one SDTL document together, pass them in as a list

```
from typing import List
paths: List = ['path_to/first/sdtl.json', 'path_to/second/sdtl.json'] 
converter = ConverterV1(paths)
```

#### Converting SDTL to RDF

Turn turn an SDTL JSON file into RDF, start by loading the file
 
```
converter = ConverterV1('path_to/sdtl.json')
```

Next, call `convert_sdtl_to_rdf` to perform the conversion. Either print
the ConverterV1 object or write to disk for the output.
```
converter.convert_sdtl_to_rdf()
print(str(converter))
converter.write_jsonld()
converter.write_turtle()

```

See `tests/to_sdtl` for examples.

#### Generating Provenance



### Unit Tests

The unit tests should be run with pytest. Navigate to the root directory
and run

`pytest`

### Examples
To run the examples, clone this repository and run the example files as
as a normal python scripts.
