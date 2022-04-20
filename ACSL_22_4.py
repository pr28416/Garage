def cycleLength(realPartC, imagPartC):
    ul, f, n = [], lambda z: z*z+realPartC+imagPartC*1j, 0+0j
    for _ in range(500):
        ul.append(n)
        n = round((q:=f(n)).real,2)+round(q.imag,2)*1j
        if abs(n) > 4: return f"ESCAPES {len(ul)}"
        if n in ul: return str(len(ul)-ul.index(n))