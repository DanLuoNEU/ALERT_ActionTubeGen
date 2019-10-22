CC=g++

OS_NAME=$(shell uname -s)
ifeq ($(OS_NAME),Linux) 
  LAPACKLDFLAGS=/usr/lib/x86_64-linux-gnu/libsatlas.so   # single-threaded blas
  #LAPACKLDFLAGS=/usr/lib64/atlas/libtatlas.so  # multi-threaded blas
  #BLAS_THREADING=-D MULTITHREADED_BLAS # remove this if wrong
endif
ifeq ($(OS_NAME),Darwin)  # Mac OS X
  LAPACKLDFLAGS=-framework Accelerate # for OS X
endif
LAPACKCFLAGS=-Dinteger=int $(BLAS_THREADING)
STATICLAPACKLDFLAGS=-fPIC -Wall -g -fopenmp -static -static-libstdc++ \
	/usr/lib/x86_64-linux-gnu/libjpeg.a \
	/usr/lib/x86_64-linux-gnu/libpng.a \
	/usr/lib/x86_64-linux-gnu/libz.a \
	/usr/lib/x86_64-linux-gnu/libblas.a \
	/usr/lib/gcc/x86_64-linux-gnu/7/libgfortran.a \
	/usr/lib/gcc/x86_64-linux-gnu/7/libquadmath.a # statically linked version

CFLAGS= -fPIC -Wall -g -std=c++11 $(LAPACKCFLAGS) -fopenmp -DUSE_OPENMP -O3
LDFLAGS=-fPIC -Wall -g -ljpeg -lpng -fopenmp 
CPYTHONFLAGS=-I/usr/include/python2.7
LIBFLAGS= -L/lib/x86_64-linux-gnu -lpng -ljpeg -lz -lblas
SOURCES := $(shell find . -name '*.cpp' ! -name 'deepmatching_matlab.cpp')
OBJ := $(SOURCES:%.cpp=%.o)
HEADERS := $(shell find . -name '*.h')


all: deepmatching-static

.cpp.o:  %.cpp %.h
	$(CC) -o $@ $(CFLAGS) -c $+

deepmatching: $(HEADERS) $(OBJ)
	$(CC) -o $@ $^ $(LDFLAGS) $(LAPACKLDFLAGS) -I/home/ibal_109/atlas/build/include

deepmatching-static: $(HEADERS) $(OBJ)
	$(CC) -o $@ $^ $(STATICLAPACKLDFLAGS)

python: $(HEADERS) $(OBJ)
#	swig -python $(CPYTHONFLAGS) deepmatching.i # not necessary, only do if you have swig compiler
	g++ $(CFLAGS) -c deepmatching_wrap.c $(CPYTHONFLAGS)
	g++ -shared $(LDFLAGS) $(LAPACKLDFLAGS) deepmatching_wrap.o $(OBJ) -o _deepmatching.so $(LIBFLAGS) 

clean:
	rm -f $(OBJ) deepmatching *~ *.pyc .gdb_history deepmatching_wrap.o _deepmatching.so deepmatching.mex???

