# Python Example Job Array

For instructions on how to run the job, see [How to run the job](#how-to-run-the-job). The other sections provide additional
background information on the job.

## What does this directory contain?

The file `minimize.py` is a serial Python script that finds the minimum value of a function of one variable. It should run
very quickly, and is not computationally intensive.

The script is intended to be run as a job array. It gets the Slurm
array task ID and task count from the environment, and computes a different initial guess for each array task based on these
values. Therefore, although the script is serial, running it using a job array demonstrates parallelism in the form of multiple independent serial jobs.

The file `minimize_job_array.qs` is a batch job script for the Slurm scheduler.
It is based on the DARWIN job script template for a serial job, but
modified with the `--array` option to demonstrate job array submission.

## What software does the job depend on?

The only requirement is a Python interpreter. The job script ensures that this requirement is fulfilled on DARWIN by
loading the Python 3.13.1 interpreter with VALET.

## How to run the job

Once you have set your workgroup, run:

```
sbatch minimize_job_array.qs
```

## Job outputs

The job will output three small text files which report the minimum values that were found by
`minimize.py` starting at three different initial guesses.

The contents of file `min_result_0.txt` should be:
```

--------------------
Minimization result:
--------------------
 Task ID = 0
  x_min  = 0.16143936157119554
f(x_min) = -127.88015857955023

```

The contents of file `min_result_1.txt` should be:
```

--------------------
Minimization result:
--------------------
 Task ID = 1
  x_min  = 0.16143936157119554
f(x_min) = -127.88015857955023

```

The contents of file `min_result_2.txt` should be:
```

--------------------
Minimization result:
--------------------
 Task ID = 2
  x_min  = 0.16143936157119557
f(x_min) = -127.88015857955023

```

Also, the job will generate three Slurm log files, `py_min-<job-id>_0.out`,
`py_min-<job-id>_1.out`, and `py_min-<job-id>_2.out` with `<job-id>` being
a number corresponding to the ID of your particular job.

The contents of file `py_min-<job-id>_0.out` should be:
```
Adding package `python/3.13.1` to your environment

Initial guess for minimum location: -1.0

Step 0: -1.0
Step 1: 1.1945280494653248
Step 2: 0.5504340281272665
Step 3: 0.22817191280860488
Step 4: 0.1636172643944559
Step 5: 0.1614417314807596
Step 6: 0.16143936157400385
Step 7: 0.16143936157119554
Step 8: 0.16143936157119554
Step 9: 0.16143936157119554

```

The contents of file `py_min-<job-id>_1.out` should be:
```
Adding package `python/3.13.1` to your environment

Initial guess for minimum location: 0.0

Step 0: 0.0
Step 1: 0.17520119364380135
Step 2: 0.1615336226848889
Step 3: 0.16143936601363482
Step 4: 0.16143936157119568
Step 5: 0.16143936157119543
Step 6: 0.16143936157119554
Step 7: 0.16143936157119554
Step 8: 0.16143936157119554
Step 9: 0.16143936157119554

```

The contents of file `py_min-<job-id>_2.out` should be:
```
Adding package `python/3.13.1` to your environment

Initial guess for minimum location: 1.0

Step 0: 1.0
Step 1: 0.4323323583816937
Step 2: 0.1950304615502552
Step 3: 0.1619972781122676
Step 4: 0.16143951717768906
Step 5: 0.16143936157120767
Step 6: 0.16143936157119557
Step 7: 0.16143936157119557
Step 8: 0.16143936157119557
Step 9: 0.16143936157119557

```

These results show that the same minimum is reached from all three initial guesses.
