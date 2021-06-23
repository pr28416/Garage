class Element:
    def __init__(self, *args):
        self.atomicNumber = int(args[0].strip(" "))
        self.element = args[1].strip(" ")
        self.symbol = args[2].strip(" ")
        self.atomicMass = float(args[3].strip(" "))
    def __str__(self): return f"{self.atomicNumber} {self.element} {self.symbol} ({self.atomicMass})"

table = []
with open("periodicTableElements.csv") as f:
    tmp = True
    for line in f:
        if tmp: tmp = False; continue
        table.append(Element(*line.split(",")))

numbers = {str(i) for i in range(10)}
lowercase = {i for i in 'qwertyuiopasdfghjklzxcvbnm'}
uppercase = {i.upper() for i in lowercase}

def calcMolarMass(string):
    global numbers, lowercase, uppercase, table
    parts = [""]
    i = 0

    # Part 1 - Split string into individual parts (numbers, elements, parenthesis, etc)
    while i < len(string):
        # A number is present at index i
        if string[i] in numbers:
            # Use another index j as an upper bound to capture the entire number
            j = i+1
            while j < len(string):
                if string[j] not in numbers: break
                j += 1
            # Capture the entire number
            parts.append(int(string[i:j]))
            # Add an empty string to the end - this is needed when we find and
            # add actual elements of a compound to our parts list
            parts.append("")
            # Update i
            i = j-1
        # A left parenthesis is present
        elif string[i] == "(":
            # Need to look for its respective right parenthesis
            # There may be additional parentheses - we should account for this
            j = i+1
            lvl = 1
            while j < len(string):
                if string[j] == "(": lvl += 1
                elif string[j] == ")":
                    if lvl == 1: break
                    else: lvl -= 1
                j += 1
            else: return None # Return None if there is no respective closing parenthesis - bad input
            # Add parenthesized string
            parts.append(string[i:j+1])
            parts.append("")
            # Update i
            i = j
        # A character is present
        else:
            parts[-1] += (string[i])
        i += 1

    # Part 2 - Process parts of the compound by maintaining a stack
    parts = list(reversed([i for i in parts if len(str(i)) != 0]))
    stack = [] # Stores submasses, multipliers, individual elements, or subcompounds
    mass = 0 # Represents total mass
    # We will keep removing items from parts and processing them
    while len(parts) > 0:
        # Check if we have a number
        if type(parts[-1]) == int:
            # If there is nothing in the stack, we have bad input
            if len(stack) == 0:
                return None
            # Get top mass
            try:
                e = stack.pop()
                # If we have a multiplier rather than an element
                if type(e) == int or type(e) == float:
                    # Multiplier = 1
                    if len(parts) == 0: mass += e
                    # Multiplier > 1
                    else: mass += e * parts.pop()
                else: # We have an element, so get its molar mass
                    mass += parts.pop() * list(filter(lambda x: x.symbol == e, table))[0].atomicMass
            except:
                # Bad input
                return None
        # Check if we have an element or a compound
        elif type(parts[-1]) == str:
            # Check if we have a submass in the stack that we can add
            if len(stack) > 0 and type(stack[-1]) == int:
                mass += stack.pop()
                continue
            # Add the mass of the subcompound, if found, to the stack
            if parts[-1][0] == "(":
                e = calcMolarMass(parts[-1][1:len(parts[-1])-1])
                parts.pop()
                if e is None: # Bad input
                    return None
                stack.append(e)
            else:
                # Keep removing items and adding their masses to the total mass
                while len(stack) > 0:
                    e = stack.pop()
                    try:
                        if type(parts[-1]) == str: # Topmost stack item was an element
                            mass += list(filter(lambda x: x.symbol == e, table))[0].atomicMass
                        else: # Topmost stack item was a multiplier
                            mass += parts.pop() * list(filter(lambda x: x.symbol == e, table))[0].atomicMass
                    except: # Bad input
                        return None
                i, j = 0, 1
                # Separate and add individual elements to the stack
                while i < len(parts[-1]):
                    while j < len(parts[-1]) and parts[-1][j] in lowercase: j += 1
                    stack.append(parts[-1][i:j])
                    i, j = j, j+1
                # Remove processed item from parts
                parts.pop()
        else: # Bad input
            return None

    # There may be leftover items in the stack - add them to the mass
    while len(stack) > 0:
        e = stack.pop()
        if type(e) == int or type(e) == float:
            mass += e
            continue
        mass += list(filter(lambda x: x.symbol == e, table))[0].atomicMass

    # We have final mass - return it
    return mass


if __name__ == "__main__":
#     print("Welcome to the molecular formula calculator. Please enter valid formulas. \n\tExamples: H2O, NaCl, Ba(OH)2, K2CO3\nType STOP to exit")
#     while True:
#         res = input("Enter molecular formula: ")
#         if not res or res == "STOP": break
#         try: print("Molar mass: %.6f (round to discretion)" % calcMolarMass(res))
#         except Exception as e: print("invalid:", e)
#
#     print("Program terminated")

    with open("temp.txt") as f:
        for line in f:
            print("%.6f" % calcMolarMass(line.strip("\n")))