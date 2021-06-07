from colors import fcolors, bcolors
from random import randint


class ResourceStyle:
    wood = f"{fcolors.CYAN}Wood{fcolors.RESET}"
    brick = f"{fcolors.RED}Brick{fcolors.RESET}"
    steel = f"{fcolors.MAGENTA}Steel{fcolors.RESET}"
    fuel = f"{fcolors.GREEN}Fuel{fcolors.RESET}"


class Game:
    def __init__(self, indiv_rounds, numPlayers, players, health=1000):
        self.indiv_rounds = indiv_rounds
        self.numPlayers = numPlayers
        self.turn = 0
        _players = players.copy()
        for i in range(len(_players)):
            r = randint(0, len(_players) - 1)
            _players[i], _players[r] = _players[r], _players[i]
        self.players = [Player(_players[uid], uid, health) for uid in range(numPlayers)]

    def getInput(self, prompt, cast, condition, errorMessage):
        while True:
            try:
                response = cast(input(prompt))
                assert condition(response)
                return response
            except:
                print(errorMessage)

    def play(self):
        rs = ResourceStyle
        for round in range(self.indiv_rounds * self.numPlayers):
            # Print round header
            print(f"\n{bcolors.YELLOW}{fcolors.BLACK}----ROUND {round + 1}----{fcolors.RESET}\n")
            # Print all player details
            for i in self.players:
                i.increaseGDP()
                i.printResources(round % self.numPlayers)
            # Player choices
            currentPlayer = self.players[round % self.numPlayers]
            # currentPlayer.printResources()
            print(f"\nPlayer {round % self.numPlayers} ({currentPlayer.name}) move - Choices:")

            choices = [
                (f"Get 50 units {rs.wood} from the forest - reverse power rule", 0),
                (f"Get 50 units {rs.brick} from the mines - u-substitution", 1),
                (f"Get 50 units {rs.steel} from the factory - parts", 2),
                (f"Get 50 units {rs.fuel} from the fuel rig - partial fractions", 3)
            ]
            # Check if can purchase weapon
            if currentPlayer.steel >= 100:
                choices.append(
                    (f"Purchase ion cannon for 100 units {rs.steel} (current: {currentPlayer.steel} units)", 4))
            if currentPlayer.steel >= 200:
                choices.append(
                    (f"Purchase forcefield for 200 units {rs.steel} (current: {currentPlayer.steel} units)", 5))
            if currentPlayer.steel >= 2000:
                choices.append(
                    (f"Purchase death star for 2000 units {rs.steel} (current: {currentPlayer.steel} units)", 6))
            # Check if can use existing Weapon
            if len(currentPlayer.ionCannon) > 0 and currentPlayer.fuel >= 25:
                choices.append((f"Use ion cannon for 25 units {rs.fuel}", 7))
            if len(currentPlayer.deathstar) > 0:
                choices.append((f"Use death star", 8))
            # Check if can upgrade govt building
            if currentPlayer.govt_stage == 1 and currentPlayer.brick >= 250:
                choices.append((
                               f"Upgrade government building to Stage II for 250 units {rs.brick} (current: {currentPlayer.brick} units)",
                               9))
            if currentPlayer.govt_stage == 2 and currentPlayer.brick >= 500:
                choices.append((
                               f"Upgrade government building to Stage III for 500 units {rs.steel} (current: {currentPlayer.steel} units)",
                               10))
            # Print all info to user
            # choices.append(("Print all player info", 11))
            choices.append(("Quit", 12))

            # Give all choices to the player
            choiceNums = {c[1] for c in choices}
            for choice in choices:
                print(f"{choice[1] + 1}. {choice[0]}")

            while True:
                print()
                # Get player move
                playerChoice = self.getInput(
                    prompt=">>> Enter number choice: ",
                    cast=lambda x: int(x) - 1,
                    condition=lambda x: x in choiceNums,
                    errorMessage="Invalid input; enter a valid number associated with the given choices."
                )
                # Evaluate player choice
                if playerChoice == 0:  # Get wood
                    print("This will be where a problem is asked")
                    print(f"Successfully acquired 50 units {rs.wood}")
                    currentPlayer.wood += 50
                elif playerChoice == 1:  # Get brick
                    print("This will be where a problem is asked")
                    print(f"Successfully acquired 50 units {rs.brick}")
                    currentPlayer.brick += 50
                elif playerChoice == 2:  # Get steel
                    print("This will be where a problem is asked")
                    print(f"Successfully acquired 50 units {rs.steel}")
                    currentPlayer.steel += 50
                elif playerChoice == 3:  # Get fuel
                    print("This will be where a problem is asked")
                    print(f"Successfully acquired 50 units {rs.fuel}")
                    currentPlayer.fuel += 50

                elif playerChoice == 4:  # Purchase ion cannon
                    print("Purchased 1 Ion Cannon (3 uses, 25 fuel required per use)")
                    currentPlayer.steel -= 100
                    currentPlayer.ionCannon.append(Weapon("Ion Cannon", 25, 3))
                    print(f"{fcolors.RED}-100{fcolors.RESET} units {rs.steel} (new amount: {currentPlayer.steel} units)")
                elif playerChoice == 5:  # Purchase forcefield
                    print("Purchased 1 Forcefield (3 uses, 50 fuel required per use)")
                    currentPlayer.steel -= 200
                    currentPlayer.ionCannon.append(Weapon("Forcefield", 50, 3))
                    print(f"{fcolors.RED}-200{fcolors.RESET} units {rs.steel} (new amount: {currentPlayer.steel} units)")
                elif playerChoice == 6:  # Purchase death star
                    print("Purchased 1 Death Star (1 use)")
                    currentPlayer.steel -= 2000
                    currentPlayer.ionCannon.append(Weapon("Death Star", 0, 1))
                    print(f"{fcolors.RED}-2000{fcolors.RESET} units {rs.steel} (new amount: {currentPlayer.steel} units)")
                elif playerChoice == 7:  # Use ion cannon
                    print("Functionality not built yet")
                elif playerChoice == 8:  # Use death star
                    print("Functionality not built yet")

                elif playerChoice == 9:  # Upgrade govt building to Stage II
                    currentPlayer.govt_stage += 1
                    print(f"Upgraded Player {currentPlayer.uid} ({currentPlayer.name}) government building to Stage II")
                    currentPlayer.brick -= 250
                    print(f"{fcolors.RED}-250{fcolors.RESET} units {rs.brick} (new amount: {currentPlayer.brick} units)")
                elif playerChoice == 10:  # Upgrade govt building to Stage III
                    print("Functionality not built yet")
                    currentPlayer.govt_stage += 1
                    print(f"Upgraded Player {currentPlayer.uid} ({currentPlayer.name}) government building to Stage III")
                    currentPlayer.steel -= 500
                    print(f"{fcolors.RED}-250{fcolors.RESET} units {rs.steel} (new amount: {currentPlayer.steel} units)")

                elif playerChoice == 12:
                    return

                break


class Player:
    def __init__(self, name, uid, govt_health):
        self.name = name
        self.uid = uid
        self.wood = self.brick = self.steel = self.fuel = 0
        self.ionCannon = []
        self.forcefield = []
        self.deathstar = []
        self.govt_health = govt_health
        self.govt_stage = 1
        self.gdp = 0
        self.gdp_levels = {1:25, 2:50, 3:100}

    def useWeapon(weapon, target):
        if weapon == "Ion Cannon":
            pass
        elif weapon == "Forcefield":
            pass
        elif weapon == "Death Star":
            pass

    def increaseGDP(self):
        self.gdp += self.gdp_levels[self.govt_stage]

    def printResources(self, c_uid):
        rs = ResourceStyle
        print(f"{bcolors.YELLOW if c_uid == self.uid else ''}Player {self.uid} ({self.name}){bcolors.RESET if c_uid == self.uid else ''} - Stage {'I' if self.govt_stage == 1 else 'II' if self.govt_stage == 2 else 'III'} Government Building - GDP: ${self.gdp}")
        print(f" • {rs.wood}:\t{self.wood} units")
        print(f" • {rs.brick}:\t{self.brick} units")
        print(f" • {rs.steel}:\t{self.steel} units")
        print(f" • {rs.fuel}:\t{self.fuel} units")
        if len(self.ionCannon) > 0:
            print(" • Ion Cannons:", end=" ")
            print(*self.ionCannon, sep=", ")
        if len(self.forcefield) > 0:
            print(" • Forcefields:", end=" ")
            print(*self.forcefield, sep=", ")
        if len(self.deathstar) > 0:
            print(" • Death Stars:", end=" ")
            print(*self.deathstar, sep=", ")


class Weapon:
    def __init__(self, label, fuelNeeded, numberOfUses):
        self.label = label
        self.fuelNeeded = fuelNeeded
        self.numberOfUses = numberOfUses

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.label} ({self.numberOfUses}x)"


# p = Player(0)
# p.wood = 25
# p.brick = 50
# p.steel = 75
# p.fuel = 100
# p.printResources()
game = Game(indiv_rounds=10, numPlayers=2, players=["Pranav", "Michael"])
game.play()