import random


class Dice:
    def __init__(self, sides: int):
        self.__sides = sides
        self._value = None

    def roll(self):
        self._value = random.randint(1, self.__sides + 1)

    def get_sides(self):
        return self.__sides

    def get_value(self):
        return self._value

    def __str__(self):
        if self._value:
            return f"Sides = {self.__sides}, " f"value = {self._value}"
        else:
            return f"Sides = {self.__sides}, " f"value not set"
