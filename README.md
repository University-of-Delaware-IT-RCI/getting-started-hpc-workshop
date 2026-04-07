# Getting Started with DARWIN

This repository contains example jobs for the "Getting Started with DARWIN" workshop at the University of Delaware. Job scripts are tailored for the DARWIN system, but the code for the example jobs could be used on other HPC systems. Refer to the README files in each example directory for instructions on how to run the jobs.

## Getting this repository

Once you are logged in to DARWIN, navigate to the directory where you want to copy this repository and run:

```
git clone https://github.com/University-of-Delaware-IT-RCI/getting-started-hpc-workshop.git
```

## Running jobs on DARWIN

Before running jobs on DARWIN, you need to set your workgroup. For example, a user with username `user` and workgroup name `my_workgroup` should run:
```
[user@login00.darwin ~]$ workgroup -g my_workgroup
[(my_workgroup:user)@login00.darwin ~]$
```

Job script templates are provided in `/opt/shared/templates/slurm` that you should always use as a starting point for your job scripts.
The example jobs in this repository already provide job scripts based on these templates.

## Python example job

The `python` directory provides a serial job written in Python. It does not use any external Python packages, so the only requirement is to have a recent enough Python interpreter available.

## C++ example job

The `cpp` directory provides a parallel job written in C++, with shared memory parallelism via OpenMP. It also uses the Eigen library for linear algebra operations.
