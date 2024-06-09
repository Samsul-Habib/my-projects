from matplotlib.pyplot import *
import numpy as np
import csv
with open(r"C:\Users\HP\Downloads\data set\heart_attack_prediction_dataset.csv",encoding='utf-8-sig') as csvfile:
    reader=csv.DictReader(csvfile)
    count=0
    age,gender,chol,famhist,smoking,alch,BMI,Continent,Diet,AA,obesity,income,ex=[],[],[],[],[],[],[],[],[],[],[],[],[]
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
        ex.append(row['Exercise Hours Per Week'])
        if count>2000:
            break
m_chol, m_ex =[],[]
for i in range(len(chol)):
    m_chol.append(eval(chol[i]))
    m_ex.append(eval(ex[i]))
for i in range(len(m_chol)-1):
    for j in range(len(m_chol)-1):
        if m_ex[j]>=m_ex[j+1]:
            temp1=m_ex[j]
            m_ex[j]=m_ex[j+1]
            m_ex[j+1]=temp1
            temp2=m_chol[j]
            m_chol[j]=m_chol[j+1]
            m_chol[j+1]=temp2

#finding the correlation coefficinet
s_x,s_y,s2_x,s2_y=0,0,0,0
for i in range(len(m_ex)):
    s_x+=m_ex[i]
    s_y+=m_chol[i]
    s2_x+=m_ex[i]**2
    s2_y+=m_chol[i]**2
E_X=s_x/len(m_ex)
E_Y=s_y/len(m_ex)
E_X2=s2_x/len(m_ex)
E_Y2=s2_y/len(m_ex)
sig_x=(E_X2-(E_X)**2)**0.5
sig_y=(E_Y2-(E_Y)**2)**0.5
S=0
for j in range(len(m_ex)):
    S+=(m_ex[j]-E_X)*(m_chol[j]-E_Y)
cov=S/len(m_ex)
print("Correlation coefficient is:",cov/(sig_x*sig_y)) #correlation coefficient
    
scatter(m_ex,m_chol)
show()
            

