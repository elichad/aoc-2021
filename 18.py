import numpy as np
import re

with open("18.txt") as f:
#with open("18-test.txt") as f:
    nos=f.read().split("\n")
    print(nos)

def reduce(numbers):
    print(numbers)
    calc=""
    for n in range(len(numbers)):
        if n==0:
            print(calc)
            calc=numbers[n]
        #elif n>20:
        #    break
        else:
            calc="[{},{}]".format(calc,numbers[n])
            actioned=True
            w=0
            while actioned==True:
                w+=1
                #print(w, calc)
                actioned=False
                matches=re.finditer("\[[0-9]+,[0-9]+\]",calc)
                for match in matches:
                    m="\[{}\]".format(match.group()[1:-1])
                    pre=calc[:match.span()[0]]
                    post=calc[match.span()[1]:]

                    l = re.findall("\[",pre)
                    r = re.findall("\]",pre)
                    if len(l)-len(r)>=4:
                        #explode
                        i,j=[int(k) for k in m.strip("\[]").split(",")]
                        #print("booming {}, {}".format(i,j))
                        left = re.search("[0-9]+",pre[::-1])
                        right = re.search("[0-9]+",post)
                        if left:
                            l_val=int(left.group()[::-1])+i
                            pre=re.sub(left.group(),str(l_val)[::-1],pre[::-1],count=1)[::-1]
                        if right:
                            r_val=int(right.group())+j
                            post=re.sub(right.group(),str(r_val),post,count=1)

                        calc="{}0{}".format(pre,post)
                        actioned=True
                        break
                if actioned==False:
                    match=re.search("[0-9]{2,}",calc)
                    if match:
                        val=int(match.group())
                        to_sub="[{},{}]".format(int(val/2),int((val+1)/2))
                        #print("subbing {} with {}".format(val,to_sub))
                        calc=re.sub(str(val),to_sub,calc,count=1)
                        actioned=True
                        continue
        print("end of sum {}: {}".format(n,calc))
    return calc

#magnitude
def magnitude(calc):
    w=0
    while w<10:
        w+=1
        matches=re.finditer("\[[0-9]+,[0-9]+\]",calc)
        for match in matches:
            m="\[{}\]".format(match.group()[1:-1])
            i,j=[int(k) for k in m.strip("\[]").split(",")]
            magnitude=3*i+2*j
            #print("subbing {} with {}".format(m,magnitude))
            calc=re.sub(m,str(magnitude),calc,count=1)
        print(calc)

    print(int(calc))
    return int(calc)

max_mag=0
for m in range(len(nos)):
    for n in range(len(nos)):
        if m==n:
            continue
        c=reduce([nos[m],nos[n]])
        mag=magnitude(c)
        print("combined {} and {} to make {} with mag {}".format(m,n,c,mag))
        if mag>max_mag:
            max_mag=mag


print(max_mag)