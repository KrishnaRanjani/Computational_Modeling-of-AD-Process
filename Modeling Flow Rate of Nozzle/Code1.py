from matplotlib import pyplot as plt
import math
import numpy as np

#parameters

a=1/4
b=(math.pi)

# velocity/speed of nozzel flow 30mm/s
vel=30 

# diameter of nozzle in mm
dia = np.array([0.25,0.30,0.35,0.4,0.5,0.6,0.8,1])  


x=[]
def flowcal(c,d):
  for i in c:
    flow= a*b*((i)**2)*vel
    x.append(flow)
  print(x)   
  
y =(flowcal(dia,vel)) 

plt.title("Flow rate for different nozele")
plt.ylabel("fluid flow in cmm/sec")
plt.xlabel("Nozel diameter mm")

plt.plot(dia,x, label= "Fluid flow in velocity speed of"+  "30" +"mm/s")
plt.legend(loc="best", fontsize="small")

plt.grid()
plt.show()
