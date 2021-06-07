# Define function
def longest_substring_repeating_chars(string):
    lo, up, finlo, finup = 0, 1, 0, 1
    while up < len(string):
        if string[up] != string[up-1]:
            if finup - finlo < up - lo:
                finlo, finup = lo, up
            lo = up
        up += 1
    if finup - finlo < up - lo:
        finlo, finup = lo, up
    return string[finlo:finup]

# Test function
func = longest_substring_repeating_chars
print(func("abbabaaaabbba"))
print(func("abccbcaacaaab"))
print(func(""))
print(func("abcdef"))