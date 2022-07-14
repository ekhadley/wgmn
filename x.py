import random, numpy as np

def choices(arr, n, out=[], head=True):
    if head:
        out = []
    out.append(arr)
    if len(arr) > n:
        for i, e in enumerate(arr):
            choices(np.delete(arr, i, 0), n, out, head=False)
    return np.unique([e for e in out if len(e) == n], axis=0)

a = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
b = np.array([1, 2, 3, 4, 5, 6])
c = np.array(['z', 'x', 'c', 'v', 'b', 'n'])

o = choices(a, 4)
print()
p = choices(b, 4)
print()
q = choices(c, 4)

print(o, len(o))
print(p, len(p))
print(q, len(q))