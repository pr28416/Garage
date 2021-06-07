from king import find_king_status as fd

with open("king_testcases.txt") as f:
    print("Testing king.py")
    for test in range(15):
        pieces = f.readline().strip("\n")
        print(f"Test {test+1} ", end="")
        try:
            assert fd(pieces) == f.readline().strip("\n")
            print("passed.")
        except:
            print("failed.")