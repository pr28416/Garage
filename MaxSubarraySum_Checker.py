from MaxSubarraySum import maxSubarraySum
with open("MaxSubarraySum_Input.txt") as fin:
    with open("MaxSubarraySum_Output.txt") as fout:
        for t in range(1, 15):
            try:
                arr = list(map(int, fin.readline().split(" ")))
                assert maxSubarraySum(arr) == int(fout.readline()), f"Incorrect output"
                print(f"Test case {t} passed")
            except Exception as e:
                print(f"Test case {t} failed:", e)
