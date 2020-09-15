import pytest

@pytest.fixture
def simple_fixture():
    print('hi')

def test_sample_function(simple_fixture):
    assert True