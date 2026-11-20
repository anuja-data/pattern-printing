for i in range(5):# run the loop 5 times
    for j in range(i + 1):# columns increase with the row
        if j == 0 or j == i or i == 4:# left edge, right edge, last row
            print("*", end=" ")
        else:
            print(" ", end=" ")  # empty inside
    print() # next line