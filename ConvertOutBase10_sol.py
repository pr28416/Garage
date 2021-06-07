from math import log

def convertFromBase10(num, base):
    # Create conversion dictionary
    numToChar = {i:"0123456789ABCDEF"[i] for i in range(16)}
    # Set power to largest
    power = int(log(num, base))
    # Convert number
    converted = ""
    for pow in range(power, -1, -1):
        # Divide
        converted += numToChar[num//(base**pow)]
        # Remainder
        num %= base**pow
    # Return
    return converted

print(convertFromBase10(18238, 7))
