import json
import pandas as pd    

class Adapter:
    """
        The Adapter is responsible for serialization and deserialization of the Transport Network Model (TNM) defined in RFC0020.
        It follows the following interface:
            from_json(JSON model)
            to_json(**table_kwargs)
        All Microservices following TNM must have an Adapter implementing this interface.
    """

    def __init__(self, tnm_model):
        """
            The Adapter constructor. Currently not in use.
        """
        self.tnm = tnm_model

    def from_json(self, options=None):
        """
            Converts the TNM to some internal representation.
            In this Creator service, it converts some options (defined in RFC0020) from JSON to a python dictionary.
        """
        if options == None:
            options = {}
        
        df = pd.json_normalize(self.tnm)
        return df

    def to_json(self, **table_kwargs):
        pass


