# SDTLConverter
[![Build Status](https://travis-ci.org/ThomasThelen/sdtl-converter.svg?branch=master)](https://travis-ci.org/ThomasThelen/sdtl-converter)
[![codecov](https://codecov.io/gh/ThomasThelen/sdtl-converter/branch/master/graph/badge.svg?token=FHBM1I1R5H)](undefined)

A python library for turning SDTL in JSON-LD format into ProvONE/Prov.

### Features

- Single SDTL file conversion
- Multiple SDTL file conversion
- Prospective & (Prospective and Retrospective) provenance support


### Installing

This isn't on PyPI, so use pip to install from this repository. 
 
`pip install git+https://github.com/ThomasThelen/sdtl-converter.git`
 

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

#### Generating Provenance

The `construct_provenance` method is the main method used to create
ProvONE representations of the SDTL. To create prospective provenance,
call `construct_provenance`.

`converter.construct_provenance()`

If instead you want a prospective provenance trace with an associasted
retrospective trace, set the `retrospective` flag to `True`]

`converter.construct_provenance(retrospective=True)` 

### Unit Tests

The unit tests should be run with pytest. Navigate to the root directory
and run

`pytest`

### Examples
To run the examples, clone this repository and run the example files as
as a normal python scripts.
