from matplotlib.pyplot import *
import numpy as np
import csv
with open(r"C:\Users\HP\Downloads\data set\heart_attack_prediction_dataset.csv",encoding='utf-8-sig') as csvfile:
    reader=csv.DictReader(csvfile)
    count=0
    smoking,alch,php=[],[],[]
    for row in reader:
        count+=1
        smoking.append(row['Smoking'])
        alch.append(row['Alcohol Consumption'])
        php.append(row['Previous Heart Problems'])
        #if count>1049:
        #    break
m_smoking,m_alcohol,m_php=[],[],[]
for i in range(len(smoking)):
    m_smoking.append(eval(smoking[i]))
    m_alcohol.append(eval(alch[i]))
    m_php.append(eval(php[i]))
x,y,F1,F2,s1,s2,s3,s4,s5,s6,s7,s8=0,28000,[],[],0,0,0,0,0,0,0,0
for j in range(len(m_smoking)): 
    if m_smoking[j]==0 and m_alcohol[j]==0 and m_php[j]==0:
        s1+=1
    elif m_smoking[j]==0 and m_alcohol[j]==0 and m_php[j]==1:
        s2+=1
    elif m_smoking[j]==0 and m_alcohol[j]==1 and m_php[j]==0:
        s3+=1
    elif m_smoking[j]==0 and m_alcohol[j]==1 and m_php[j]==1:
        s4+=1
    elif m_smoking[j]==1 and m_alcohol[j]==0 and m_php[j]==0:
        s5+=1
    elif m_smoking[j]==1 and m_alcohol[j]==0 and m_php[j]==1:
        s6+=1
    elif m_smoking[j]==1 and m_alcohol[j]==1 and m_php[j]==0:
        s7+=1
    else:
        s8+=1
F1=[s1,s2,s3,s4,s5,s6,s7,s8]
E1=[1,2,3,4,5,6,7,8]
print(F1)
#E is the list with people in different income range with previous heart problem
#F is the list with people in different income range with NO previous heart problem    

s_x,s_y,s2_x,s2_y=0,0,0,0
for i in range(len(E1)):
    s_x+=E1[i]
    s_y+=F1[i]
    s2_x+=E1[i]**2
    s2_y+=F1[i]**2
E_X=s_x/len(E1)
E_Y=s_y/len(F1)
E_X2=s2_x/len(E1)
E_Y2=s2_y/len(F1)
sig_x=(E_X2-(E_X)**2)**0.5
sig_y=(E_Y2-(E_Y)**2)**0.5
S=0
for j in range(len(E1)):
    S+=(E1[j]-E_X)*(F1[j]-E_Y)
cov=S/len(E1)
print("Covariance is:",cov)
print("Correlation coefficient is:",cov/(sig_x*sig_y)) #correlation coefficient
print("SD of X:",sig_x)
print("SD of Y:",sig_y)
print("average of X is:",sum(E1)/len(E1))
print("average if Y is:",sum(F1)/len(F1))

scatter(E1,F1,label="Total number of people with smoking and drinking habit with previous heart problems.")
xlabel("Habit of drinking smoking related to heart disease",color='black',size=15)
ylabel("Number of people",color='black',size=15)
#my_xticks = ['1','2','3','4','5','6','7','8']
#xticks(E1, my_xticks)
title('Number of people with drinking/smoking habit related to previous or NO previuos heart disease.',color='red',size=20)
legend()
z1 = np.polyfit(E1,F1, 1)
p1 = np.poly1d(z1)
plot(E1,p1(E1),"r-")
show()
