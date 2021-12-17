import numpy as np

with open("17.txt") as f:
#with open("17-test.txt") as f:
    content=f.read().strip().split()[2:]
    area_x=(int(content[0].split("..")[0][2:]), int(content[0].split("..")[1][:-1]))
    area_y=(int(content[1].split("..")[0][2:]), int(content[1].split("..")[1]))
    print(content, area_x, area_y)

    test_x=list(range(area_x[0],area_x[1]+1))
    test_y=list(range(area_y[0],area_y[1]+1))
    print(test_x)
    print(test_y)
    max_y = -(area_y[0]+1)

    valid_x={}
    for x in range(area_x[1]+1):
        vx=x
        d=0
        n=0
        while d<=area_x[1] and n<max_y*2+5:
            d+=vx
            if vx>0:
                vx-=1
            if d in range(area_x[0],area_x[1]+1):
                if n not in valid_x:
                    valid_x[n]=[x]
                else:
                    valid_x[n].append(x)
            n+=1
    #print(valid_x)

    combos=set()
    for y in range(area_y[0],max_y+1):
        print("testing ",y)
        vy=y
        d=0
        n=0
        while d>=area_y[0]:
            d+=vy
            vy-=1
            if d in range(area_y[0],area_y[1]+1):
                if n in valid_x:
                    for x in valid_x[n]:
                        combos.add((x,y))
                        print("combo at step {}: {} {}".format(n,x,y))
            n+=1

    print(combos)
    print(len(combos))
