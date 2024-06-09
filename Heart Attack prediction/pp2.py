 """#finding the correlation coefficinet
            s_y,s2_y=0,0
            for l in range(len(m_B)):
                s_y+=m_B[l]
                s2_y+=m_B[l]**2
            
            E_Y=s_y/len(m_A)
            
            E_Y2=s2_y/len(m_A)
            
            sig_y=(E_Y2-(E_Y)**2)**0.5
            S=0
            for z in range(len(m_B)):
                S+=(m_A[z]-E_X)*(m_B[z]-E_Y)
                cov=S/len(m_B)
            print("Correlation coefficient between col","(",str(i),")","and","col","(",str(j),")","is:",cov/(sig_x*sig_y)) #correlation coefficient           """
