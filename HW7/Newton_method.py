# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:07:20 2020

@author: duola
"""


from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist\
    
def function(x1,x2):
    return 100*(x2-x1**2)**2+(1-x1)**2

def gradient(x1,x2):
    return 200*(x2-x1**2)*(-2*x1)+2*(1-x1)*(-1),200*(x2-x1**2)

def hessian(x1,x2):
    return [[400*(3*x1**2-x2)+2,-400*x1],[-400*x1,200]]

def Armijobtls(x,y):
    alpha=1
    c1=10**(-4)
    theta=0.5
    x1,x2=x,y
    grad=gradient(x1,x2)
    hessi=np.mat(hessian(x1,x2)).I.tolist()
    xk1=x1-alpha*(hessi[0][0]*grad[0]+hessi[0][1]*grad[1])
    xk2=x2-alpha*(hessi[1][0]*grad[0]+hessi[1][1]*grad[1])
    while function(xk1,xk2)>function(x1,x2)-c1*alpha*((hessi[0][0]*grad[0]+hessi[0][1]*grad[1])*grad[0]+(hessi[1][0]*grad[0]+hessi[1][1]*grad[1])*grad[1]):
        alpha*=theta
        xk1=x1-alpha*(hessi[0][0]*grad[0]+hessi[0][1]*grad[1])
        xk2=x2-alpha*(hessi[1][0]*grad[0]+hessi[1][1]*grad[1])
    return alpha
    
def Newton_method(x,y):
    Alpha=[]
    Gradient=[]
    x1,x2=x,y
    grad=gradient(x1,x2)
    hessi=np.mat(hessian(x1,x2)).I.tolist()
    c=max(abs(grad[0]),abs(grad[1]))
    while c>10**(-4):
        alpha=Armijobtls(x1,x2)
        Alpha.append(alpha)
        Gradient.append(c)
        x1-=alpha*(hessi[0][0]*grad[0]+hessi[0][1]*grad[1])
        x2-=alpha*(hessi[1][0]*grad[0]+hessi[1][1]*grad[1])
        grad=gradient(x1,x2)
        c=max(abs(grad[0]),abs(grad[1]))
        hessi=np.mat(hessian(x1,x2)).I.tolist()
    return (x1,x2),Alpha,Gradient
c,Alpha,Gradient=Newton_method(-1.2,1)
n=[]
for i in range(len(Alpha)):
    n.append(i+1)
#plt.plot(n,Alpha)
plt.plot(n,Gradient)
plt.show()