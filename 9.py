import numpy as np

with open("9.txt") as f:
#with open("9-test.txt") as f:
    lines=f.readlines()
    grid=np.zeros((len(lines),len(lines[0])-1),int)
    for i in range(len(lines)):
        grid[i]=list(lines[i].strip())

    print(grid)

    skip=set()
    lows=set()
    for ind,v in np.ndenumerate(grid):
        if ind in skip:
            continue

        check=[]
        if ind[0]!=0:
            check.append((ind[0]-1,ind[1]))
        if ind[0]!=len(grid)-1:
            check.append((ind[0]+1,ind[1]))
        if ind[1]!=0:
            check.append((ind[0],ind[1]-1))
        if ind[1]!=len(grid[0,:])-1:
            check.append((ind[0],ind[1]+1))

        low=True
        for c in check:
            if grid[c]>v:
                skip.add(c)
            else:
                low=False

        if low:
            print(ind,v)
            lows.add(ind)

risks=sum(grid[l]+1 for l in lows)
print(risks)