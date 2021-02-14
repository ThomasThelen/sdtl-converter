# SDTLConverter
[![Build Status](https://travis-ci.org/ThomasThelen/sdtl-converter.svg?branch=master)](https://travis-ci.org/ThomasThelen/sdtl-converter)
[![codecov](https://codecov.io/gh/ThomasThelen/sdtl-converter/branch/master/graph/badge.svg?token=FHBM1I1R5H)](undefined)

A python library for ingesting SDTL in the JSON format into rdflib,
which can then be queried or exported into a number of formats such as
JSON-LD or turtle.

### Features

- Supports SDTL v ____
- Converting individual SDTL JSON files into a graph
- Load multiple SDTL JSON files and combine into single graph

### Installing

This isn't on PyPI, so use pip to install from this repository. 
 
`python3 -m pip install 
git+https://github.com/ThomasThelen/sdtl-converter.git`
 

### Usage


#### Loading SDTL Into the Graph

Turn turn a single SDTL JSON file into RDF, start by constructing a
`ConverterV1` class and pass the path to the sdtl into the constructor.
 
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

#### Querying the Graph

In the case that you want to use rdflib to query the SDTL, refer to the
`tests/` directory for example queries to get you started. The graph can
be queried with SPARQL in the standard way using the SDTL ontology.
