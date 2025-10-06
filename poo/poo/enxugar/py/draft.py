class Towel:
    color: str
    size: str
    wetness: int

    def __init__(self, color: str, size: str) -> None:
        self.color = color
        self.size = size
        self.wetness = 0

    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        elif self.size == "M":
            return 20
        elif self.size == "G":
            return 30

        return 0

    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def wringOut(self) -> None:
        self.wetness = 0

    def isDry(self) -> bool:
        return self.wetness == 0
    
    def show(self) -> None:
        print(self)

    def __str__(self) -> str:
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"

towel = Towel("", "")
while True:
    command = input()
    args = command.split()
    print(f"${command}")
    if args[0] == "end":
        break
    elif args[0] == "criar":
        towel = Towel(args[1], args[2])
    elif args[0] == "enxugar":
        towel.dry(int(args[1]))
    elif args[0] == "torcer":
        towel.wringOut()
    elif args[0] == "seca":
        print("sim" if towel.isDry() else "nao")
    elif args[0] == "mostrar":
        towel.show()
    else:
        print("fail: comando invalido")