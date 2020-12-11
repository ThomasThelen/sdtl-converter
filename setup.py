import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sdtlconverter",
    version="0.0.1",
    author="Thomas Thelen",
    author_email="thelen@nceas.ucsb.edu",
    description="A tool for converting SDTL into a ProvONE data model.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThomasThelen/sdtl-provone",
    packages=["sdtlconverter"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'rdflib',
        'xsdata',
    ],
)
