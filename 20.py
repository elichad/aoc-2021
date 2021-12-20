import numpy as np
import re

with open("20.txt") as f:
#with open("20-test.txt") as f:
    algorithm=f.readline().strip()
    algorithm=re.sub("\.","0",algorithm)
    algorithm=re.sub("#","1",algorithm)
    f.readline()
    grid={}
    j_max=0
    i=0
    for line in f.readlines():

        line=re.sub("\.","0",line)
        line=re.sub("#","1",line).strip()
        for j in range(len(line)):
            grid[(i,j)]=line[j]
        i+=1
        j_max=j
    for m in [-1,i]:
        for n in range(-1,j_max+2):
            print(m,n)
            grid[(m,n)]="0"
    for n in [-1,j_max+1]:
        for m in range(-1,i+1):
            print(m,n)
            grid[(m,n)]="0"
    print(grid)


for i in range(50):
    print(i)
    start_grid=grid.copy()
    start_keys=start_grid.keys()
    for k in start_keys:
        x_items=[k[0]-1,k[0],k[0]+1]
        y_items=[k[1]-1,k[1],k[1]+1]
        number=""
        for x in x_items:
            for y in  y_items:
                if (x,y) not in start_grid:
                    if i%2==0:
                        grid[(x,y)]="1"
                        number+="0"
                    else:
                        grid[(x,y)]="0"
                        number+="1"
                else:
                    number+=start_grid[(x,y)]
        n=int(number,2)
        grid[k]=algorithm[n]
#    print(sorted(grid.keys()))

#count
count={"0":0,"1":0}
for i in grid.values():
    count[i]+=1
print(count)