def findTime(c1, c2, c3, c4, c5):
    hours = minutes = 0
    for c, v in zip([c1, c2, c3, c4, c5], [1, 1, 2, 3, 5]):
        if c in {"R", "B"}: hours += v
        if c in {"G", "B"}: minutes += v*5
    if minutes == 60:
        hours += 1
        minutes = "00"
    elif minutes < 10: minutes = f"0{minutes}"
    else: minutes = str(minutes)
    hours %= 12
    hours = f"0{hours}" if hours < 10 else str(hours)
    return f"{hours}:{minutes}"


