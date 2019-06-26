import pytest

import cuppak
from cuppak import *
from cuppak.component import *
from cuppak.window import *
from cuppak.dto import *

def pytest_report_header(config):
    return 'blarg'

class Abd(object):
    def return_zero(self):
        return 0

##def test_a2(abd):
##    assert 0 == abd.return_zero()

@pytest.fixture(scope='session')
def abd():
    return Abd()