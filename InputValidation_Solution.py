def getInput(prompt="", cast=None, condition=None, errorMessage=None):
    while True:
        try:
            response = (cast or str)(input(prompt))
            assert condition is None or condition(response)
            return response
        except:
            print(errorMessage or "Invalid input. Try again.")


# Get personal information
name = getInput(prompt="Enter your name: ")
age = getInput(prompt="Enter your age: ",
               cast=int,
               condition=lambda x: x > 0)
height=getInput(prompt="Enter your height in inches: ",
                cast=float,
                condition=lambda x: x > 0,
                errorMessage="That's not a valid height!")
# Do list math
numbers = getInput(prompt="Enter integers: ",
                   cast=lambda line: list(map(int, line.split(" "))),
                   errorMessage="Invalid input. Make sure to separate your integers with a single space.")

print(name, age, height, type(name), type(age), type(height))
print(numbers, sum(numbers))

