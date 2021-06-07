# Define printSubsets() function
def printSubsets(lst, toggles=None, i=0):
    if toggles == None:
        toggles = [0] * len(lst)

    if i >= len(lst):
        subset = [str(lst[i]) for i in range(len(lst)) if toggles[i] == 1]
        print("{" + ", ".join(subset) + "}")

    else:
        toggles[i] = 0
        printSubsets(lst, toggles, i+1)
        toggles[i] = 1
        printSubsets(lst, toggles, i+1)


# Test function
printSubsets(['a', 'b', 'x', 'y'])
