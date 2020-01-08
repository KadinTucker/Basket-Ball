# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 11:32:19 2020
@author: Victor Alphonce
"""
from  scipy import *
from  matplotlib.pyplot import *

#x and y are lists of 2D vectors with z and a(a = alpha)
#N is the number of iterations
#xdz,xda,ydz,yda are the derivate functions of x and y respectively, over z and a respectively

def temp(x,y,z0,a0,xB,yB,N=200,tol=1e-5):
    G0 = [x[0],y[0]] #a 2D vector of the first items of the lists of the 2D vectors
    DG=[[xdz(z0),xda(a0)],[ydz(z0),yda(a0)]] #Jacobian Matrix of the derivatives when the variables = 0
    step_size=-G0*linalg.inv(DG) #the stepsize
    for i in range(N):
        x.append(x[i]+dj[0])
        if abs(xB-x[i+1])<tol: #when x->xB break
            break
    for i in range(N):
        y.append(y[i]+dj[1])
        if abs(yB-y[i+1])<tol: #when y->yB break
            break
    if abs(xB-x[-1])>tol or abs(yB-y[-1])>tol:
        raise Exception("It did not reach the tolerance, try a higher N.")
    return(x[-1],y[-1])

#ToDo: error checking
