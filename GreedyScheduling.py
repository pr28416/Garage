# intervals = [[1, 3], [7, 12], [2, 5], [6, 18], [14, 16]]
intervals = [[100, 200], [150, 700], [50, 70], [39, 48], [234, 546]]
intervals.sort(key=lambda x: (x[1], x[0]))
print(intervals)
count = 0
visited = []
end = -1
for interval in intervals:
    if end <= interval[0]:
        end = interval[1]
        count += 1
        visited.append(interval)

print(count, visited)
