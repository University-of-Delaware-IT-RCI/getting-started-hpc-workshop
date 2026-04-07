# Python Example Job

For instructions on how to run the job, see [How to run the job](#how-to-run-the-job). The other sections provide additional
background information on the job.

## What does this directory contain?

The file `minimize.py` is a serial Python script that finds the minimum value of a function of one variable. It should run
very quickly, and is not computationally intensive. There is no parallelism in this job.

The file `minimize_job.qs` is a batch job script for the Slurm scheduler,
based on the DARWIN job script template for a serial job.

## What software does the job depend on?

The only requirement is a Python interpreter. The job script ensures that this requirement is fulfilled on DARWIN by
loading the Python 3.13.1 interpreter with VALET.

## How to run the job

Once you have set your workgroup, run:

```
sbatch minimize_job.qs
```

## Job outputs

The job will output a small text file called `min_result.txt`, which reports the minimum value that was found by
`minimize.py`. The contents of this file should be:
```

--------------------
Minimization result:
--------------------
  x_min  = 0.16143936157119554
f(x_min) = -127.88015857955023

```

Also, it will generate a Slurm log file, `py_min-<job-id>.out`, with `<job-id>` being a number corresponding
to the ID of your particular job. The contents of this file should be:
```
Adding package `python/3.13.1` to your environment

Initial guess for minimum location: 0

Step 0: 0
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
