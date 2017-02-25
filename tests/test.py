import sys
from nose.tools import *
from solve_led.main import *

def test_main():
	eq_(main(), "hello")

def test_version():
	eq_(sys.version_info[0], 3, "Python is not in version 3")