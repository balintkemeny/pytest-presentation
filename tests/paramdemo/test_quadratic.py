import pytest

from paramdemo.quadratic import solve_quadratic


def test__solve_quadratic__compute_both_roots__when_given_valid_coefficients__single_case_1():
    solution = solve_quadratic(1, 2, 1)
    
    assert solution == (-1, -1)


def test__solve_quadratic__compute_both_roots__when_given_valid_coefficients__single_case_2():
    solution = solve_quadratic(1, -3, 1.25)
    
    assert solution == (2.5, 0.5)


def test__solve_quadratic__compute_both_roots__when_given_valid_coefficients__no_param():
    for case in [
        {"a": 1, "b": 2,  "c": 1,    "expected": (-1, -1)},
        {"a": 1, "b": -3, "c": 1.25, "expected": (2.5, 0.5)},
    ]:
        solution = solve_quadratic(case["a"], case["b"], case["c"])
        assert solution == case["expected"]


@pytest.mark.parametrize("a,b,c,expected", [
    (1, 2, 1, (-1, -1)),
    (1, -3, 1.25, (2.5, 0.5)),
])
def test__solve_quadratic__compute_both_roots__when_given_valid_coefficients__func_param(a, b, c, expected):
    solution = solve_quadratic(a, b, c)
    assert solution == expected


@pytest.fixture(params=[
    (1, 2, 1, (-1, -1)),
    (1, -3, 1.25, (2.5, 0.5)),
])
def valid_cases(request):
    return request.param


def test__solve_quadratic__compute_both_roots__when_given_valid_coefficients__fixture_param(valid_cases):
    solution = solve_quadratic(valid_cases[0], valid_cases[1], valid_cases[2])
    assert solution == valid_cases[3]