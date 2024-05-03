"""
Генератор стандартного равномерного распределения
"""
__all__ = ['_gen']

from math import floor

def uniform_distribution(numbers, m):
    i = 0
    while i < len(numbers):
        x = numbers[i] / m
        yield x
        i += 1

_gen = uniform_distribution
