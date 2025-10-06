class Animal:
    species: str
    age: int
    sound: str

    def __init__(self, species: str, sound: str) -> None:
        self.species = species
        self.age = 0
        self.sound = sound

    def makeSound(self) -> str:
        if self.age == 0:
            return "---"
        if self.age == 4:
            return "RIP"
        return self.sound
    
    def ageBy(self, increment: int) -> None:
        self.age += increment
        if (self.age >= 4):
            print(f"warning: {self.species} morreu")
            self.age = 4

    def __str__(self):
        return f"{self.species}:{self.age}:{self.sound}"
    
  
animal = Animal("", "")
while True:
    commandStr = input()
    command = commandStr.split()
    if command[0] == "end":
        print(f"${commandStr}")
        break
    if command[0] == "init":
        print(f"${commandStr}")
        animal = Animal(command[1], command[2])
    if command[0] == "show":
        print(f"${commandStr}")
        print(animal)
    if command[0] == "grow":
        print(f"${commandStr}")
        animal.ageBy(int(command[1]))
    if command[0] == "noise":
        print(f"${commandStr}")
        print(animal.makeSound())