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


worldSize = 5
foodCount = 4
bombCount = 4

episodes = 100000
episodeLength = 15

e = dwarf.env(worldSize, foodCount, bombCount, episodeLength)
c = bond.agent(e, updateRate = 10, discount=.8,epsilon=.95,learnRate=.1)

c.memreq = 300
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






