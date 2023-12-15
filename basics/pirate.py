from __future__ import annotations
from enum import Enum

Drink = Enum("Drink", ["RUM", "BEER", "WATER"])


class DrinkException(ValueError):
    pass


class Pirate:
    def __init__(self, happiness: int, sailing_skill: int) -> None:
        self.happiness = happiness
        self.sailing_skill = sailing_skill

    @staticmethod
    def create() -> Pirate:
        return Pirate(
            happiness=0,
            sailing_skill=0,
        )

    def train_sailing(self) -> None:
        self.sailing_skill += 1

    def drink(self, d: Drink) -> None:
        print("Down the hatch!")
        match d:
            case Drink.WATER:
                raise DrinkException("a pirate cannot drink water")
            case Drink.RUM:
                self.happiness += 10
            case Drink.BEER:
                self.happiness += 1
