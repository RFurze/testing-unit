import src.functions as fc

"""
Return
- "even"
- "odd"

Scenarios:
- Not int: return "yellow"
- 0: return "https://www.britannica.com/story/is-zero-an-even-or-an-odd-number"
- odd: 7=="odd"
- even: 2=="even"
- odd_larger = 54689813858351 == "odd"
- even_larger = 646868423121532 == "even"

- Negative odd: -7=="odd"
- Negative even: -2=="even"
- Negative odd_larger = -54689813858351 == "odd"
- Negative even_larger = -646868423121532 == "even"
"""


def test_type():
    assert fc.evenodd("a") == "yellow"
    assert fc.evenodd({1, 2, 0}) == "yellow"
    assert fc.evenodd([1, 2, 0]) == "yellow"


def test_zero():
    assert (
        fc.evenodd(0)
        == "https://www.britannica.com/story/is-zero-an-even-or-an-odd-number"
    )


def test_odd_small():
    assert fc.evenodd(7) == "odd"


def test_even_small():
    assert fc.evenodd(2) == "even"


def test_odd_large():
    assert fc.evenodd(54689813858351) == "odd"


def test_even_large():
    assert fc.evenodd(646868423121532) == "even"


def test_odd_small_neg():
    assert fc.evenodd(-7) == "odd"


def test_even_small_neg():
    assert fc.evenodd(-2) == "even"


def test_odd_large_neg():
    assert fc.evenodd(-54689813858351) == "odd"


def test_even_large_neg():
    assert fc.evenodd(-646868423121532) == "even"
