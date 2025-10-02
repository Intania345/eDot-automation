import pytest

@pytest.fixture(scope="module")
def setup():
    print("setup module level fixture")
    yield
    print("teardown module level fixture")

@pytest.fixture(scope="function")
def before():
    print("setup function level fixture")
    yield
    print("teardown function level fixture")

@pytest.mark.usefixtures("setup", "before")
@pytest.mark.sanity
def test_add_customer():
    print("test_add_customer")

@pytest.mark.usefixtures("setup", "before")
@pytest.mark.regression
def test_add_customer():
    print("test_add_customer")