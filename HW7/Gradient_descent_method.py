# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 23:20:07 2020

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

def Armijobtls(x,y):
    alpha=1
    c1=10**(-4)
    theta=0.5
    x1,x2=x,y
    xk1=x1-alpha*gradient(x1,x2)[0]
    xk2=x2-alpha*gradient(x1,x2)[1]
    while function(xk1,xk2)>function(x1,x2)-c1*alpha*(gradient(x1,x2)[0]**2+gradient(x1, x2)[1]**2):
        alpha*=theta
        xk1=x1-alpha*gradient(x1,x2)[0]
        xk2=x2-alpha*gradient(x1,x2)[1]
    return alpha
    
def gradient_descent_method(x,y):
    Alpha=[]
    Gradient=[]
    result=[]
    x1,x2=x,y
    grad=gradient(x1,x2)
    c=max(abs(grad[0]),abs(grad[1]))
    while c>10**(-4):
        alpha=Armijobtls(x1,x2)
        Alpha.append(alpha)
        Gradient.append(c)
        result.append(function(x1,x2))
        x1-=alpha*grad[0]
        x2-=alpha*grad[1]
        grad=gradient(x1,x2)
        c=max(abs(grad[0]),abs(grad[1]))
    return (x1,x2),Alpha,Gradient,result
c,Alpha,Gradient,result=gradient_descent_method(1.2,1.2)
print(c)
n=[]
for i in range(len(Alpha)):
    n.append(i+1)
print(result)