import tensorflow as tf, time, random, dwarf, bond, numpy as np

worldSize = 10
foodCount = 15
bombCount = 15

episodes = 100
episodeLength = 25


e = dwarf.env(worldSize, foodCount, bombCount)
c = bond.agent(e)
c.genModels(disc=.99,eps=.8,ler=.01)

avgReward = 0
for i in range(0, episodes):
    time.sleep(1)
    e.show()


    action, type = c.genAction()
    prev = [r[:] for r in e]
    stepReward, newState = e.applyAction(action)
    c.remember([prev, action, stepReward, [r[:] for r in e.env]])

    print(f"{action}: {type}")
    print(f"\033[0m Step: {e.step}   Total episode reward: {e.episodeReward}   Last move reward: {stepReward}")
    if e.step > episodeLength:
        avgReward += e.reset()

avgReward /= episodes
print(avgReward)



