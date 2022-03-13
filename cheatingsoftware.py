import random

choices = ['a', 'b', 'c', 'd', 'e']

for i in range(0, 49):
    ans = []
    for j in range(0, 3):
        if random.random() > .35:
            ans.append(choices[j])
    if len(ans) == 0:
        ans = ['e']

    print(ans)