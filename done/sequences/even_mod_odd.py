import time, math, matplotlib.pyplot as plt
add = True
x = []
y = []
k = 0
even = 0
odd = 1
out = 0
cap = 300000

while k < cap:

    klist = list(str(k))
    for i in range(0, (len(klist))):
        klist[i] = int(klist[i])
        if (i%2) == 0:
            even += klist[i]
        if (i%2) > 0:
            odd += klist[i]
        out = even%odd
    x.append(k)    
    y.append(out)
    k += 1
    print(round((k/cap)*100, 3))



plt.plot(x, y)
plt.ylabel('dicks sucked (millions)')
plt.show()

"""
breaks up numbers into a list, and plots the remainder of
the division of the even indexed and odd indexed numbers
"""