import constants
import math
import matplotlib.pyplot as plt
import numpy as np

#Defining the 'air resistance constant', compiling all of the constants that affect the force of drag on our basketball
AIR_RES_CONSTANT = constants.AIR_DENSITY * constants.AIR_RES_C * math.pi * constants.DIAMETER * constants.DIAMETER / 8.0

def get_euler_solution(derivative, numsteps, upper, initial):
    """
    Returns an explicit Euler's method solution to a given differential equation,
    called `derivative`, of the form dy/dx = f(x, y)
    Can operate on numpy vectors
    Runs with `numsteps` iterations, from x = 0 to x = `upper`
    Uses `initial` as the initial value for y
    """
    inputs = [0]
    outputs = [initial]
    delta = float(upper) / numsteps
    for i in range(1, numsteps):
        inputs.append(inputs[i-1] + delta)
        outputs.append(outputs[i-1] + delta * derivative(inputs[i-1], outputs[i-1]))
    return inputs, outputs

def generate_function(inputs, outputs):
    """
    Creates afunction from a numeric approximation thereof
    Accesses the output at an input value nearest to the corresponding input values
    The function generated is effectively a function of only x, but has y as a dummy parameter
    Assumes a linearly increasing sequence `inputs`
    """
    def function(x, y=None):
        try:
            return outputs[int(x / (inputs[-1] - inputs[0]) * len(inputs))]
        except:
            raise ValueError("input not in domain of inferred function")
    return function

def air_res(speed):
    """
    Returns the magnitude of air resistance force based on the absolute speed of a moving object
    """
    return AIR_RES_CONSTANT * speed * speed

def get_acceleration(time, velocity):
    """
    Gets the instantaneous acceleration 
    at the given time and velocity of a moving object
    Takes velocity as a two-dimensional vector
    """
    speed = math.hypot(velocity[0], velocity[1])
    angle = math.acos(velocity[0] / speed)
    return np.array([-air_res(speed) * math.cos(angle) / constants.MASS,
            -air_res(speed) * math.sin(angle) / constants.MASS - constants.GRAVITY])

def solve_boundary_problem(endtime, launch_angle, num_iterations):
    """
    Solves the boundary value problem explicitly
    First obtains an Euler's method solution giving the velocity vectors at each time step,
    then obtains an Euler's method solution for the positions given the velocity vectors
    Returns a list of x values and y values, ready for plotting
    """
    times, velocities = get_euler_solution(get_acceleration, num_iterations, endtime, 
            np.array([math.cos(launch_angle) * constants.LAUNCH_SPEED, math.sin(launch_angle) * constants.LAUNCH_SPEED]))
    times, positions = get_euler_solution(generate_function(times, velocities), num_iterations, endtime, np.array([constants.PLAYER_WIDTH, constants.PLAYER_WIDTH]))
    return unpack_vectors(positions)

def unpack_vectors(vector_list):
    """
    Takes a list of 2d vectors and returns two lists,
    each containing the corresponding components in association
    """
    xs = []
    ys = []
    for v in vector_list:
        xs.append(v[0])
        ys.append(v[1])
    return xs, ys
    
def plot_trajectory(xpoints, ypoints):
    plt.plot(xpoints, ypoints)
    plt.plot([constants.PLAYER_DISTANT], [constants.BASKET_HEIGHT], "ro")
    plt.savefig("trajectory.png")

#47 pi / 128 - good lower shot
#56 pi / 128 - good upper shot
def main():
    xpoints, ypoints = solve_boundary_problem(2, 56 * math.pi / 128, 100)
    plot_trajectory(xpoints, ypoints)

def newton_zero(function, derivative, guess, num_iterations, epsilon=0.01):
    """
    Uses newton's method to determine a zero of a given function
    Takes in the function and its derivative, as functions
    If the function value at the determined zero is further from zero than `epsilon`, 
    the zero determined is known to be fraudulent
    Returns the final determined input for the zero and whether or not this is a "true" zero
    """
    for i in range(num_iterations):
        guess -= function(guess) / derivative(guess)
    true_zero = abs(function(guess)) < epsilon
    return guess, true_zero

def try_newton_guess(times, positions, velocities, guess):
    """
    Tries to determine a time at which the position of the basketball
    is at the basket
    Uses Newton's method of approximation on a system:
     - x(t) - x_b = 0,
     - y(t) - y_b = 0,
    trying to find a solution to this system. 
    TODODODO:
    """
    pass

if __name__ == "__main__":
    main()