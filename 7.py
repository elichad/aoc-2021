with open("7.txt") as f:
#with open("7-test.txt") as f:
    positions=[int(i) for i in f.readline().strip().split(",")]
    print(positions)

    fuel_max=920000000
    for i in range(max(positions)):
        fuel=sum([abs(j-i) for j in positions])
        if fuel<fuel_max:
            fuel_max=fuel
        else:
            break

    fuel_new_max=920000000
    for i in range(max(positions)):
        fuel_new=sum([sum(range(abs(j-i)+1)) for j in positions])
        if fuel_new<fuel_new_max:
            fuel_new_max=fuel_new
        else:
            break


    print(fuel_max)
    print(fuel_new_max)