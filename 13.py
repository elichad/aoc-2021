import numpy as np

with open("13.txt") as f:
#with open("13-test.txt") as f:

    holes=set()
    holes_data, folds_data=f.read().split('\n\n')
    for line in holes_data.split('\n'):
        x,y=[int(i) for i in line.strip().split(',')]
        holes.add((x,y))

    for line in folds_data.split('\n'):
        direction,val=line.strip().split()[-1].split('=')
        val=int(val)
        index=0 if direction=="x" else 1
        for hole in holes.copy():
            if hole[index]>val:
                if index==0:
                    new_hole=(2*val-hole[0], hole[1])
                else:
                    new_hole=(hole[0], 2*val-hole[1])
                holes.discard(hole)
                holes.add(new_hole)
        print(direction, val, len(holes))

    paper=np.full((40,6)," ")
    for hole in holes:
        paper[hole]="#"
    s=""
    for i in range(6):
        l=paper[:,i]
        for j in range(len(l)):
            s+=l[j]
        s+="\n"
    print(s)