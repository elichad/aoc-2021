with open("8.txt") as f:
#with open("8-test.txt") as f:

    original=[]
    digits=[]
    for line in f.readlines():
        print(line)
        o,d=line.strip().split(" | ")
        original.append(o.split())
        digits.append(d.split())

    v=0
    unique={2,4,3,7}
    unique_count=0
    for display in range(len(digits)):
        mapping={}
        hold={}
        o=sorted(original[display],key=len)
        print(o)
        for x in o:
            x="".join(sorted(x))
            match len(x):
                case 2:
                    mapping[x]=1
                    hold[1]=set(x)
                case 3:
                    mapping[x]=7
                case 4:
                    mapping[x]=4
                    hold[4]=set(x)
                case 5:
                    y=set(x)
                    if y.intersection(hold[1])==hold[1]:
                        mapping[x]=3
                    elif len(y.difference(hold[4]))==2:
                        mapping[x]=5
                    else:
                        mapping[x]=2
                case 6:
                    if set(x).intersection(hold[1])==hold[1]:
                        if set(x).intersection(hold[4])==hold[4]:
                            mapping[x]=9
                        else:
                            mapping[x]=0
                    else:
                        mapping[x]=6
                case 7:
                    mapping[x]=8
            if len(x) in unique:
                unique_count+=1

        print(mapping)
        d=digits[display]
        w=int("".join(str(mapping["".join(sorted(z))]) for z in d))
        print(w)
        v+=w

print(unique_count)
print(v)