"""Test cython module1
"""
import numpy as np

cimport cython
from libc.stdio cimport printf
from numpy cimport import_array, ndarray, uint32_t

from cython.parallel import prange

__all__ = ["example_mpi"]


import_array()

cpdef void hello_cython():
    printf("Hello world from cython!\n")


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.initializedcheck(False)
cpdef ndarray[uint32_t, ndim=2] example_mpi(int nx=100, int ny=100):
    cdef:
        ndarray[uint32_t, ndim=2] ans = np.zeros((nx, ny), dtype=np.uint32)
        uint32_t[:, ::1] ans_mv = ans
        int i, j

    for i in prange(nx, nogil=True):
        for j in range(ny):
            ans_mv[i, j] = 1

    return ans


cdef class TestClass1:
    """Test class1

    Parameters
    ----------
    a : int
        parameter a
    b : int
        parameter b
    """
    def __init__(self, int a, int b):
        self.a = a
        self.b = b

    cpdef void print_result(self):
        cdef int c = self.add()
        printf("a: %d, b: %d, a+b: %d\n", self.a, self.b, c)

    cdef int add(self) nogil:
        return self.a + self.b
