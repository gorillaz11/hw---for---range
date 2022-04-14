rows =25
for i in range(1,rows):
    for j in range(rows-i,-1,-1):
        print(end=" ")
    for j in range(i,0,-1):
        print(j, end="")
    for j in range(2,i+1,):
        print(j, end="")
    print()