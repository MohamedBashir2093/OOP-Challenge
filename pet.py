
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # default hunger level
        self.energy = 5  # default energy level
        self.happiness = 5  # default happiness level
        self.tricks = []  # list to store learned tricks

    def eat(self):
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 3)
            self.happiness += 1
        print(f"{self.name} ate and is now less hungry and happier.")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} slept and is now more energetic.")

    def play(self):
        if self.energy > 0:
            self.energy = max(0, self.energy - 2)
            self.happiness += 2
            self.hunger += 1
            print(f"{self.name} played and is happier but hungrier and a bit tired.")
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        print(f"Status of {self.name}:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}.")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")




