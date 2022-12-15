import pytest

def testHomepage():
    print("This is homepage")

def testverifypage():
    print("page verified")

@pytest.mark.Sanity
def testMatchValue():
    t="Homepage"
    assert t == "Homepage"
