import numpy as np

with open("19.txt") as f:
#with open("19-test.txt") as f:
    scanners=f.read().split("\n\n")
    orig=[]
    for s in scanners:
        content=s.split("\n")
        cs=[]
        for c in content[1:]:
            c=c.strip().split(",")
            c=[int(i) for i in c]
            cs.append(c)
        orig.append(cs)

    print(orig)

needed_beacons=12

permutations=[
    (-1,-1,-1,0),
    (-1,-1,-1,1),
    (-1,-1,-1,2),
    (-1,-1,1,0),
    (-1,-1,1,1),
    (-1,-1,1,2),
    (-1,1,-1,0),
    (-1,1,-1,1),
    (-1,1,-1,2),
    (-1,1,1,0),
    (-1,1,1,1),
    (-1,1,1,2),
    (1,-1,-1,0),
    (1,-1,-1,1),
    (1,-1,-1,2),
    (1,-1,1,0),
    (1,-1,1,1),
    (1,-1,1,2),
    (1,1,-1,0),
    (1,1,-1,1),
    (1,1,-1,2),
    (1,1,1,0),
    (1,1,1,1),
    (1,1,1,2)
]

scans=orig.copy()
fixed={0:(0,0,0)}
w=0
while len(fixed.keys())<len(scans) and w<10:
    w+=1
    for s in range(len(scans)):
        if s not in fixed:
            continue
        for t in range(len(scans)):
            if t in fixed:
                continue
            if s==t:
                continue
            print("testing ",s,t)
            fixed_position=fixed[s]
            possible_positions={}
            possible_permutations={}
            s_items=scans[s]
            t_items=scans[t]
            for i in range(len(s_items)):
                for j in range(len(t_items)):
                    for k,l,m,n in permutations:
                        s_item=s_items[i]
                        t_item=t_items[j]
                        x=s_item[0] - k*t_item[n]
                        y=s_item[1] - l*t_item[(n+1)%3]
                        z=s_item[2] - m*t_item[(n+2)%3]
                        if (x,y,z) not in possible_positions:
                            possible_positions[(x,y,z)]={}
                        if (k,l,m,n,1) not in possible_positions[(x,y,z)]:
                            possible_positions[(x,y,z)][(k,l,m,n,1)]=0
                        possible_positions[(x,y,z)][(k,l,m,n,1)]+=1
                        x=s_item[0] - k*t_item[n]
                        y=s_item[1] - l*t_item[(n-1)%3]
                        z=s_item[2] - m*t_item[(n-2)%3]
                        if (x,y,z) not in possible_positions:
                            possible_positions[(x,y,z)]={}
                        if (k,l,m,n,-1) not in possible_positions[(x,y,z)]:
                            possible_positions[(x,y,z)][(k,l,m,n,-1)]=0
                        possible_positions[(x,y,z)][(k,l,m,n,-1)]+=1
            best_position=0
            best_position_count=0
            for p in possible_positions.keys():
                total=sum(possible_positions[p].values())
                if total>best_position_count:
                    best_position=p
                    best_position_count=total
                    best_permutation=0
                    best_permutation_count=0
                    #print(p,possible_positions[p])
                    for q in possible_positions[p].keys():
                        if possible_positions[p][q]>best_permutation_count:
                            best_permutation=q
                            best_permutation_count=possible_positions[p][q]

            print(best_position,best_position_count, best_permutation, best_permutation_count)
            if best_position_count>=needed_beacons:
                # transform t rel to s
                transformed_items = []
                for i in range(len(t_items)):
                    t_item=t_items[i]
                    k,l,m,n,o=best_permutation
                    x=best_position[0] + k*t_item[n%3]
                    y=best_position[1] + l*t_item[(n+o*1)%3]
                    z=best_position[2] + m*t_item[(n+o*2)%3]
                    transformed_items.append([x,y,z])
                    #print("transformed {} to {}".format(t_item,(x,y,z)))
                scans[t]=transformed_items
                print("fixing {} at {}".format(t,best_position))
                #print(scans[t])
                fixed[t]=best_position

#combine sets
all_beacons=set()
for i in range(len(scans)):
    if i not in fixed:
        continue
    for j in range(len(scans[i])):
        a = scans[i][j]
        all_beacons.add((a[0],a[1],a[2]))

print(len(all_beacons))
#print(sorted(all_beacons))

max_manhattan=0
for i in fixed.keys():
    for j in fixed.keys():
        if i==j:
            continue
        manhattan = sum([abs(fixed[i][n]-fixed[j][n]) for n in range(3)])
        if manhattan>max_manhattan:
            max_manhattan=manhattan

print(max_manhattan)