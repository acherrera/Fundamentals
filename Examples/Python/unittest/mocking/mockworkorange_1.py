"""
Showing how to use mocking for teting
"""

import os

def work_on():
    """ Simple function to work with """
    path = os.getcwd()
    print(f'Working on {path}')
    return path


work_on()
