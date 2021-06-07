N = int(input("Enter number of commands:"))
print("Commands:")
commands = [list(map(input().split(" "))) for _ in range(N)]
variables = {}
ACC = None
for command in commands:
    if command[1] == "DC":
        val = command[2]
        try:
            val = float(val)
        except:
            try:
                val = int(val)
            except:
                pass
        variables[command[0]] = val

    # elif command[1] == "LOAD":
