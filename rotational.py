N = int(input())
for _ in range(N):
    A = input()
    B = input()
    if len(A) != len(B):
        print("NO")
    else:
        for i in range(len(A)):
            if A == B:
                print("YES")
                break
            B = B[-1] + B[:len(B)-1]
        else:
            print("NO")
