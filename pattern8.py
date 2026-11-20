for i in range(5):#run the loop 5 times
    for j in range(i): # spaces increase each row
        print(" ", end=" ")
    for k in range(9 - 2 * i): # stars decrease 9, 7, 5, 3, 1
        print("*", end=" ")
    print() # next line