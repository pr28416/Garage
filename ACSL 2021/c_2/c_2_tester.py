from c_1_sol import sumOfLastRow as solr

with open("c_1_testcases.txt") as f:
    print("Testing c_1_sol.py")
    for test in range(10):
        print(f"Test {test+1} ", end="")
        try:
            ans = solr(*map(int, f.readline().split(" ")))
            cor = int(f.readline())
            assert ans == cor, f"{ans} {cor}"
            print("passed.")
        except AssertionError as a:
            print("failed.", a)