import src.functions as fc
from random import randint


def test_two():
    assert fc.inc(2) == 3


def test_type():
    assert isinstance(fc.inc(2), int), "The result should be an integer"


def test_negative():
    assert fc.inc(-1) == 0, "The result should be 0"


def test_three():
    assert fc.inc(3) == 4, "The result should be 4"


def test_large():
    for i in range(1_000):
        item = randint(-100_000, 100_000)
        assert item + 1 == fc.inc(item)


def test_string():
    assert fc.inc("3") == "Please use an integer or float input"
