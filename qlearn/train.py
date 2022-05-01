import time, dwarf, bond

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

a = []


avgReward = 0
avgEpTime = 0

worldSize = 4
foodCount = 1
bombCount = 1

episodes = 1000
episodeLength = 15

e = dwarf.env(worldSize, foodCount, bombCount, episodeLength)
c = bond.agent(e, updateRate = 10)
c.genModels(discount=.8,epsilon=.95,learnRate=.7)
c.memreq = 200
c.batchSize = 64

stime = time.time()
for i in range(1, episodes+1):
    e.reset()
    e.display()
    for j in range(0, e.epLen):
        e.display()
#        action, type = e.getUserAction()

        action, type = c.genAction(show=True)

        newState, stepReward = e.applyAction(action)
        c.remember([e.getObs(), action, stepReward, newState])
        c.train()

        #print(f"{action}: {type}")
        print(f"{bcolors.OKGREEN}Episode {i}, Step {e.step}   Last move reward: {stepReward}   Total episode reward: {e.episodeReward}{bcolors.OKBLUE}")

    if i*episodeLength > c.memreq:
        avgEpTime += time.time()-stime
        avgReward += e.episodeReward
        print(f"\033[91m\033[1mEp{i}: Average reward: {avgReward/i}, {(time.time()-stime)/i} seconds per episode")




