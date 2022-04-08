N = int(input().strip(" "))
for _ in range(N):
    K = int(input())
    init = input().strip(" ")
    for _ in range(K):
        inst = input().strip(" ").split(" ")
        init += init[int(inst[0]):int(inst[0])+int(inst[1])] + inst[2]
    if len(init) > 1000:
        print(init[len(init)-1000:])
    else:
        print(init)
