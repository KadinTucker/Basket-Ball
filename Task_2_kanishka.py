''' Attempt at Task 2 for Basketball'''
# here z_0 will be a guess for the z the ball goes through the hoop
# alp_0 will be a guess for the angle
# N will be how ever many times we want divide the scaled time sections into
import numpy as np
import matplotlib.pyplot as plt
DIAMETER = 0.24 #Meters
MASS = 0.6 #Kilograms
AIR_RES_C = 0.45
AIR_DENSITY = 1.23 #kilogram / meter cubed
BASKET_HEIGHT = 3.05 #meters
PLAYER_DISTANT = 2.0 #meters
GRAVITY = 9.81 #Meters per second squared
k=(1/2)*AIR_DENSITY*AIR_RES_C*(DIAMETER**2)*(np.pi/4)

u=9#Initial velocity
x_0=0
y_0=1.75

def Guess_solv(z_0, alp_0, N):
    ''' This function will take in the guess for the angle and 
    and give you the position of the ball at z=z_0'''
    h=z_0/N
    t=[0]
    v_x=[u*np.cos(alp_0)]
    v_y=[u*np.sin(alp_0)]
    m=MASS
    g=GRAVITY
    for i in range(0,N-1):
        s=(v_x[i]**2+v_y[i]**2)**(1/2)
        t.append(t[i]+(h))
        v_x.append(v_x[i]-(h*k*s*v_x[i]*z_0)/m)
        v_y.append(v_y[i]-h*(k*s*v_y[i]+m*g)*z_0/m)
    x=[x_0]    
    y=[y_0]
    for i in range(0,N):
        x.append(x[i]+v_x[i]*(z_0/N))
        y.append(y[i]+v_y[i]*(z_0/N))
    return [x, y]    
    

    