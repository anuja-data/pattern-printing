for i in range(5):# run the loop 5 times
    for j in range(5):# columns
        if i == 0 or i == 4 or j == 0 or j == 4:# border only
            print("*", end=" ")
        else:
            print(" ", end=" ")  # empty inside
    print() #move to next line