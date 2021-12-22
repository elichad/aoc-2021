import numpy as np
import re
import functools

with open("22.txt") as f:
#with open("22-test.txt") as f:
    grid=np.zeros((101,101,101))
    for line in f.readlines():
        state,dirs= line.strip().split()
        state = 1 if state=="on" else 0
        dirs = dirs.split(",")
        set_x=None
        set_y=None
        set_z=None
        for d in dirs:
            dir = d[0]
            vals = tuple([int(i) for i in d.split("=")[1].split("..")])
            if vals[0] <-50 or vals[1]>50:
                print("continuing")
                continue
            if dir=="x":
                dir=0
                set_x=(vals[0]+50, vals[1]+50)
            elif dir=="y":
                dir=1
                set_y=(vals[0]+50, vals[1]+50)
            elif dir=="z":
                dir=2
                set_z=(vals[0]+50, vals[1]+50)
        if set_x and set_y and set_z:
            grid[set_x[0]:set_x[1]+1,set_y[0]:set_y[1]+1,set_z[0]:set_z[1]+1]=state
        print(set_x,set_y,set_z)


    print(np.sum(grid))


def update_tuple(inp,n,values):
    if n==0:
        return (*values,*inp[2:])
    if n==1:
        return (*inp[:2],*values,*inp[4:])
    if n==2:
        return (*inp[:4],*values)

#with open("22.txt") as f:
with open("22-test.txt") as f:
    # ambitious attempt to create something in anticipation of part but it's just fundamentally wrong
    states={(-50,50,-50,50,-50,50):0}
    for line in f.readlines():
        state,dirs= line.strip().split()
        state = 1 if state=="on" else 0
        dirs = dirs.split(",")
        for d in dirs:
            dir = d[0]
            vals = tuple([int(i) for i in d.split("=")[1].split("..")])
            if vals[0] <-50 or vals[1]>50:
                continue
            if dir=="x":
                dir=0
            elif dir=="y":
                dir=1
            elif dir=="z":
                dir=2

            states
            print(dir,state,vals,states)
            added=None
            for r in list(states.keys()):
                k=(r[dir*2],r[dir*2+1])
                exist_range=range(k[0],k[1]+1)
                if vals[0] in exist_range or vals[1] in exist_range:

                    if state==states[r]:
                        states.pop(r)
                        if added:
                            states.pop(added)
                            new_range = (min(k[0],vals[0],added[dir*2]),max(k[1],vals[1],added[dir*2+1]))
                        else:
                            new_range = (min(k[0],vals[0]),max(k[1],vals[1]))
                        to_add = update_tuple(r,dir,new_range)
                        states[to_add]=state
                        added=to_add
                    else:
                        states.pop(r)
                        below_range=0
                        above_range=0
                        in_range=k
                        if vals[0]>k[0]:
                            below_range=(k[0],vals[0]-1)
                            in_range=(vals[0],in_range[1])
                        if vals[1]<k[1]:
                            above_range=(vals[1]+1,k[1])
                            in_range=(in_range[0],vals[1])
                        if below_range:
                            to_add=update_tuple(r,dir,below_range)
                            states[to_add]=1 if state==0 else 0
                        if above_range:
                            to_add=update_tuple(r,dir,above_range)
                            states[to_add]=1 if state==0 else 0
                        #compare[in_range]=state
                        #added=True
                elif vals[0]<k[0] and vals[1]>k[1]:
                    states.pop(r)
            if not added:
                print("{} not in keys for dir {}".format(vals,dir))
                to_add=update_tuple(r,dir,vals)
                states[to_add]=state

            print(dir,states)

    s=0
    for k in states.keys():
        p=1
        for d in range(3):
            p*=abs(k[d+1]-k[d])
        s+=states[k]*p
    print(s)