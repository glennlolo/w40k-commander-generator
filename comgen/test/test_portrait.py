import pprint
import logging
import pytest

from comgen.portrait import Portrait
from comgen.enums import Race, Rank, Sex, Subtype

@pytest.fixture
def params():
    return {
        "race": Race.astra.title,
        "sex": Sex.male.title,
        "subtype": Subtype.cadian.title,
        "rank": Rank.lieutenant.title,
    }

def testGenerateCadianMalePortrait(params):
    portrait = Portrait(params)