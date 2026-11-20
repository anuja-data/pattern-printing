for i in range(1, 6):# run the loop from 1 to 6
    for j in range(6 - i):  # spaces first
        print(" ", end=" ")
    for k in range(i):   # then i stars
        print("*", end=" ")
    print()  # move to next line