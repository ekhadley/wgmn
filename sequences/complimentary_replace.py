import time, matplotlib.pyplot as plt, math
i = 0
x = []
y = []

while i < 9999:
    x.append(i)
    mag = 10**(len(str(i)))
    y.append((mag-i)**math.log2(10))
    i += 1
    print(mag-i)
    time.sleep(0)


print(y)
plt.plot(x, y)
plt.ylabel('dicks sucked (millions)')
plt.show()

'''
replaces every nonzero digit with its subtraction from 10 and outputs on the y axis
'''