import numpy as np

with open("14.txt") as f:
#with open("14-test.txt") as f:
    original=f.readline().strip()
    f.readline()
    rules={}
    for line in f.readlines():
        pair,value=line.strip().split(" -> ")
        rules[pair]=value
    pair_count={}
    for i in range(len(original)-1):
        p=original[i:i+2]
        print(p)
        if p in pair_count:
            pair_count[p]+=1
        else:
            pair_count[p]=1

    for i in range(40):
        pair_count_2=pair_count.copy()
        for k in pair_count_2.keys():
            current=pair_count_2[k]
            extra_letter=rules[k]
            new_one=k[0]+extra_letter
            new_two=extra_letter+k[1]
            pair_count[k]-=current
            if new_one in pair_count:
                pair_count[new_one]+=current
            else:
                pair_count[new_one]=current
            if new_two in pair_count:
                pair_count[new_two]+=current
            else:
                pair_count[new_two]=current

    minimum=99999999999999999999999999999
    minimum_letter=""
    maximum=0
    maximum_letter=""
    letter_counts={a:0 for a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    print(letter_counts)
    for k in pair_count.keys():
        v=pair_count[k]
        letter_counts[k[0]]+=v
    letter_counts[original[-1]]+=1
    print(letter_counts)

    for a in letter_counts.keys():
        print(a,minimum, maximum)
        if letter_counts[a]==0:
            continue
        if letter_counts[a]<minimum:
            minimum=letter_counts[a]
            minimum_letter=a
        if letter_counts[a]>maximum:
            maximum=letter_counts[a]
            maximum_letter=a
        print(a,minimum, maximum)
    print(maximum-minimum)
