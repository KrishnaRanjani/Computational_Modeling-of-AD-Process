from matplotlib import pyplot as plt
import math

# Density of the PLA
rho = 1240

# Kinematic viscosity of PLA
nu = 4

# Returns pressure drop Pa/m
# Reynolds' number tells us which expression to use in the two different scenarios
# v velocity of the fluid
# D pipes' diameter
def pressureDrop(v,D):
    Re = (v*D)/nu

    if Re < 2000:
        print("Laminar flow",v,D)
        Fa = 64/Re
    else:
        print("Turbolent flow")
        Fa = 0.316 * math.pow(Re,-0.25)

    r = Fa*(1/D)*rho*math.pow(v,2)/2
    return r


pressDropv = {}

diaPipe = []
veloc = []

v = 0.001
d = 0.1

while v < 0.025:
    veloc.append(v)
    v += 0.005
while d < 1.00:
    diaPipe.append(d)
    d += 0.1


pressDropd = {}
pressDropv = {}

for i in veloc:
    pressDropv[i] = list()
    for j in diaPipe:
        pressDropv[i].append(pressureDrop(i,j))


def plotAllDia():
    try:
        x = diaPipe
        plt.title("Pressure drops given a fixed fluid velocity")
        plt.ylabel("Pressure drop Pa/m")
        plt.xlabel("Nozel diameter mm")
        for v in veloc:
            y =  pressDropv[v]
            plt.plot(x,y,label="Fluid velocity "+str(v)+" m/s")
        plt.legend(loc="best", fontsize="small")
        plt.grid()
        
        plt.show()

    except Exception as e:
        print(e)


plotAllDia()
