#!/usr/bin/python3
"""module containing lazy_matrix_mul function which uses numpy module
"""
import numpy

def lazy_matrix_mul(m_a, m_b):
    """matrix multiplication using numpy module"""
    return numpy.matmul(m_a, m_b)
