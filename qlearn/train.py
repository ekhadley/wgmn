import tensorflow as tf, time, random, dwarf, bond, numpy as np

worldSize = 10
foodCount = 15
bombCount = 15

episodes = 100
episodeLength = 25


e = dwarf.env(worldSize, foodCount, bombCount)
c = bond.agent(disc=.9,eps=.2,lr=.9)

avgReward = 0
for i in range(0, episodes):
    e.show()
    r = e.applyMove(e.getUserMove())
    print(f"Step: {e.step}   Total episode reward: {e.episodeReward}   Last move reward: {r}")
    if e.step > episodeLength:
        avgReward += e.reset()

avgReward /= episodes
print(avgReward)