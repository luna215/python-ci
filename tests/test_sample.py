import pytest


@pytest.fixture
def simple_fixture():
    print("hi")


def test_sample_function(simple_fixture):
    assert True


class Paul:
    pass


class Karen:
    pass


class Paco:
    pass


class Jennifer:
    pass


class Mom:
    pass
