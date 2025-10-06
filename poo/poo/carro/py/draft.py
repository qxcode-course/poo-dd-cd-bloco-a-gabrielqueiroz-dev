class Carro:
    passenger = 0
    km = 0
    passMax = 0
    gas = 0
    gasMax = 0

    def __init__(self, passenger: int, km: int, passMax: int, gas: int, gasMax: int):
        self.passenger = passenger
        self.km = km
        self.passMax = passMax
        self.gas = gas
        self.gasMax = gasMax

    def show(self):
        print(self)

    def enter(self):
        self.passenger += 1
        if self.passenger > self.passMax:
            print("fail: limite de pessoas atingido")
            self.passenger = self.passMax
            return

    def leave(self):
        self.passenger -= 1
        if self.passenger < 0:
            print("fail: nao ha ninguem no carro")
            self.passenger = 0

    def fuel(self, increment: int):
        self.gas += increment
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, distance: int):
        if self.passenger == 0:
            print("fail: nao ha ninguem no carro")
            return
        
        if distance >= self.gas and self.gas > 0:
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.km += self.gas
            self.gas = 0
            return
        elif self.gas <= 0:
            print("fail: tanque vazio")
            return
        
        self.gas -= distance
        self.km += distance

        if self.gas < 0:
            self.gas = 0
    
    def __str__(self):
        return f"pass: {self.passenger}, gas: {self.gas}, km: {self.km}"

carro = Carro(0, 0, 2, 0, 100)
while True:
    text = input()
    args = text.split()
    print(f"${text}")

    if args[0] == "show":
        carro.show()
    
    if args[0] == "enter":
        carro.enter()
    
    if args[0] == "leave":
        carro.leave()

    if args[0] == "drive":
        carro.drive(int(args[1]))

    if args[0] == "fuel":
        carro.fuel(int(args[1]))
    
    if args[0] == "end":
        break