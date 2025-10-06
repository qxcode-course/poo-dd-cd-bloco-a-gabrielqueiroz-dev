class Calculator:
    display: float = 0.0
    batteryMax: int = 100
    battery: int = 0

    def __init__(self, baterryMax: int) -> None:
        self.baterryMax = baterryMax

    def charge(self, amount: int) -> None:
        self.battery += amount
        if self.battery > self.baterryMax:
            self.battery = self.baterryMax

    def sum(self, a: float, b: float):
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return
        self.battery -= 1
        self.display = a + b

    def division(self, num: float, den: float):
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return
        self.battery -= 1
        if den == 0:
            print("fail: divisao por zero")
            return
        self.display = num / den

    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"

calculator = Calculator(0)
while True:
  command = input()
  args = command.split()
  print("$" + command)
  if args[0] == "end":
    break
  elif args[0] == "show":
    print(calculator)
  elif args[0] == "init":
    calculator = Calculator(int(args[1]))
  elif args[0] == "charge":
    calculator.charge(int(args[1]))
  elif args[0] == "sum":
    calculator.sum(float(args[1]), float(args[2]))
  elif args[0] == "div":
    calculator.division(float(args[1]), float(args[2]))
  else:
    print("fail: comando invalido")
