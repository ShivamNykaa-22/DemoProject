import pytest

def testLogin():
    print("Login Success")

def testLogoff():
    print("Logoff successful")

@pytest.mark.Sanity
def testCalculation():
    assert 2+2 == 4
