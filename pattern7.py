for i in range(5):# run the loop 5 times
    for j in range(4 - i):# decrease space each row
        print(" ", end=" ")
    for k in range(2 * i + 1): # stars in 1, 3, 5, 7, 9
        print("*", end=" ")
    print() # move to next line