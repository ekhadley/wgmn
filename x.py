from asyncio import transports
import random, numpy as np

class connect4:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.board = [['.' for j in range(0, 6)] for i in range(0, 7)]
        self.movenum = 0
        self.live = True

    def move(self, player, col):
        for i, e in enumerate(self.board[col-1]):
            if e == '.':
                if player == self.p1:
                    self.board[col-1][i] = 'x'
                if player == self.p2:
                    self.board[col-1][i] = 'o'
                self.movenum += 1
                break

    def show(self):
        rep = ''
        t = np.ndarray.tolist(np.transpose(self.board))
        t.reverse()
        for i in t:
            for j in i:
                rep += j + ' '
            rep += '\n'
        return rep

    def checkEnd(self):
        p1pos, p2pos = [], []
        for i, e in enumerate(self.board):
            for j, f in enumerate(e):
                if f == 'x':
                   p1pos.append([i, j])
                if f == 'o':
                    p2pos.append([i, j]) 

        for i in self.board:
            if sublist(i, ['x', 'x', 'x', 'x']):
                return 1
            if sublist(i, ['o', 'o', 'o', 'o']):
                return 2
        for i in np.ndarray.tolist(np.transpose(self.board)):
            if sublist(i, ['x', 'x', 'x', 'x']):
                return 1
            if sublist(i, ['o', 'o', 'o', 'o']):
                return 2
        for i in diags(self.board):
            if sublist(i, ['x', 'x', 'x', 'x']):
                return 1
            if sublist(i, ['o', 'o', 'o', 'o']):
                return 2
        o = [e[:] for e in self.board]
        [e.reverse() for e in o]
        for i in diags(o):
            if sublist(i, ['x', 'x', 'x', 'x']):
                return 1
            if sublist(i, ['o', 'o', 'o', 'o']):
                return 2
        

def sublist(a, b):
    for i in range(0, len(a)-len(b)+1):
        if a[i:i+len(b)] == b:
            return True
    return False

def diags(a):
    n = len(a[0]) + len(a) - 1
    b = [np.ndarray.tolist(np.diag(a, k=i)) for i in range(-n, n)]
    return [e for e in b if e != []]


g = connect4('e', 'k')
for i in range(0, 15):
    g.move('e', random.randint(1, 7))
    g.move('k', random.randint(1, 7))

[print(e) for e in g.board]
print(g.show())
