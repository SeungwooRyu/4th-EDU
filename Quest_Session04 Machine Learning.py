#HW for Session 05: Machine Learning

#Way1
import csv
import pandas as pd
from scipy import optimize as op
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('C:\\Users\\승우\\Desktop\\caschool.csv', engine='python')

new = data[['read_scr', 'str', 'avginc']]


def beta(b):
    value = 0
    for i in range(0, len(new)):
        value += ((b[1]*new.iloc[i,1] + b[2]*new.iloc[i,2] + b[0] - new.iloc[i,0])**2) / (2*len(new))
        return value
    

result = op.minimize(beta, (2, 15, 18))
result



#Way 2
#HW for Session 05: Machine Learning
import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('C:\\Users\\승우\\Desktop\\caschool.csv', engine='python')
new = data[['read_scr', 'str', 'avginc']]

#cost function에는, 문제에서 제시했던대로 beta1, beta2, 상수의 순서대로, 하나의 리스트로 넣어줄 것

def cost(beta):
    value = 0
    for i in range(0, len(new)):
        value += ((beta[1]*new.iloc[i,1] + beta[2]*new.iloc[i,2] + beta[0] - new.iloc[i,0])**2) / (2*len(new))
        return value

def costd(beta) :
    J0 = 0
    J1 = 0
    J2 = 0
    for i in range(len(new)):
        J0 += (beta[1]*new.iloc[i,1] + beta[2]*new.iloc[i,2] - new.iloc[i,0]) / len(new)
    for i in range(len(new)):
        J1 += (beta[1]*new.iloc[i,1] + beta[2]*new.iloc[i,2] - new.iloc[i,0])*new.iloc[i,1] / len(new)
    for i in range(len(new)):
        J2 += (beta[1]*new.iloc[i,1] + beta[2]*new.iloc[i,2] - new.iloc[i,0])*new.iloc[i,2] / len(new)
    return [J0, J1, J2]
    
    
alpha = 0.005
ini = [3,10,15]
algo = [ini[1]-alpha*costd(ini)[1], ini[2]-alpha*costd(ini)[2],ini[0]-alpha*costd(ini)[0]]

def result(a, b):

    
    if (cost(b) > cost(a)):
        print ("Learning rate is too large")
    
    else:
        while(True):
            a = b
            b = [a[1]-alpha*costd(a)[1], a[2]-alpha*costd(a)[2], a[0]-alpha*costd(a)[0]]
            if (cost(a)-cost(b) < 0.005):
                break
                    
    return(a)
 
print(result(ini, algo), cost(result(ini, algo)))
    
