import math

##Ignore till line 24 ####
current = int(input("Amount of loops: "))

lis = []
vlt=[]

for x in range(current):
    lis.append(float(input("currnet: ")))
    vlt.append(float(input("voltage: ")))

print(lis)


avg_current=sum(lis)/len(lis)
print(avg_current)

avg_vlt=sum(vlt)/len(vlt)
print(avg_vlt)

Resistance=avg_vlt/avg_current

print("Resistance:",Resistance)


if (0.09<=Resistance<=0.1):
    print("1p")
if(0.04<=Resistance<=0.05):

    print("2p")
if(0.025<Resistance<=0.35):
    print("3p")
if(0.021<Resistance<=0.025):
    print("4p")
if(0.0167<Resistance<=0.021):
    print("5p")
if(0.01 <Resistance<=0.02):
    print("6p")
if(6.25> Resistance >=0.59):
    print("Voc")
if(Resistance> 6.25):
    print("error")