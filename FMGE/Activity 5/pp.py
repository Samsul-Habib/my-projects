from matplotlib.pyplot import *
import numpy as np
import csv
with open(r"C:\Users\HP\Downloads\data set\universal_top_spotify_songs.csv",encoding='utf-8-sig') as csvfile:
    reader=csv.DictReader(csvfile)
    count=0
    pop=[]
    for row in reader:
        count+=1
        pop.append(row['popularity'])
        #if count>500:
        #   break
#print(pop)
print("\n")
A={}
for i in range(1,11):
    s=0
    for j in range(len(pop)):
        if pop[j]==str(i):
            s+=1
    A[i]=s
print(A)
print(sum(A.values()))
#print(A.values())
K=list(A.keys())
V=list(A.values())
MM=[]
for i in range(len(V)):
    """MM.append(V[i]/sum(V))
    print("P(X=",K[i],")is:",V[i]/sum(V))"""
    MM.append(V[i]/sum(V))
    print("P(X=",K[i],")is:",MM[i])

print(sum(MM))
final,MM2=[],[]
import math
n=10
def ff(n,r):
    return (math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))
for i in range(len(MM)):
    x=1/K[i]
    y=(math.factorial(n-K[i])*math.factorial(K[i]))/math.factorial(n)
    z=y*MM[i]
    a=math.log(z,math.exp(1))
    b=x*a
    c=math.exp(b)
    final.append(c)
    MM2.append(ff(n,K[i])*((0.5645)**K[i])*(1-0.5645)**(n-K[i]))
print(final)
avg=sum(final)/len(final)
print(avg)

import matplotlib.pyplot as plt
plt.plot(K,[0.00301,0.0204,0.053,0.1476,0.2095,0.2567,0.1789,0.092,0.031,0.00276],color='red',label='Estimated probability')
plt.plot(K,MM2,color='blue',label='Probability calculated using Binomial Distribution')
plt.xlabel("X",color='black',size=20)
plt.ylabel("P(X)",color='black',size=20)
plt.legend()
plt.show()
