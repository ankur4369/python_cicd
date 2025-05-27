from hello import add, sub

def setup():
    print("Setting up the tests")

def teardown():
    print("tearing down the tests")

def test_add():
    assert add(3, 5) == 8, "Test case 1 failed"
    assert add(4, 5) == 9, "Test case 2 failed"

print(__name__)
if __name__ == "__main__":
    test_add()