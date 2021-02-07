import sympy as sp
from sympy.functions.combinatorial.numbers import *
from itertools import product
import numpy as np


def stable_soln_fast(transition_matrix: np.matrix):
    m = transition_matrix.T
    _, eigen_matrix = np.linalg.eig(m)

    vec: np.matrix = None
    for eig_vec in eigen_matrix.T:
        if eig_vec.min() >= 0:
            vec = eig_vec
            break

    vec = np.divide(vec, vec.sum())

    return vec


def flip_fewer_coins(a_flips, b_flips):
    def fewer_flips(n, a):
        if n > a:
            return 1
        if n <= 0:
            return 0
        return sum(nC(a, i) * (sp.Rational(1, 2) ** a) for i in range(n))

    return sum(
        nC(b_flips, i + 1)
        * fewer_flips(i + 1, a_flips)
        * (sp.Rational(1, 2) ** b_flips)
        for i in range(b_flips)
    )


def going_up():
    return nC(4, 3) * Rational(1, 2) ** 4 + Rational(1, 2) ** 4


print(going_up())

# print(flip_fewer_coins(3, 4))

# print(stable_soln_fast(np.matrix([[0.3, 0.7], [0.8, 0.2]])))
