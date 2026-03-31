COMPILE_ENV = darwin

# OpenMP flag differs depending on compiler
ifeq ($(CXX), icpx)
  OMP_FLAG = -qopenmp
else
  OMP_FLAG = -fopenmp
endif

# Compiler flags for OpenMP and optimizations (plus warnings)
CXXFLAGS = $(OMP_FLAG) -O3 -march=native -Wall

# Eigen include directory for installation on Ubuntu Linux with apt
# (can be used for testing on a local machine)
ifeq ($(COMPILE_ENV), local)
  CPPFLAGS = -I/usr/include/eigen3 
endif

# Workaround for missing eigen3 from VALET's Eigen CPPFLAGS
ifeq ($(COMPILE_ENV), darwin)
  CPPFLAGS := $(CPPFLAGS)/eigen3
endif

.PHONY: clean

matrix_multiply : matrix_multiply.cpp
	$(CXX) $(CXXFLAGS) $(CPPFLAGS) matrix_multiply.cpp -o matrix_multiply

clean : 
	$(RM) matrix_multiply
