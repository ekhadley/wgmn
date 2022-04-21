import cv2, random, numpy as np

foodReward = 10
bombPenalty = -25
movePenalty = -1


blankTile = 0
foodTile = 1
bombTile = 2
agentTile = 3


def makePlane(size, tile):
    row = []
    plane = []
    for i in range(0, size):
        row.append(tile)
    for i in range(0, size):
        plane.append(row.copy())
    return plane

def plant(arr, val, find):
    y = random.randint(0, len(arr)-1)
    x = random.randint(0, len(arr[y])-1)
    while(arr[y][x] != find):
        y = random.randint(0, len(arr)-1)
        x = random.randint(0, len(arr[y])-1)
    arr[y][x]=val
    return x, y

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

class env:
    def __init__(self, size, food, bomb, env = None):
        self.size=size
        self.food = food
        self.bomb = bomb
        self.moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.colorDict = {agentTile:bcolors.OKBLUE + bcolors.BOLD, 
                          blankTile:bcolors.ENDC, 
                          bombTile:bcolors.FAIL, 
                          foodTile:bcolors.OKGREEN}
        self.episodeReward = 0
        self.step = 0

        if not env:
            self.env = makePlane(size, blankTile)
            self.posx, self.posy = plant(self.env, agentTile, blankTile)
            for i in range(0, food):
                plant(self.env, foodTile, blankTile)
            for i in range(0, bomb):
                plant(self.env, bombTile, blankTile)
        else:
            self.env = env

    def reset(self):
        t = self.episodeReward
        self.env = makePlane(self.size, blankTile)
        self.episodeReward = 0
        self.step = 0
        self.posx, self.posy = plant(self.env, agentTile, blankTile)
        for i in range(0, self.food):
            plant(self.env, foodTile, blankTile)
        for i in range(0, self.bomb):
            plant(self.env, bombTile, blankTile)
        return t

    def get(self, x, y):
        return self.env[y][x]
    def set(self, x, y, val):
        self.env[y][x] = val

    def getUserAction(self):
        move = input("What direction would you like to move in? (W, A, S, D)\n").upper()
        map = ["D", "S", "A", "W"]
        while(move not in map):
            move = input("Not recognized, use W, A, S, D \n").upper()
        return map.index(move)

    def applyAction(self, move):
        moveReward = 0
        moveDirection = self.moves[move]
        self.step += 1

        self.set(self.posx, self.posy, blankTile)

        self.posx += moveDirection[0]
        self.posy += moveDirection[1]

        self.posx = self.size-1 if self.posx>=self.size else self.posx
        self.posx = 0 if self.posx<0 else self.posx
        self.posy = self.size-1 if self.posy>=self.size else self.posy
        self.posy = 0 if self.posy<0 else self.posy

        dest = self.get(self.posx, self.posy)

        if dest == foodTile:
            moveReward += foodReward
        if dest == bombTile:
            moveReward += bombPenalty
        moveReward += movePenalty

        self.set(self.posx, self.posy, agentTile)

        self.episodeReward += moveReward
        return self.env, moveReward

    def simAction(self, move):
        copyEnv = self.clone()
        return copyEnv.applyAction(move), copyEnv.env

    def clone(self):
        cp = env(self.size, self.food, self.bomb, env = [r[:] for r in self.env])
        cp.posx = self.posx
        cp.posy = self.posy
        return cp

    def show(self):
        colorEnv = self.env.copy()
        for i in range(len(colorEnv)):
            print()
            for j in range(len(colorEnv[i])):
                print(f"{self.colorDict[colorEnv[i][j]]}{colorEnv[i][j]}, ", end="")
        print(bcolors.BOLD + bcolors.WARNING)

    def display(self, windowSize):
        colors = {blankTile:np.array([0, 0, 0]), agentTile:np.array([200, 200, 100]), 
                  bombTile:np.array([250, 0, 40]), foodTile:np.array([200, 30, 0])}

        envArray = np.array(self.env)
        envArray = np.kron(envArray, np.ones((windowSize, windowSize)))
        rbgArray = np.zeros((self.size*windowSize, self.size*windowSize, 3))

        for i in range(0, self.size*windowSize):
            for j in range(0, self.size*windowSize):
                for k in colors:    
                    if envArray[i][j] == k:
                        rbgArray[i][j] = colors[k]
                        break

        cv2.imshow("game", rbgArray)
        cv2.waitKey(1)













































































