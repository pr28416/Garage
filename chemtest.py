class PeriodicTableElement:
    def __init__(self, atomicNumber, element, symbol):
        self.atomicNumber = atomicNumber
        self.element = element
        self.symbol = symbol

    def __str__(self):
        return f"{self.atomicNumber} {self.element} {self.symbol}"

elements = []

with open("periodicTableElements.csv") as file:
    for i, line in enumerate(file):
        if i == 0: continue
        columns = line.split(",")
        elements.append(PeriodicTableElement(columns[0], columns[1], columns[2]))

for e in elements:
    print(e)