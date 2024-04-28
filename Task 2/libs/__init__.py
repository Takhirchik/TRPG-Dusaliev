"""
Реализация преобразования ПСЧ к заданному распределения
"""

from .standart import st
from .triangle import tr
from .exponential import ex
from .normal import nr
from .gamma import gm
from .lognormal import ln
from .logistic import ls
from .binomial import bi

__all__ = [
    "st",
    "tr",
    "ex",
    "nr",
    "gm",
    "ln",
    "ls",
    "bi"
]

