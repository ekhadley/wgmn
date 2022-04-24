import tensorflow as tf, time, random, dwarf, bond, numpy as np

worldSize = 7
foodCount = 10
bombCount = 10

episodes = 14
episodeLength = 10


e = dwarf.env(worldSize, foodCount, bombCount)
c = bond.agent(e)
c.genModels(discount=.99,epsilon=.8,learnRate=.01, updateRate = 20)

avgReward = 0
avgEpTime = 0


for i in range(1, episodes+1):
    e.reset()
    e.show()

    c.updateModel()

    stime = time.time()
    for j in range(0, episodeLength):
#        time.sleep(1)
#        e.show()
        
        action, type = c.genAction()
#        action, type = e.getUserAction()
        currentState = e.getObs()
        newState, stepReward = e.applyAction(action)
        c.remember([currentState, action, stepReward, newState])

        c.train()

        print(f"{action}: {type}")
        print(f"\033[0mEpisode {i}, Step {e.step}   Total episode reward: {e.episodeReward}   Last move reward: {stepReward}")
    avgEpTime += time.time()-stime
    avgReward += e.episodeReward
    print(f"\033[91m\033[1mAverage reward: {avgReward/i}, {(time.time()-stime)/i} seconds per episode")



