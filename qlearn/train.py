import time, dwarf, bond

display = 1
showMoves = 1
showStats = 1
showMoveInfo = 0
recentAvgs = []
for i in range(0, 9):
    recentAvgs.append(0)

avgReward = 0
avgEpTime = 0

worldSize = 7
foodCount = 10
bombCount = 10

episodes = 1000
episodeLength = 10

e = dwarf.env(worldSize, foodCount, bombCount, episodeLength)
c = bond.agent(e, updateRate = 10)
c.genModels(discount=.99,epsilon=.8,learnRate=.01)

stime = time.time()

for i in range(1, episodes+1):
    e.reset()
    e.show()
    for j in range(0, e.epLen):
#        time.sleep(1)
#        e.show()
#        action, type = e.getUserAction()

        action, type = c.genAction()

        currentState = e.getObs()
        newState, stepReward = e.applyAction(action)
        c.remember([currentState, action, stepReward, newState])
        c.train()

        #print(f"{action}: {type}")
        #print(f"\033[0mEpisode {i}, Step {e.step}   Last move reward: {stepReward}   Total episode reward: {e.episodeReward}")

    avgEpTime += time.time()-stime
    avgReward += e.episodeReward
    recentAvgs.append(e.episodeReward)
    recentAvgs.pop(0)

    print(f"\033[91m\033[1mEp{i}: Average reward: {avgReward/i}, Average in last 10 episodes: {sum(recentAvgs)/len(recentAvgs)}{(time.time()-stime)/i} seconds per episode")




