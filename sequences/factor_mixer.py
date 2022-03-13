import matplotlib.pyplot as plt


def facto(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

def prod(factors): 
    result = 1
    for x in factors: 
         result = result * x  
    return result 

a = 0
y = []
x = []

while a < 1000:
    x.append(a)
    u = (prod(remove(facto(a))))
    y.append(u)
    print(u, a)
    a += 1


plt.plot(x, y)
plt.show()
'''
takes a number, splits it into a list of its prime factors, and removes the powers of each prime.
essentially brings every factor to the power 1
'''