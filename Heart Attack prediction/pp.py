from matplotlib.pyplot import *
import numpy as np
import csv
sgg=0
with open(r"C:\Users\HP\Downloads\data set\heart_attack_prediction_dataset.csv",encoding='utf-8-sig') as csvfile:
    reader=csv.DictReader(csvfile)
    for i in range(1,5):
        count,A=0,[]
        for row in reader:  
        
            count+=1
            A.append(row[str(i)])
            if count>20:
                break
        m_A=[]
        for b in range(len(A)):
            m_A.append(eval(A[b]))
        s_x,s2_x=0,0
        for l in range(len(m_A)):
            
            s_x+=m_A[l]
            s2_x+=m_A[l]**2
        E_X=s_x/len(m_A)
        E_X2=s2_x/len(m_A)
        sig_x=(E_X2-(E_X)**2)**0.5
        for j in range(1,5):
            c,B=0,[]
            if j!=i:
                for row in reader:
                    c+=1
                    
                    B.append(row[str(j)])
                    if c>20:
                        break
            m_B =[]
            for k in range(len(B)):
                m_B.append(eval(B[k]))
            print(m_A)
            print(m_B)
            sgg+=1
            print("\n")
print(sgg)
           
