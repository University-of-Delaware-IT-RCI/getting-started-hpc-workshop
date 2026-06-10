# Script to find the minimum of a function using Newton's method
#
# Does not use external Python libraries. Only requires the standard
# "math" Python module.
#
# Intended to be a simple example for use with an HPC job submission script,
# without requiring setup of a Python virtual environment. There is no
# parallelism, so this is only meant to be run as a serial job.
#
# Demonstrates Slurm job array functionality, with each array task starting
# from a different initial guess that is determined based on its task ID.
# Each array task is still a serial job, but now there is parallelism in
# the sense that we can try several different initial guesses at the same time.

import math
import os

if __name__ == "__main__":

    # Job array information
    array_task_id = int(os.getenv("SLURM_ARRAY_TASK_ID"))
    array_task_count = int(os.getenv("SLURM_ARRAY_TASK_COUNT"))
    
    # Objective function to minimize, and its derivatives
    function = lambda x : 50*math.exp(x) + \
                          -50*x*math.sinh(1) + \
                          -(100 + 50*math.cosh(1))
    gradient = lambda x : 50*math.exp(x) - 50*math.sinh(1)
    hessian  = lambda x : 50*math.exp(x)

    # Bounds of the domain in which we seek a minimum
    x_lower = -1
    x_upper = 1

    # Interval between initial guesses covered by the job array 
    x_step = (x_upper - x_lower) / (array_task_count - 1)

    # Initial guess based on array task ID
    arg_min = x_lower + x_step * array_task_id
    
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
    with open(f'min_result_{array_task_id}.txt', 'w') as output_file:
        output_file.write('\n--------------------\n')
        output_file.write('Minimization result:')
        output_file.write('\n--------------------\n')
        output_file.write(f' Task ID = {array_task_id}\n')
        output_file.write(f'  x_min  = {arg_min}\n')
        output_file.write(f'f(x_min) = {min_value}\n\n')
