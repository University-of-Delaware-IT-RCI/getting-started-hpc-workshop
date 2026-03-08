// Code to do matrix-matrix multiplication with shared memory parallelism
//
// The Eigen library is used for the (dense) matrix multiplication, while OpenMP
// is used for parallelism. OpenMP's timer is used for measuring the runtime.
//
// Intended to be a simple example for use with an HPC job submission script.
// Can be used to demonstrate speedup when increasing the number of OpenMP
// threads.

#include <iostream>
#include <Eigen/Dense>

using Eigen::MatrixXd;

int main(int argc, char *argv[])
{
    std::cout << "\nUsing " << Eigen::nbThreads() << " OpenMP threads...";
    std::cout << std::endl << std::endl;

    // Default matrix dimension if no argument is passed in
    int N = 1000;

    // If an integer is passed in, this is used as the matrix dimension
    if (argc > 1)
        N = atoi(argv[1]);

    std::cout << "Multiplying matrices with dimension N = ";
    std::cout << N << std::endl << std::endl;

    // Matrices are initialized to zero. We are just interested in timing the
    // operation, so the values of the entries are not important.
    MatrixXd A = MatrixXd::Zero(N, N);
    MatrixXd B = MatrixXd::Zero(N, N);
    
    MatrixXd C(N, N);

    double t0 = omp_get_wtime();

    // noalias() needed to avoid creation of a temporary matrix
    // (Eigen creates a temporary matrix by default otherwise)
    C.noalias() = A * B;

    double t1 = omp_get_wtime();

    std::cout << "Time (s) = " << t1 - t0;
    std::cout << std::endl << std::endl;
    
    return 0;
}
