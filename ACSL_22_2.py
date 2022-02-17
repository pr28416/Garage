def fibCypher(num1, num2, key, msg):
    fib, enc = [num1, num2] + [0] * 18, []
    for i in range(2, len(fib)): fib[i] = fib[i-1] + fib[i-2]
    for i, c in enumerate(msg): enc.append(str(ord(c)+3*((ord(key)-97+fib[i%20])%26+97)))
    return " ".join(enc)

print(fibCypher(3, 7, 'h', 'ACSL c2'))