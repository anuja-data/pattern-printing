for i in range(5): # top half
    for j in range(4 - i):# spaces decrease
        print(" ", end=" ")
    for k in range(2 * i + 1):# stars increase
        print("*", end=" ")
    print()

for i in range(4):# bottom half
    for j in range(i + 1): # spaces increase
        print(" ", end=" ")
    for k in range(7 - 2 * i):# stars decrease 7, 5, 3, 1
        print("*", end=" ")
    print()