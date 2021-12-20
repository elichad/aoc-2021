import numpy as np

# a failed attempt to match scanners using relative differences between beacons

#with open("19.txt") as f:
with open("19-test-2.txt") as f:
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

permutation_sets=[]
locs=[]
for scanner_items in orig:
    permutations=set()
    orientations={}
    locations=np.empty((len(scanner_items),len(scanner_items),3))
    #print(scanner_items)
    for i in range(len(scanner_items)):
        for j in range(len(scanner_items)):
            if j>=i:
                continue
            x=scanner_items[j][0]-scanner_items[i][0]
            y=scanner_items[j][1]-scanner_items[i][1]
            z=scanner_items[j][2]-scanner_items[i][2]
            relative=(x,y,z)
            locations[i,j]=relative
            #print(scanner_items[j],scanner_items[i],relative)
            for k in [-1,1]:
                for l in [-1,1]:
                    for m in [-1,1]:
                        for n in [0,1,2]:
                            if (k,l,m,n) not in orientations:
                                orientations[(k,l,m,n)]=set()
                        orientations[(k,l,m,0)].add((k*x,l*y,m*z))
                        orientations[(k,l,m,1)].add((k*y,l*z,m*x))
                        orientations[(k,l,m,2)].add((k*z,l*x,m*y))

                        #print((k*x,l*y,m*z),orientations[(k,l,m)])
    #print(orientations)
    permutation_sets.append(orientations.copy())
    locs.append(locations)

#print(permutation_sets[0])

fixes={0:(1,1,1,0)}
total_sensors=set()
#while len(fixes.keys())<=len(scanners):
for i in range(len(permutation_sets)):
    for j in range(len(permutation_sets)):
        if j>=i or i>=len(scanners):
            continue
        p=permutation_sets[i]
        if i in fixes:
            p={fixes[i]: p[fixes[i]]}
            print("fixed {} at {}".format(i,p.keys()))
        q=permutation_sets[j]
        if j in fixes:
            q={fixes[j]: q[fixes[j]]}
            print("fixed {} at {}".format(j,q.keys()))

        max_overlap_len=0
        max_overlap=0
        max_combo=0

        for k in p.keys():
            for l in q.keys():
                overlap=p[k].intersection(q[l])
                print(overlap)
                #print(i,k,j,l,overlap)
                #if len(overlap)/2>12:
                if len(overlap)>max_overlap_len:
                    max_overlap_len=len(overlap)
                    max_overlap=overlap
                    max_combo=(i,k,j,l)
                    permutation_sets.append({k: p[k].union(q[l])})

        print("results are ",max_combo,max_overlap)
        if max_overlap!=0:
            if max_combo[0] in fixes:
                fixes[max_combo[2]]=max_combo[3]
            if max_combo[2] in fixes:
                fixes[max_combo[0]]=max_combo[1]
            #add that permutation to total
            #total_sensors=total_sensors.union(p[max_combo[1]]).union(q[max_combo[l]])

print(fixes)


            #find positions
