# SDTLConverter
[![Build Status](https://travis-ci.org/ThomasThelen/sdtl-converter.svg?branch=master)](https://travis-ci.org/ThomasThelen/sdtl-converter)
[![codecov](https://codecov.io/gh/ThomasThelen/sdtl-converter/branch/master/graph/badge.svg?token=FHBM1I1R5H)](undefined)

A python library for turning SDTL in JSON-LD format into ProvONE/Prov.




### Try it Out

Install with pip
 
 `pip install git+https://github.com/ThomasThelen/sdtl-converter.git`
 
 To import the library in a sorce file,  
 
 `from sdt-converter import Converter`


TCreate an instance of `Converter`, passing the location of an SDTL JSON
file to its constructor, shown below.
 
`converter = Converter('path_to/sdtl.json')`

#### Constructing Provenance

The `construct_provenance` method is the main method used to create
proveance representations of the SDTL. To create prospective provenance,
use the following

`converter.construct_provenance()`

or

`converter.construct_provenance(prospective=True)`




