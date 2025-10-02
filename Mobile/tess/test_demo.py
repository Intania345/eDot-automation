import pytest

def setup_function(function):
    print("setup_function")

def teardown_function(function):
    print("teardown_function")

def test_demo():
    print("demo pytest")

def setup_module(module):
    print("setup_module")

def teardown_module(module):
    print("teardown_module")