with open("1.txt") as f:
    numbers=[int(line) for line in f.readlines()]
    aggregates=[sum(numbers[j:j+3]) for j in range(0,len(numbers)-2)]
    c = 0
    for i in range(1, len(numbers)):
        if numbers[i]>numbers[i-1]:
            c+=1
    d = 0
    for i in range(1, len(aggregates)):
        if aggregates[i]>aggregates[i-1]:
            d+=1

    print(c, d)