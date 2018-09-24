"""
Purpose: Showing how to decode JSON data
"""

import pprint

import json

def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct


# Showing how to open a json files also
with open("dump_file.json", 'r') as complex_file_data:
    data = complex_file_data.read()
    numbers = json.loads(data, object_hook=decode_complex)


pprint.pprint(numbers)
