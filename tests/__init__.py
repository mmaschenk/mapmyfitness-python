import unittest

from mapmyfitness import MapMyFitness


class MapMyFitnessTestCase(unittest.TestCase):
    def setUp(self):
        self.mmf_api = MapMyFitness(api_key='abc123', access_token='super-secret-token')