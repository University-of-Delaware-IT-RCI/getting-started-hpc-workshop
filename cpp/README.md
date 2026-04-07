# C++ Example Job

For instructions on how to run the job, see [How to run the job](#how-to-run-the-job). The other sections provide additional
background information on the job.

## What does this directory contain?

The file `matrix_multiply.cpp` is a C++ program that multiplies two matrices together. It uses shared memory parallelism
via OpenMP to speed up the computation when run with multiple processors. The matrix multiplication is timed, and this
time is reported in a Slurm log file that can be inspected after the job runs.

The file `Makefile` facilitates the compilation of the C++ program using GNU Make. You do not need to be familiar with
how Makefiles work to run this job. The command you need to run to use this Makefile is provided below.

The file `matrix_multiply_job.qs` is a batch job script for the Slurm scheduler, based on the DARWIN job script template
for a multi-threaded parallel job.

## What software does the job depend on?

A C++ compiler and the Eigen library are required to compile the program. These are available on DARWIN via VALET. See
[How to run the job](#how-to-run-the-job) below for more information.

The C++ standard library is also needed at runtime. The job script ensures that this requirement is fulfilled.

## How to run the job

Before running the job, we need to compile the program. First, load a recent C++ compiler and the
Eigen library with VALET:
```
vpkg_devrequire gcc/14.2 eigen
```
Then, compile the program by running:
```
make
```
You should now see an executable named `matrix_multiply` in this directory.

Once you have set your workgroup, run:
```
sbatch matrix_multiply_job.qs
```
to run the job with a single processor. To run the job with multiple processors, edit the job script to increase
`--cpus-per-task` to the desired number of processors, and submit the job again.

## Job outputs

The only output is a Slurm log file, `mat_mult-<job-id>.out`, with `<job-id>` being a number corresponding to the ID
of your particular job. An example of what this log file contains for a run with 4 processors is provided below, but
keep in mind that the specific number for the timing, as well as processor IDs (the `58,59,60,61` you see below),
may differ for you:
```
Adding package `gcc/14.2.0` to your environment
-- OpenMP job setup complete:
--  OMP_THREAD_LIMIT     = 4
--  OMP_PROC_BIND        = true
--  OMP_PLACES           = cores
--  MKL_NUM_THREADS      = 4
--  MKL_DYNAMIC          = true
--  MP_BLIST             = 58,59,60,61


Using 4 OpenMP threads...

Multiplying matrices with dimension N = 4000

Time (s) = 0.830722

```
