import numpy as np
import re
import functools

with open("21.txt") as f:
#with open("21-test.txt") as f:
    orig = [int(line.strip()[-1]) for line in f.readlines()]
    starts=orig.copy()
    print(starts)
    scores = [0,0]
    die=0
    fin=21
    perms={}
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i+j+k not in perms:
                    perms[i+j+k]=0
                perms[i+j+k]+=1
    print(perms)
    universes=[[starts,scores]]
    count={0:0,1:0}
    w=0
    while len(universes)>0 and w<5:
        print(w, len(universes))
        w+=1
        tot = 0
        die+=3
        #for i in range(3):
        #    die+=1
        #    tot+=die
        i=1-(int(die/3))%2
        for k in range(len(universes)):
            starts,scores=universes.pop(0)
            for p in perms:
                starts[i] += p
                starts[i] = starts[i]%10
                if starts[i] ==0:
                    starts[i] = 10
                scores[i] += starts[i]
                if scores[i]>=fin:
                    count[i]+=1
                universes.append([starts,scores])



# print(scores)
# print(min(scores)*die)

# positions = range(1,11)
# scores=range(1,fin)
# finish={0:0,1:0}
# track={}
# for i in positions:
#     for j in positions:
#         for s in scores[::-1]:
#             for t in scores[::-1]:
#                 if s==0 and t==0:
#                     if i!=starts[0] or j!=starts[1]:
#                         continue
#                 for p in perms:
#                     ii = (i+p)%10
#                     if ii==0:
#                         ii=10
#                     ss=s+ii
#                     if ss>fin:
#                         finish[0]+=perms[p]
#                         track[(i,j,s,t,p,0)]=perms[p]
#                     track[(i,j,s,t,p,0)]=(ii,j,ss,t)

#                     jj = (j+p)%10
#                     if jj==0:
#                         jj=10
#                     tt=t+jj
#                     if tt>fin:
#                         finish[1]+=perms[p]
#                         track[(i,j,s,t,p,1)]=perms[p]
#                     track[(i,j,s,t,p,1)]=(i,jj,s,tt)

# values={}
# combos = {}
# for i in positions:
#     for p in perms:
#         new_pos = (i+p)%10
#         if new_pos==0:
#             new_pos=10

#         combos[(i,p)]=new_pos

# counts=[]
# for i in orig:
#     print(i)
#     w=1
#     universes=[(i,0,1)]
#     count={}
#     while len(universes)>0:
#         print(len(universes))
#         for u in range(len(universes)):
#             state = universes.pop(0)
#             for p in perms:
#                 no = state[2]*perms[p]
#                 pos = combos[(state[0],p)]
#                 s= state[1]+pos
#                 if s>=fin:
#                     if w not in count:
#                         count[w]=0
#                     count[w]+=no
#                 else:
#                     universes.append((pos,s,no))
#         w+=1
#     print(count)
#     counts.append(count)

# wins={0:0,1:0}
# for i in counts[0].keys():
#     for j in counts[1].keys():
#         s=counts[0][i]
#         t=counts[1][j]

#         if j>=i: # 1 takes longer than 0 to win
#             varieties = 27**i
#             for k in range(3,i):
#                 print("subtracting ",k)
#                 varieties/=counts[1][k]
#             wins[0]+=s*varieties
#         else: # 1 wins earlier
#             varieties = sum(counts[0].values())
#             for k in range(3,i):
#                 print("subtracting ",k)
#                 varieties-=counts[0][k]
#             wins[1]+=varieties*t
#         print(i,j,s,t,varieties,wins)

# print(wins)

# heavily inspired by reddit solutions teaching me about functools.cache
@functools.cache
def update(x,y,s,t):
    outsx=[]
    outsy=[]
    for p in perms:
        xx=(x+p)%10 or 10
        ss=s+xx
        if ss>=fin:
            outsx.append(perms[p])
            outsy.append(0)
        else:
            outy,outx = update(y,xx,t,ss)
            outsx.append(outx*perms[p])
            outsy.append(outy*perms[p])
    return sum(outsx),sum(outsy)

wins={0:0,1:0}
result = update(orig[0],orig[1],0,0)
print(max(result))