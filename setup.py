import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sdtlconverter",
    version="1.0",
    author="Thomas Thelen",
    author_email="thelen@nceas.ucsb.edu",
    description="A tool for converting SDTL JSON files into the SDTL graph representation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThomasThelen/sdtl-provone",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'rdflib',
        'xsdata',
        'rdflib-jsonld',
    ],
)
