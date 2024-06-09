from matplotlib.pyplot import *
import numpy as np
import csv
with open(r"C:\Users\HP\Downloads\data set\heart_attack_prediction_dataset.csv",encoding='utf-8-sig') as csvfile:
    reader=csv.DictReader(csvfile)
    count=0
    age,gender,chol,famhist,smoking,alch,BMI,Continent,Diet,AA,obesity,income,php,bp=[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    for row in reader:
        count+=1
        age.append(row['Age'])
        gender.append(row['Sex'])
        chol.append(row['Cholesterol'])
        famhist.append(row['Family History'])
        smoking.append(row['Smoking'])
        alch.append(row['Alcohol Consumption'])
        BMI.append(row['BMI'])
        Continent.append(row['Continent'])
        Diet.append(row['Diet'])
        AA.append(row['Heart Attack Risk'])
        obesity.append(row['Obesity'])
        income.append(row['Income'])
        php.append(row['Previous Heart Problems'])
        bp.append(row['Blood Pressure'])
        #if count>1049:
        #    break
m_income,m_php=[],[]
for i in range(len(income)):
    m_income.append(eval(income[i]))
    m_php.append(eval(php[i]))
x,y,F1,F2,s1,s2=0,28000,[],[],0,0
for i in range(11):
    for j in range(len(m_income)):
        if x<=m_income[j]<y and m_php[j]==0:
            s1+=1
    F1.append(s1)
    s1=0
    x+=28000
    y+=28000
x1,y1,E1,E2,ss1=0,28000,[],[],1
for i in range(11):
    for k in range(len(m_income)):
        if x1<=m_income[k]<y1 and m_php[k]==1:
            s2+=1
    E1.append(s2)
    E2.append(ss1)
    ss1+=1
    s2=0
    x1+=28000
    y1+=28000
#E is the list with people in different income range with previous heart problem
#F is the list with people in different income range with NO previous heart problem    
    
"""print(E1)
print(F1)
print(E2)
print(sum(F1)+sum(E1))"""

s_x,s_y,s2_x,s2_y=0,0,0,0
for i in range(len(E2)):
    s_x+=E2[i]
    s_y+=E1[i]
    s2_x+=E2[i]**2
    s2_y+=E1[i]**2
E_X=s_x/len(E1)
E_Y=s_y/len(E2)
E_X2=s2_x/len(E2)
E_Y2=s2_y/len(E1)
sig_x=(E_X2-(E_X)**2)**0.5
sig_y=(E_Y2-(E_Y)**2)**0.5
S=0
for j in range(len(E2)):
    S+=(E2[j]-E_X)*(E1[j]-E_Y)
cov=S/len(E2)
print("Covariance is:",cov)
#print("Correlation coefficient is:",cov/(sig_x*sig_y)) #correlation coefficient
print("standard deviation of X1:",sig_x)
print("standard deviation of Y1:",sig_y)

s_x,s_y,s2_x,s2_y=0,0,0,0
for i in range(len(E2)):
    s_x+=E2[i]
    s_y+=F1[i]
    s2_x+=E2[i]**2
    s2_y+=F1[i]**2
E_X=s_x/len(F1)
E_Y=s_y/len(E2)
E_X2=s2_x/len(E2)
E_Y2=s2_y/len(F1)
sig_x=(E_X2-(E_X)**2)**0.5
sig_y=(E_Y2-(E_Y)**2)**0.5
S=0
for j in range(len(E2)):
    S+=(E2[j]-E_X)*(F1[j]-E_Y)
cov=S/len(E2)
print("average of X1:",sum(E2)/len(E2))
print("average of Y1:",sum(E1)/len(E2))
print("average of Y2:",sum(F1)/len(E2))

print("Covariance is:",cov)
#print("Correlation coefficient is:",cov/(sig_x*sig_y)) #correlation coefficient
print("standard deviation of X2:",sig_x)
print("standard deviation of Y2:",sig_y)
print('\n')
print("Previous heart problem:",E1,sum(E1))
print("No previous heart problem:",F1,sum(F1))


scatter(E2,E1,label="Total number of people falling in different income range with previous heart problems.")
scatter(E2,F1,label="Total number of people falling in different income range with NO previous heart problems.")
xlabel("Income range(in Lakh)",color='black',size=15)
ylabel("Number of people",color='black',size=15)
my_xticks = ['<0.28','0.28-0.56','0.56-0.84','0.84-1.12','1.12-1.4','1.4-1.68','1.68-1.96','1.96-2.24','2.24-2.52','2.52-2.80','>2.80']
xticks(E2, my_xticks)
title('Number of people of different income range with previous or NO previuos heart disease.',color='red',size=20)
legend()
z1 = np.polyfit(E2,E1, 1)
p1 = np.poly1d(z1)
#plot(E2,p1(E2),"r-")
z2 = np.polyfit(E2,F1, 1)
p2 = np.poly1d(z2)
#plot(E2,p2(E2),"r-")
show()
