if __name__ == '__main__':
    #records = [['v', 1.0]]
    #records = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Tinas', 37.2], ['Akriti', 41], ['Harsh', 39]]
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    print(records)
    t = []
    for rec in records:
        t.append(rec[1])
    t.sort()
    t = [float(x) for x in list(dict.fromkeys(t))]
    print(t)

    if len(t) > 1:
        sgrd = float(t[1])
    if len(t) == 1:
        sgrd = float(t[0])

    names = []
    for rec in records:
        if rec[1] == sgrd:
            names.append(rec[0])

    names.sort()
    for name in names:
        print(name)