import matplotlib.pyplot as plt
import numpy as np

voltages = []
index = []
while 1:
    try:
        lim = int(input("How many values would you like to read?: "))
        for i in range(1, lim):
            f = open("Circuit_Simulation" + str(i) + ".txt", "r")
            for j in f:
                if "voltage=" in j:
                    voltages.append(float(j[8:].strip()))
            index.append(i)
        plt.plot(index, voltages)
        plt.show()
        break
    except ValueError:
        print("invalid input, try again")
        lim = input("How many values would you like to read?: ")
        try:
            lim = int(lim)
        except:
            print("invalid input, try again")















































































