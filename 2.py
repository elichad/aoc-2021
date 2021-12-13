with open("2.txt") as f:
    instructions=[line.split() for line in f.readlines()]
    values={
        "horizontal":0,
        "aim":0,
        "depth":0,
    }
    for i in instructions:
        d=i[0]
        n=int(i[1])
        if d=="forward":
            values["horizontal"]+=n
            values["depth"]+=values["aim"]*n
        elif d=="down":
            values["aim"]+=n
        elif d=="up":
            values["aim"]-=n
        else:
            print("bad command",d)

    horizontal=values["horizontal"]
    depth=values["depth"]

    print(horizontal*depth)