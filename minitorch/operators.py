"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable


#
# Implementation of a prelude of elementary functions.
def mul(a, b):
    return a * b


def id(a):
    return a


def add(a, b):
    return a + b


def neg(a):
    return -a


def lt(a, b):
    return a < b


def eq(a, b):
    return a == b


def max(a, b):
    return b if a < b else a


def is_close(a, b):
    return abs(a - b) < 1e-2


def relu(a):
    return max(a, 0)


import math


def log(a):
    return math.log(a)


def exp(a):
    return math.exp(a)


def inv(a):
    return a ** -1


def sigmoid(a):
    if a > 0:
        return inv(1 + exp(-a))
    return exp(a) / (1 + exp(a))


def log_back(a, b):
    return b / a


def relu_back(a, b):
    if a < 0:
        return 0
    return b


def inv_back(a, b):
    return -b / a ** 2


# Mathematical functions:
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.

def map(iterable, function):
    for x in iterable:
        yield function(x)



def zipWith(iterable1, iterable2, function):
    for x, y in zip(iterable1, iterable2):
        yield function(x, y)



def reduce(iterable, function):
    res = None
    for x in iterable:
        if res is None:
            res = x
            continue
        res = function(res, x)
    return res


def negList(li):
    return map(li, neg)



def addLists(li1, li2):
    return zipWith(li1, li2, add)



def sum(li):
    res = reduce(li, add)
    if res is None:
        res = 0
    return res



def prod(li):
    res = reduce(li, mul)
    if res is None:
        res = 1
    return res
# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
