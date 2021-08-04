puzzles = [1]
for i in range(3, 131):
    puzzles.append(i)

while 1:
    new = int(input("which peice did you find?   "))
    try:
        puzzles.remove(new)
    except Exception:
        print('peice not found')
    print(f'you still need: {puzzles}')