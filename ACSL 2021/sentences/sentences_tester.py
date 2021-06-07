from sentences import generate_sentences as gs

with open("sentences_testcases.txt") as f:
    print("Testing sentences.py")
    for test in range(13):
        N = int(f.readline())
        dictionary = []
        for _ in range(N):
            dictionary.append(f.readline().strip("\n"))
        sentences = f.readline().strip("\n")
        print(f"Test {test+1} ", end="")
        try:
            assert gs(dictionary, sentences) == f.readline().strip("\n")
            print("passed.")
        except:
            print("failed.")