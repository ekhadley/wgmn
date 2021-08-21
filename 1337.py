board=[["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]]

def dupes(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] == l[j] and i != j:
                return True
    return False

found = []
for i in range(1,10):
    found.append([[], []])
for i in range(len(board)):
    for j in range(len(board)):
        if board[j][i] != '.':
            found[int(board[j][i])-1][0].append([i+1])
            found[int(board[j][i])-1][1].append([j+1])

for i in range(len(found)):
    if dupes(found[i][0]) or dupes(found[i][1]):
        print('invalid')
        break
#    for j in range(len(found[i][0])):
