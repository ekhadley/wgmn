def crosser(a, b, c, x, y, z):
    first = b*z-c*y
    second = c*x-a*z
    third = a*y-b*x
    print(str(first) + ', ' + str(second) + ', ' + str(third))

crosser(6, 0, 0, 3, 9, 6)