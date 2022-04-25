import tensorflow as tf, time, random, dwarf, bond, numpy as np

worldSize = 7
foodCount = 10
bombCount = 10

episodes = 14
episodeLength = 10


e = dwarf.env(worldSize, foodCount, bombCount)
c = bond.agent(e, episodeLength = episodeLength, updateRate = 10)
c.genModels(discount=.99,epsilon=.8,learnRate=.01, updateRate = 20)

avgReward = 0
avgEpTime = 0

stime = time.time()
for i in range(1, episodes+1):
    e.reset()
    e.show()
    for j in range(0, e.episodeLength):
#        time.sleep(1)
#        e.show()
#        action, type = e.getUserAction()

        action, type = c.genAction()

        currentState = e.getObs()
        newState, stepReward = e.applyAction(action)
        c.remember([currentState, action, stepReward, newState])
        c.train()

        print(f"{action}: {type}")
        print(f"\033[0mEpisode {i}, Step {e.step}   Last move reward: {stepReward}   Total episode reward: {e.episodeReward}")

    avgEpTime += time.time()-stime
    if j>10:
        avgReward += e.episodeReward
    print(f"\033[91m\033[1mAverage reward: {avgReward/i}, {(time.time()-stime)/i} seconds per episode")



