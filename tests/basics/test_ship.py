import pytest

from basics.ship import Ship


def assert_identical(s1: Ship, s2: Ship):
    __tracebackhide__ = True
    assert s1 == s2
    if s1.name != s2.name:
        pytest.fail(f"the names do not match. {s1.name} != {s2.name}")


class TestShip():
    s1 = Ship(
        name="The Flying Dutchman", 
        speed=50,
        size= 200,
    )

    s2 = Ship(
        name="Santissima Trinidad",
        speed=50,
        size=200,
    )
    
    def test__equality__when_two_ships_differ_only_by_name(self):
        assert self.s1 == self.s2

    @pytest.mark.xfail
    def test__identity__when_two_ships_differ_only_by_name(self):
        assert_identical(self.s1, self.s2)
