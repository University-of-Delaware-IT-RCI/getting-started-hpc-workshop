COMPILE_ENV = darwin

ifeq ($(COMPILE_ENV), local)
  CXX = g++
endif
# If compiling on DARWIN, CXX should be set
# (assuming compiler was loaded with vpkg_devrequire)

# Optional compiler flags
CXXFLAGS = -Wall -O3 -march=native

# Eigen include directory for installation on Ubuntu Linux with apt
EIGEN_INC_LINUX=/usr/include/eigen3

# Mandatory compiler flags, with optional ones appended
ifeq ($(COMPILE_ENV), local)
  ALL_CXXFLAGS = -I$(EIGEN_INC_LINUX) -fopenmp $(CXXFLAGS)
endif
ifeq ($(COMPILE_ENV), darwin)
  ALL_CXXFLAGS = -I${EIGEN_PREFIX}/include/eigen3 -fopenmp $(CXXFLAGS)
endif

.PHONY: clean

matrix_multiply : matrix_multiply.cpp
	$(CXX) $(ALL_CXXFLAGS) -o matrix_multiply matrix_multiply.cpp

clean : 
	rm -f matrix_multiply
