from numpy cimport ndarray, uint32_t


cpdef void hello_cython()

cpdef ndarray[uint32_t, ndim=2] example_parallel(int nx=*, int ny=*)

cdef class TestClass1:
    cdef:
        public int a
        public int b
    
    cpdef void print_result(self)

    cdef int add(self) nogil
