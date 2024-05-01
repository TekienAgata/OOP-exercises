class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 0
        self.tiredness = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if len(name) < 3:
            raise ValueError("Name too short")
        if name.isalpha() is False:
            raise ValueError("Invalid characters used")
        self._name = name

    def _passage_of_time(self):
        self.hunger += 1
        self.tiredness += 1

    @property
    def _mood(self):
        if self.hunger < 5 and self.tiredness < 5:
            return "happy"
        if self.hunger <= 10 and self.tiredness <= 10:
            return "content"
        if self.hunger <= 15 and self.tiredness <= 15:
            return "annoyed"
        if self.hunger > 15 or self.tiredness > 15:
            return "mad"

    def talk(self):
        print(f"{self.name} is {self._mood}")
        self._passage_of_time()

    def eat(self, food: int = 4):
        self.hunger -= food
        self._passage_of_time()

    def play(self, fun: int = 4):
        self.tiredness -= fun
        self._passage_of_time()

    def __str__(self):
        return f"Pet's name: {self.name}, hunger: {self.hunger}, tiredness: {self.tiredness}"


def main():
    name = input("Enter pet's name\n")
    pet = Pet(name)
    while True:
        print("\n--- Menu ---")
        print("1. Talk to pet")
        print("2. Feed pet")
        print("3. Play with pet")
        print("4. Show pet's details")
        print("5. Exit")
        choice = input("What would you like to do with your pet?\n")
        if choice == "1":
            pet.talk()
        elif choice == "2":
            food = input("How much would you like to feed your pet?\n")
            if food:
                pet.eat(int(food))
            else:
                pet.eat()
            print(f"{pet.name} ate!")
        elif choice == "3":
            fun = input("How much would you like to play with your pet?\n")
            if fun:
                pet.play(int(fun))
            else:
                pet.play()
            print(f"{pet.name} played!")
        elif choice == "4":
            print(pet)
        elif choice == "5":
            print("Dismantling your pet")
            break
        else:
            print("Invalid choice, please choose a number betwenn 1 and 5")


if __name__ == "__main__":
    main()
