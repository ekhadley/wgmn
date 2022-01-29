import random

choices = ['a', 'b', 'c', 'd', 'e']

for i in range(0, 49):
    ans = []
    for j in range(0, 4):
        if random.random() > .5:
            ans.append(choices[j])
        if ans[:-1] == 'e' or len(ans) == 0:
            ans = ['e']
    print(ans)