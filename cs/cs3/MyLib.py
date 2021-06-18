
def copylist(a):
    z = [e for e in a]
    for i in range(len(a)):
        z[i] = [e for e in a[i]]
    return z

def sameSize(a, b):
    try:
        if len(a) == len(b):
            for i in range(len(a)):
                if len(a[i]) != len(b[i]):
                    return False
            return True
        else:
            return False
    except:
        return False

def multlist(a, b):
    try:
        l = len(a) if len(a)>len(b) else len(a) if len(a)==len(b) else len(b)
        o = []
        x = 0
        for i in range(l):
            o.append(a[i]*b[i])
        for i in o:
            x += i
        return x
    except:
        return "improper types"

def isEqual(a, b):
    if a == b:
        return True
    else:
        return False
    return 'cannot be evaluated'

def add_Mat(a, b):
    try:
        if sameSize(a, b):
            z = copylist(a)
            for i in range(len(a)):
                for j in range(len(a[i])):
                    z[i][j] += b[i][j]
            return z
        else:
            return "nonexistent result"
    except:
        return "unsupported types"

def sub_Mat(a, b):
    try:
        if sameSize(a, b):
            z = copylist(a)
            for i in range(len(a)):
                for j in range(len(a[i])):
                    z[i][j] -= b[i][j]
            return z
        else:
            return "nonexistent result"
    except:
        return "unsupported types"

def scale_Mat(a, s):
    z = copylist(a)
    try:
        for i in range(len(z)):
            for j in range(len(z[i])):
                z[i][j] *= s
        return z
    except:
        return "unsupported types, or switch parameters"

def trace_Mat(a):
    x = 0
    i = 0
    try:
        while 1:
            x += a[i][i]
            i += 1
    except IndexError:
        return x

def trans_Mat(a):
    z = copylist(a)
    try:
        for i in range(len(z)):
            for j in range(len(z[i])):
                z[i][j] = a[j][i] 
        return z
    except IndexError:
        return "improper matrix"

def calc_det(a):
    square2 = [[0, 0],[0, 0]]
    square3 = [[0,0,0],[0,0,0],[0,0,0]]
    try:
        if sameSize(a, square2):
            det = a[0][0]*a[1][1] - a[0][1]*a[1][0]
            return det
        if sameSize(a, square3):
            det = a[0][0]*(a[1][1]*a[2][2] - a[1][2]*a[2][1]) - a[0][1]*(a[1][0]*a[2][2] - a[1][2]*a[2][0]) + a[0][2]*(a[1][0]*a[2][1] - a[1][1]*a[2][0])
            return det
        else:
            return "square matrices only"
    except IndexError:
        return "unsupported types"


def cmult_Mat(a, b):
    try:
        cprod = [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]
        return cprod
    except:
        return 'improper list size for cross product operation'

def dmult_Mat(a, b):
    try:
        z = trans_Mat(copylist(b))
        p = copylist(a)
        if sameSize(a, b):
            for i in range(len(a)):
                for j in range(len(a[i])):
                    p[i][j] = multlist(a[i], z[j])
            return p
        else:
            return "different size matrices not supported"
    except IndexError:
        return "unsupported types"

def inv_Mat(a):
    return "¯\_(ツ)_/¯"

t = [[1,   2,  3, 4],
     [5,  6,  7,  8],
     [9, 10, 11, 12]]

p = [[1, 2],
     [3, 4]]

a = [[25, 54, 17],
     [23, 45, 2],
     [15, 34, 51]]

b = [[3, 96, 31],
     [46, 57, 24],
     [32, 92, 27]]










































