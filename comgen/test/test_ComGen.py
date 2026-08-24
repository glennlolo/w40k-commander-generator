import logging
from unittest import TestCase
from unittest.mock import patch

from comgen.comgen import ComGen
from comgen.enums import Race, Rank, Sex, Subtype

class TestGetCommanderParams(TestCase):

    def setUp(self):
        self.options = {
            "race": Race.astra.title,
            "sex": "",
            "subtype": "",
            "rank": "",
            "batch": 1,
            "export": "json",
            "mode": "full",
            "debug": False
        }

    def testGetRandomCommanderParams(self):
        comgen = ComGen(self.options)
        params = comgen.getCommandersParams(self.options)
        # Check param types and length
        self.assertIsInstance(params, list)
        self.assertEqual(len(params), 1)
        self.assertIsInstance(params[0], dict)
        self.assertIsInstance(params[0]["race"], Race)
        self.assertIsInstance(params[0]["sex"], Sex)
        self.assertIsInstance(params[0]["subtype"], Subtype)
        self.assertIsInstance(params[0]["rank"], Rank)
        # Check forced value
        self.assertEqual(params[0]["race"].title, self.options["race"])
        # Check if params are compatible
        self.assertEqual(params[0]["subtype"].race, params[0]["race"].title)
        self.assertIn(params[0]["race"].title, params[0]["rank"].race)

    def testGetSpecificCommanderParams(self):
        self.options["sex"] = Sex.male.title
        self.options["subtype"] = Subtype.mordian.title
        self.options["rank"] = Rank.general.title

        comgen = ComGen(self.options)
        params = comgen.getCommandersParams(self.options)
        # Check values
        self.assertEqual(params[0]["sex"].title, self.options["sex"])
        self.assertEqual(params[0]["subtype"].title, self.options["subtype"])
        self.assertEqual(params[0]["rank"].title, self.options["rank"])

    def testGetIncompatibleCommanderParams(self):
        self.options["subtype"] = Subtype.mordian.title
        self.options["rank"] = Rank.chaplain.title

        with self.assertRaises(AssertionError):
            ComGen(self.options)

    def testBatchGeneration(self):
        self.options["batch"] = 5
        comgen = ComGen(self.options)
        params = comgen.getCommandersParams(self.options)
        # Check batch size and types
        self.assertIsInstance(params, list)
        self.assertEqual(len(params), 5)
        # Check parameter values
        self.assertTrue(all(isinstance(param, dict) for param in params))
        self.assertTrue(all(param["race"].title == self.options["race"] for param in params))
        self.assertTrue(all(param["subtype"].race == param["race"].title for param in params))
        self.assertTrue(all(param["race"].title in param["rank"].race for param in params))

    def testDebugLogging(self):
        self.options["debug"] = True
        # Check if debug messages are logged
        logger = logging.getLogger('comgen.comgen')
        with patch.object(logger, 'info') as mock_info, patch.object(logger, 'debug') as mock_debug:
            comgen = ComGen(self.options)
            params = comgen.getCommandersParams(self.options)
            mock_info.assert_called_with("Generating 1 commanders with the following options: %s", self.options)
            mock_debug.assert_called_with("Commander #0 generated options: %s", params[0])