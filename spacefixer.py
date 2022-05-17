with open("payments_full.txt") as f:
    rows = [i.split("\t") for i in f.readlines()]
    for i in range(len(rows)):
        rows[i] = [s.replace(" ", "") for s in rows[i]]

with open("output.txt", "w") as f:
    for line in rows:
        f.write("\t".join(line))
























