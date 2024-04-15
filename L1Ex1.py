import random


class Coin:
    def __init__(self, denomination: int):
        self.denomination = denomination
        self.side = "heads"

    def __str__(self):
        return f"Coin's side: {self.side}, coin's denomination: {self.denomination}"

    def throw(self):
        self.side = random.choice(["heads", "tails"])


def coin_game():
    coin1 = Coin(1)
    coin2 = Coin(2)
    coin3 = Coin(5)
    amount = 0
    while amount < 20:
        coin1.throw()
        coin2.throw()
        coin3.throw()
        if coin1.side == "heads":
            amount += coin1.denomination
        if coin2.side == "heads":
            amount += coin2.denomination
        if coin3.side == "heads":
            amount += coin3.denomination
    if amount == 20:
        print("Congratulations! :)")
        return True
    print("Boohoo! :(")
    return False


if __name__ == "__main__":
    result = 0
    for _ in range(100):
        if coin_game() is True:
            result += 1
    print(f"Wins: {result}, losses: {100-result}")
