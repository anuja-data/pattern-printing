n = 5   # size of the pattern

for i in range(1, n + 1): # top half
    for j in range(i):   # left wing stars
        print("*", end=" ")
    for k in range(2 * (n - i)): # gap in the middle
        print(" ", end=" ")
    for j in range(i):  # right wing stars
        print("*", end=" ")
    print()

for i in range(n - 1, 0, -1):# bottom half
    for j in range(i):   # left wing stars
        print("*", end=" ")
    for k in range(2 * (n - i)): # gap in the middle
        print(" ", end=" ")
    for j in range(i):   # right wing stars
        print("*", end=" ")
    print()