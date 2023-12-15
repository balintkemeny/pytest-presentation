import pytest

from basics.pirate import Pirate, Drink, DrinkException


def test__train_sailing__increases_sailing_skill_by_one():
    sut = Pirate.create()

    sut.train_sailing()

    assert sut.sailing_skill == 1


def test__drink__increases_happiness_by_ten_when_given_rum():
    sut = Pirate.create()

    sut.drink(Drink.RUM)

    expected_happiness = 10
    if sut.happiness != expected_happiness:
        pytest.fail(f"Expected happiness to be {expected_happiness}, got {sut.happiness}")


def test__drink__raises_exception_when_given_water():
    sut = Pirate.create()

    with pytest.raises(DrinkException):
        sut.drink(Drink.WATER)


def test__drink__prints_down_the_hatch_to_stdout(capsys):
    sut = Pirate.create()

    sut.drink(Drink.BEER)

    captured_output = capsys.readouterr().out.rstrip()
    assert captured_output == "Down the hatch!"
