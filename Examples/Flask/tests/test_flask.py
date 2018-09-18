
from unittest import mock, TestCase
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../modules")
import main.py


class TeatFlask(TestCase):

    def test_index(self):

