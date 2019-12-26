''' Attempt at Task 2 for Basketball'''
# here z_0 will be a guess for the z the ball goes through the hoop
# alp_0 will be a guess for the angle
# f_euler will be the function implemented by Mirjiam in order to solve
# N will be how ever many times we want divide the time sections into
def Guess_solv(z_0, alp_0, N):
    ''' This function will take in the guess for the angle and 
    and give you the position of the ball at z=z_0'''
    
    f_euler(f_vert, N, z_0) #Should give two lists one with vertical velocities V_y and z_0 grided
    f_euler(f_horizontal, N, z_0) #should give two lists one with horizontal velocities V_x and the same grided z_0 as before
    x=[x_0]
    y=[y_0]
    for i in range(0,N):
        x.append(V_x[i]*(z_0/N))
        y.append(V_y[i]*(z_0/N))
    return [x[-1], y[-1]]    
    
    
    