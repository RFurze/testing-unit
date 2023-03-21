import src.functions as fc
import pytest

"""
Function name: dice_simulator():
Number of sides: 250
Is it fair: True

Return
    - type: int
    - min: 1
    - max: 250
    - distribution: 
        1/250: 1
        1/250: 2
        ... 0.004
    
"""


@pytest.fixture
def N():
    return 10_000_000


@pytest.fixture
def faces(N):
    faces = [fc.dice_simulator() for _ in range(N)]
    return faces


@pytest.fixture
def probabilities(N, faces):
    p = [faces.count(i + 1) / N for i in range(250)]
    return p


def test_type():
    assert isinstance(fc.dice_simulator(), int)


def test_min(faces):
    assert min(faces) == 1


def test_max(faces):
    assert max(faces) == 250


def test_dist(probabilities):
    for r in range(1, 251):
        for p in probabilities:
            assert p - r / 250 < 0.0001
            # assert pytest.approx(p,abs=1e-2) == r/250
