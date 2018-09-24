"""
Purpose: Show how to serialized complex data type and save
"""

import json
import pprint


# Define and encoder for the complex type
def encode_complex(z):
    """ Example with only one encoder method """
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError("Object of type '{}' is not JSON \
                serializable".format(type_name))


class ComplexEncoder(json.JSONEncoder):
    """ Extend the default JSON class """
    def default(self, z):
        if isinstance(z, complex):
            return_dict = {
                    '__complex__' : True,
                    'real' : z.real,
                    'imag' : z.imag
                    }
            return (return_dict)
        else:
            # If not complex, let the master deal with it
            super().default(self,z)



# Turn complex object into json string
with open('dump_file.json', 'w') as f:
    json_string = json.dump(9 + 5j, f, cls=ComplexEncoder)

