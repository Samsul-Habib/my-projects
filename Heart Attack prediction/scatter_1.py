from matplotlib.pyplot import *
import numpy as np
import csv
with open(r"C:\Users\HP\Downloads\data set\heart_attack_prediction_dataset.csv",encoding='utf-8-sig') as csvfile:
    reader=csv.DictReader(csvfile)
    count=0
    age,gender,chol,famhist,smoking,alch,BMI,Continent,Diet,AA,obesity,php,hs=[],[],[],[],[],[],[],[],[],[],[],[],[]
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
        php.append(row['Previous Heart Problems'])
        #if count>20:
        #    break
m_gender=[]
m_diet=[]
m_BMI=[]
m_php,m_AA=[],[]
for i in BMI:
    m_BMI.append(eval(i))
for k in gender:
    if k=='Male':
        k=1         #1 for Male
        m_gender.append(k)
    elif k=='Female':
        k=0         #0 for female
        m_gender.append(k)
for i in Diet:
    if i=='Average':
        i=1
        m_diet.append(i)
    elif i=='Healthy':
        i=2
        m_diet.append(i)
    else:
        i=0
        m_diet.append(i)
m_famhist=[]
AS,AS1=0,0
for i in range(len(php)):
    m_AA.append(eval(AA[i]))
    m_php.append(eval(php[i]))
    if m_AA[i]==1:
        AS+=1
    if m_php[i]==1:
        AS1+=1
print("Total number of people with Heart Attack risk:",(AS/len(AA))*100)
print("Total number of people with previuos heart attack problems:",(AS1/len(AA))*100)
    
    
m_chol=[]
for i in chol:
    m_chol.append(eval(i))
m_obes=[]
for i in obesity:
    m_obes.append(eval(i))
s1,s2,s3,s4,s5,s6,s7,s8=0,0,0,0,0,0,0,0
for i in range(len(m_BMI)):
    if m_BMI[i]<18.5 and m_chol[i]<=200:
        s7+=1
    elif m_BMI[i]<18.5 and m_chol[i]>200:
        s8+=1
    elif 18.5<=m_BMI[i]<=24.9 and m_chol[i]<=200:
        s1+=1
    elif 18.5<=m_BMI[i]<=24.9 and m_chol[i]>200:
        s2+=1
    elif 25<=m_BMI[i]<=29.9 and m_chol[i]<=200:
        s3+=1
    elif 25<=m_BMI[i]<=29.9 and m_chol[i]>200:
        s4+=1
    elif m_BMI[i]>=30 and m_chol[i]<=200:
        s5+=1
    else:
        s6+=1
print("Underweight(BMI<18.5) person with normal cholesterol:",s7)
print("Underweight person with high cholesterol:",s8) 
print("Person with normal weight(BMI 18.5 to 24.9) and normal cholesterol(<=200 mg/dL):",s1)
print("Person with normal weight and high cholesterol(>200 mg/dL):",s2)
print("Person with overwieght(BMI 25 to 29.9) and normal cholesterol(<=200 mg/dL):",s3)
print("Person with overweight and high cholesterol(>200 mg/dL):",s4)
print("Obes person (BMI>30) with Normal cholesterol(<=200 mg/dL):",s5)
print("Obes person with high cholesterol(>200 mg/dL):",s6)
Y=[s7,s8,s1,s2,s3,s4,s5,s6]
X=[1,2,3,4,5,6,7,8]

s_x,s_y,s2_x,s2_y=0,0,0,0
for i in range(len(X)):
    s_x+=X[i]
    s_y+=Y[i]
    s2_x+=X[i]**2
    s2_y+=Y[i]**2
E_X=s_x/len(X)
E_Y=s_y/len(Y)
E_X2=s2_x/len(X)
E_Y2=s2_y/len(X)
sig_x=(E_X2-(E_X)**2)**0.5
sig_y=(E_Y2-(E_Y)**2)**0.5
S=0
for j in range(len(X)):
    S+=(X[j]-E_X)*(Y[j]-E_Y)
cov=S/len(X)
print("Covariance is:",cov)
print("Correlation coefficient is:",cov/(sig_x*sig_y)) #correlation coefficient
print("\n")
print("average number of people:",sum(Y)/8)
print("average BMI/Cholesterol range:",sum(X)/8)
print("standard deviation of BMI/Cholesterol range:",sig_x)
print("stnadard deviation of total number of people:",sig_y)
print(Y)
print(X)

xlabel("BMI and Cholesterol group",color='black',size=20)
ylabel("Number of person",color='black',size=20)
title("Number of person vs. BMI and Cholesterol group",color='red',size=30)
scatter(X[0],Y[0],label='underweight(BMI<18.5) person with normal cholesterol(<=200)')
scatter(X[1],Y[1],label='underweight(BMI<18.5) person with high cholesterol(>200)')
scatter(X[2],Y[2],label='normal weight(18.5<=BMI<=24.9) person with normal cholesterol(<=200)')
scatter(X[3],Y[3],label='normal weight(18.5<=BMI<=24.9) person with high cholesterol(>200)')
scatter(X[4],Y[4],label='overweight(25<=BMI<=30) person with normal cholesterol(<=200)')
scatter(X[5],Y[5],label='overweight person(25<=BMI<=30) with high cholesterol(>200)')
scatter(X[6],Y[6],label='obes(BMI>30) person with normal cholesterol(<=200)')
scatter(X[7],Y[7],label='obes(BMI>30) person with high cholesterol(>200)')
z = np.polyfit(X, Y, 1)
p = np.poly1d(z)
plot(X,p(X),"r-")
legend()
show()

