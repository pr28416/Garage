with open("random_output.txt") as f:
    numbers = []
    for _ in range(100):
        numbers.append(float(f.readline()))

from WichmanHill import r8_random as rand

print(rand(100, 200, 300))


# s1 = s2 = s3 = 100
# for i in range(5):
#     val, s1, s2, s3 = rand(s1, s2, s3)
#     print(val)

first=0.44960042304882464
0.44960041783776544
0.44960042394708233
val=1

for i in range(100, 1000):
    for j in range(100, 1000):
        for k in range(100, 1000):
            tmp,a,b,c=rand(i,j,k)
            if abs(tmp-first) < abs(val-first):
                val=tmp
                print("changing to %s %s %s (val=%s)" % (i,j,k,val))


# s1, s2, s3 = 533, 888, 963
# for i in range(100):
#     val, s1, s2, s3 = rand(s1, s2, s3)
#     print(val)

# for a in range(100, 1000):
#     for b in range(100, 1000):
#         for c in range(100, 1000):
#             # print("new:", a, b, c)
#             s1, s2, s3 = a, b, c
#             for i in range(100):
#                 val, s1, s2, s3 = rand(s1, s2, s3)
#                 # if round(val*10000000)//10000000 != round(numbers[i]*10000000)//10000000:
#                 if val != numbers[i]:
#                     break
#             else:
#                 print(a, b, c)
#                 break
#         else: continue
#         break
#     else: continue
#     break