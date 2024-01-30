#!/usr/bin/python3
""" multiply two matrix using external module"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ multiply two matrix """
    return numpy.matmul(m_a, m_b)
