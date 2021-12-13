with open("6.txt") as f:
#with open("6-test.txt") as f:
    start=[int(i) for i in  f.readline().strip().split(",")]
    state={i:0 for i in range(7)}
    feed={i:0 for i in range(7)}
    for i in start:
        state[i]+=1

for d in range(256):
    day=d%7
    feed_day=(d+2)%7
    feed[feed_day]+=state[day]
    state[day]+=feed[day]
    feed[day]=0

print(sum(state.values())+sum(feed.values()))