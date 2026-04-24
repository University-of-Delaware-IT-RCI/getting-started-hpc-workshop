# Set flags for compiling on DARWIN if environment is not specified
COMPILE_ENV = darwin

# OpenMP flag is different for Intel compiler
ifeq ($(CXX), icpx)
  OMP_FLAG = -qopenmp
else
  OMP_FLAG = -fopenmp
endif

# Compiler flags for OpenMP and optimizations (plus warnings)
CXXFLAGS = $(OMP_FLAG) -O3 -march=native -Wall

# Workaround for missing eigen3 from VALET's Eigen CPPFLAGS
ifeq ($(COMPILE_ENV), darwin)
  CPPFLAGS := $(CPPFLAGS)/eigen3
endif

# Eigen include directories for testing on a local machine
# (need to set COMPILE_ENV when running make for this to work)
#
# Options provided for Eigen installed on Ubuntu Linux with APT
# or Eigen installed on macOS with Homebrew
#
ifeq ($(COMPILE_ENV), ubuntu)
  CPPFLAGS = -I/usr/include/eigen3
else ifeq ($(COMPILE_ENV), macos)
  CPPFLAGS = -I/opt/homebrew/Cellar/eigen/5.0.1/include/eigen3
endif

.PHONY: clean

matrix_multiply : matrix_multiply.cpp
	$(CXX) $(CXXFLAGS) $(CPPFLAGS) matrix_multiply.cpp -o matrix_multiply

clean : 
	$(RM) matrix_multiply
