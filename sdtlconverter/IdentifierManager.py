from typing import List
import rdflib

from sdtlconverter.schemas.generated.sdtl import all_classes


"""
Class that handles the generation and management of identifiers for RDF subjects. 
"""


class IdentifierManager:
    def __init__(self):
        self.counts = 0
        misc_terms: List[str] = ["bag"]

        # Create the ProvONE and SDTL namespaces.
        self.provone_ns = rdflib.Namespace("http://purl.dataone.org/provone/2015/01/15/ontology#")
        self.prov_ns = rdflib.Namespace('http://www.w3.org/ns/prov#')
        self.schema_ns = rdflib.Namespace('http://www.schema.org/#')
        self.sdtl_namespace: rdflib.Namespace = rdflib.Namespace('https://rdf-vocabulary.ddialliance.org/sdtl#')

        # Create a map of sdtl types to count
        sdtl_schema: dict = {i: 0 for i in all_classes}

        # The schema is CamelCaps, but SDTL JSON is subCaps, so convert
        # the keys to lowerUpper, which amounts to lowercasing the first letter
        self.counts = {}
        for key, value in sdtl_schema.items():
            lowercase_key = key[0].lower() + key[1:]
            self.counts[lowercase_key] = value
        for misc_term in misc_terms:
            self.counts[misc_term] = 0

    def get_id(self, property_name: str) -> rdflib.URIRef:
        """
         Returns an identifier that follows the recommended convention class/count.
         Note that classes in RDF are CamelCase while classes in JSON
         follow thisConvention.  property_name might also be camelCase so uppercase
         the first letter...

         :param property_name: The name of the property (usually an SDTL class)
         :return: A compliant URI
         """
        property_lowered = property_name[0].lower() + property_name[1:]
        capitalzed_name = self.to_upper(property_lowered)
        if property_name in self.counts:
            self.counts[property_name] += 1
            return rdflib.URIRef('{}{}/{}'.format('#', capitalzed_name, str(self.counts[property_name])))
        elif property_lowered in self.counts:
            self.counts[property_lowered] += 1
            return rdflib.URIRef('{}{}/{}'.format('#', capitalzed_name, str(self.counts[property_lowered])))
        else:
            self.counts[property_lowered] = 1
            return rdflib.URIRef('{}{}/{}'.format('#', capitalzed_name, str(self.counts[property_lowered])))

    def get_property_id(self, sdtl_property) -> rdflib.URIRef:
        """
        Returns of the form: sdtl#sdtl_property

        Properties shouldn't have any sort of count associated with them (which is what get_id does).
        This method returns a namespaced sdtl property.
        :param sdtl_property:
        :return:
        """
        return rdflib.URIRef(f'{self.sdtl_namespace}{self.to_upper(sdtl_property)}')

    @staticmethod
    def to_lower(term):
        return term[0].lower() + term[1:]

    @staticmethod
    def to_upper(term):
        return term[0].upper() + term[1:]
