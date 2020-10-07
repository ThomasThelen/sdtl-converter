from typing import List
import rdflib

import schemas.generated.sdtl as sdtl


class IdentifierManager:
    def __init__(self):
        self.counts = 0

        # A list of terms in ProvONE that have identifiers. DEVNOTE: The
        # xsd of ProvONE can *hopefully* be generated from the owl file and then
        # have python classes generated (see how the sdtl is done)
        provone_terms: List[str] = ["Port", "Program", "Workflow"]

        # Create the ProvONE and SDTL namespaces.
        self.provone_ns = rdflib.Namespace("http://purl.dataone.org/provone/2015/01/15/ontology#")
        self.sdtl_namespace: rdflib.Namespace = rdflib.Namespace('sdtl#')

        # Create a map of sdtl types to count
        sdtl_schema: dict = {i: 0 for i in sdtl.all_classes}

        # The schema is CamelCaps, but SDTL is subCaps, so convert
        # the keys to lowerUpper, which amounts to lowercasing the first letter
        self.counts = {}
        for key, value in sdtl_schema.items():
            lowercase_key = key[0].lower() + key[1:]
            self.counts[lowercase_key] = value
        for provone_term in provone_terms:
            self.counts[provone_term] = 0

    def get_id(self, property_name):
        """
         Returns an identifier that follows the recommended convention
             class/count

         :param property_name: The name of the property (usually an SDTL class)
         :return: A compliant URI
         """
        if property_name in self.counts:
            self.counts[property_name] += 1
            return rdflib.URIRef('{}{}/{}'.format('#', property_name, str(self.counts[property_name])))
        else:
            return rdflib.URIRef(f'{self.sdtl_namespace}{property_name}')

    def get_property_id(self, sdtl_property) -> str:
        """
        sdtl#sdtl_property
        :param self:
        :param sdtl_property:
        :return:
        """
        return rdflib.URIRef(f'{self.sdtl_namespace}{sdtl_property}')