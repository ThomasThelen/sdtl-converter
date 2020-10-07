# SDTLConverter
[![Build Status](https://travis-ci.org/ThomasThelen/sdtl-converter.svg?branch=master)](https://travis-ci.org/ThomasThelen/sdtl-converter)
[![codecov](https://codecov.io/gh/ThomasThelen/sdtl-converter/branch/master/graph/badge.svg?token=FHBM1I1R5H)](undefined)

A python library for turning SDTL in JSON-LD format into ProvONE/Prov.




### Try it Out

Install with pip
 
`pip install git+https://github.com/ThomasThelen/sdtl-converter.git`
 
 To import the library in a sorce file,  
 
`from sdt-converter import Converter`

#### Loading SDTL
 
 The path to the SDTL file is passed to the Converter constructors.
 
 For example, to load and parse SDTL 1.0,
  
`converter = ConverterV1('path_to/sdtl.json')`


#### Constructing Provenance

The `construct_provenance` method is the main method used to create
ProvONE representations of the SDTL. To create prospective provenance,
call `construct_provenance`.

`converter.construct_provenance()`

or

`converter.construct_provenance(prospective=True)`
