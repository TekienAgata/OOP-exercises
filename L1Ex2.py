class Sponge:
    def __init__(self, hydration: int = 100):
        self.hydration = hydration

    def wring(self):
        self.hydration -= 20
        if self.hydration < 10:
            self.hydration = 10

    def wet(self):
        self.hydration = 100

    def touch(self):
        print(self.hydration)
