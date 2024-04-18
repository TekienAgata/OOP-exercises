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


class BlackJack:
    computer_result = 0
    player_result = 0
    c1, c2, p1, p2 = Dice(6), Dice(6), Dice(6), Dice(6)

    def game(self):
        if self.player_result > 21:
            return self.who_wins()
        if self.computer_result < 17:
            self.throw_computer()
        if 0 <= self.player_result:
            answer = input("Do you want to roll the dice?")
            if answer.strip().lower() in ["yes", "y"]:
                self.throw_player()
            else:
                self.player_result = (
                    -1 if self.player_result == 0 else (-1) * self.player_result
                )
        elif self.computer_result >= 17:
            return self.who_wins()
        print(
            f"Computer: {self.computer_result}, player: {0 if self.player_result == -1 else abs(self.player_result)}"
        )
        self.game()

    def throw_computer(self):
        self.c1.roll()
        self.c2.roll()
        self.computer_result += self.c1.get_value() + self.c2.get_value()

    def throw_player(self):
        self.p1.roll()
        self.p2.roll()
        self.player_result += self.p1.get_value() + self.p2.get_value()

    def who_wins(self):
        print(
            f"Computer: {self.computer_result}, player: {0 if self.player_result == -1 else abs(self.player_result)}"
        )
        if self.player_result > 21:
            return "computer wins"
        if self.player_result == self.computer_result:
            return "it's a tie"
        if self.player_result == 21 or self.computer_result == 21:
            "Blackjack!\n"
            if self.player_result == 21:
                return "player wins"
            else:
                return "computer wins"
        if self.player_result < 21 and 21 > self.computer_result > self.player_result:
            return "computer wins"
        else:
            return "player wins"
