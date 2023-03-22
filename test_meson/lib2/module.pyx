"""Test module
"""
from libc.stdio cimport printf

from ..lib1.module cimport TestClass1


cdef class TestClass2(TestClass1):
    """Test class inherited by lib1.module.TestClass1

    Parameters
    ----------
    a : int
        parameter a
    b : int
        parameter b
    c : int
        parameter c
    """
    cdef:
        public int c

    def __init__(self, int a, int b, int c):
        self.c = c
        super().__init__(a, b)

    cpdef void print_result(self):
        """print (self.a + self.b) * self.c
        """
        cdef int val = self.mul(self.add())
        printf("a: %d, b: %d, c: %d, (a + b) * c: %d\n", self.a, self.b, self.c, val)

    cdef int mul(self, int val) nogil:
        return val * self.c
