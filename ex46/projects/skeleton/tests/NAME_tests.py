from pytest import *
import NAME

def setup():
    print('SETUP!')

def teardown():
    print('TEARDOWN!')

def test_basic():
    print('TEST!')
