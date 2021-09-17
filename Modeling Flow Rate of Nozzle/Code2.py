from matplotlib import pyplot as plt
import math
import numpy as np


a=1/4
b=(math.pi)

# velocity/speed of nozzel flow 30mm/s
vel=np.array([30,35,40,45,50,55,60]) 

# diameter of nozzle in mm
dia = np.array([0.25,0.30,0.4,0.5,0.6,0.8,1])  

x=[]
def flowcal(c,d):
  for i in c:
     flow= a*b*((i)**2)*d
     x.append(flow)


flowcal(dia,vel) 
plt.title("Flow rate for different nozzle")
plt.ylabel("fluid flow in cmm/sec")
plt.xlabel("Nozel diameter mm")


plt.plot(dia,x,)
plt.legend(["30 velocity/speed","35 velocity/speed","40 velocity/speed","45 velocity/speed",
            "50 velocity/speed","55 velocity/speed","60 velocity/speed"], loc="best", fontsize="small")

print(dia)

plt.grid()
plt.show()
