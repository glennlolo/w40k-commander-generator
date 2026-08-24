import pprint
import logging
import pytest

from comgen.comgen import ComGen
from comgen.enums import Race, Rank, Sex, Subtype

@pytest.fixture
def options():
    return {
        "race": Race.astra.title,
        "sex": "",
        "subtype": "",
        "rank": "",
        "batch": 1,
        "export": "json",
        "mode": "full",
        "debug": False
    }

def testGetRandomCommanderParams(options):
    comgen = ComGen(options)
    params = comgen.getCommandersParams(options)
    # Check param types and length
    assert isinstance(params, list)
    assert len(params) == 1
    assert isinstance(params[0], dict)
    assert isinstance(params[0]["race"], Race)
    assert isinstance(params[0]["sex"], Sex)
    assert isinstance(params[0]["subtype"], Subtype)
    assert isinstance(params[0]["rank"], Rank)
    # Check forced value
    assert params[0]["race"].title == options["race"]
    # Check if params are compatible
    assert params[0]["subtype"].race == params[0]["race"].title
    assert params[0]["race"].title in params[0]["rank"].race

def testGetSpecificCommanderParams(options):
    options["sex"] = Sex.male.title
    options["subtype"] = Subtype.mordian.title
    options["rank"] = Rank.general.title

    comgen = ComGen(options)
    params = comgen.getCommandersParams(options)
    # Check values
    assert params[0]["sex"].title == options["sex"]
    assert params[0]["subtype"].title == options["subtype"]
    assert params[0]["rank"].title == options["rank"]

def testGetIncompatibleCommanderParams(options):
    options["subtype"] = Subtype.mordian.title
    options["rank"] = Rank.chaplain.title

    with pytest.raises(AssertionError):
        ComGen(options)

def testBatchGeneration(options):
    options["batch"] = 5
    comgen = ComGen(options)
    params = comgen.getCommandersParams(options)
    # Check batch size and types
    assert isinstance(params, list)
    assert len(params) == 5
    # Check parameter values
    assert all(isinstance(param, dict) for param in params)
    assert all(param["race"].title == options["race"] for param in params)
    assert all(param["subtype"].race == param["race"].title for param in params)
    assert all(param["race"].title in param["rank"].race for param in params)

def testDebugLogging(options,caplog):
    options["debug"] = True
    comgen = ComGen(options)
    caplog.clear()
    with caplog.at_level(logging.DEBUG):
        params = comgen.getCommandersParams(options)
        assert caplog.record_tuples == [("comgen.comgen", logging.INFO, "Generating 1 commanders with the following options: \n" + pprint.pformat(options)), 
                                    ("comgen.comgen", logging.DEBUG, "Commander #0 generated options: \n" + pprint.pformat(params[0]))]