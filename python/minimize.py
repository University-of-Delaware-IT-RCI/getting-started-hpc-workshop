# Script to find the minimum of a function using Newton's method
#
# Does not use external Python libraries. Only requires the standard
# "math" Python module.
#
# Intended to be a simple example for use with an HPC job submission script,
# without requiring setup of a Python virtual environment. There is no
# parallelism, so this is only meant to be run as a serial job.

import math

if __name__ == "__main__":

    # Objective function to minimize, and its derivatives
    function = lambda x : 50*math.exp(x) + \
                          -50*x*math.sinh(1) + \
                          -(100 + 50*math.cosh(1))
    gradient = lambda x : 50*math.exp(x) - 50*math.sinh(1)
    hessian  = lambda x : 50*math.exp(x)

    # Initial guess
    arg_min = 0
    
    # Number of Newton iterations
    # Not many are needed because the initial guess is already close
    iterations = 10

    print(f'\nInitial guess for minimum location: {arg_min}\n')

    print(f'Step 0: {arg_min}')

    # Newton loop
    for i in range(iterations-1):
        arg_min = arg_min - gradient(arg_min)/hessian(arg_min)
        print(f'Step {i+1}: {arg_min}')

    min_value = function(arg_min)

    print(' ')

    # Output result to file (overwrites file if it already exists) 
    with open('min_result.txt', 'w') as output_file:
        output_file.write('\n--------------------\n')
        output_file.write('Minimization result:')
        output_file.write('\n--------------------\n')
        output_file.write(f'  x_min  = {arg_min}\n')
        output_file.write(f'f(x_min) = {min_value}\n\n')
