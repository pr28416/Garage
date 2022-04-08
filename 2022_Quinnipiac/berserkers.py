# runs = input()
# results = []
# temp = []
# time = 0
# location = 0
# thing = False

# for x in range(int(runs)):
#     temp = []
#     b1, r1, b2, r2, c = map(int, input().split(" "))
#     # for y in values:
#     #     if y == " ":
#     #        thing = True 
#     #     else:
#     #         temp.append(y)
#     # b1 = int(temp[0])
#     # r1 = int(temp[1])
#     # b2 = int(temp[2])
#     # r2 = int(temp[3])
#     # c = int(temp[4])

#     # if b1 == b2:
#     #     time = 0
#     # else:
#     time = (b2-b1)/(r1-r2)
#     location = (r1 * time) + b1

#     if int(location) >=  c:
#         results.append("MORE SUPPORT")
#     elif location < 0:
#         results.append("MORE SUPPORT")
#     else:
#         results.append(str(int(time)) + " " + str(int(location)))
    
# for n in results:
#     print(n)

N = int(input().strip(" "))
for _ in range(N):
    b1,r1,b2,r2,c = map(int,input().split(" "))
    # if r1 == r2 and b1 != b2:
    #     print("MORE SUPPORT")
    #     continue
    if (r1 == r2):
        if (b1 != b2):
            print("MORE SUPPORT")
        else:
            print(f"{b1} 0")
    else:
        t = (b2-b1)//(r1-r2)
        # if (t != int(t)):
        l2 = b2+(r2*t)
        l1 = b1+(r1*t)
        if t != int(t) or l1 != l2 or l1 >= c or l2 >= c or t < 0:
            print("MORE SUPPORT")
        else:
            print(f"{int(t)} {int(l1)}")