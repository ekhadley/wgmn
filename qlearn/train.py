import time, dwarf, bond


avgReward = 0
avgEpTime = 0

worldSize = 7
foodCount = 10
bombCount = 10

episodes = 1000
episodeLength = 10

e = dwarf.env(worldSize, foodCount, bombCount, episodeLength)
c = bond.agent(e, updateRate = 10)
c.genModels(discount=.8,epsilon=.8,learnRate=.1)
c.memreq = 20
c.batchSize = 16

stime = time.time()

for i in range(1, episodes+1):
    e.reset()
    e.show()
    for j in range(0, e.epLen):
#        time.sleep(1)
        e.show()
#        action, type = e.getUserAction()


        possibleRewards = []
        for m in [0, 1, 2, 3]:
            dontcare, r = e.simAction(m)
            possibleRewards.append(r)

        print(c.memories)

        optimalAction, type = c.genAction()
        newState, stepReward = e.applyAction(optimalAction)
        c.remember([e.getObs(), possibleRewards, newState])
        c.train()

        #print(f"{action}: {type}")
        print(f"\033[0mEpisode {i}, Step {e.step}   Last move reward: {stepReward}   Total episode reward: {e.episodeReward}")

    avgEpTime += time.time()-stime
    avgReward += e.episodeReward

    print(f"\033[91m\033[1mEp{i}: Average reward: {avgReward/i}, {(time.time()-stime)/i} seconds per episode")




