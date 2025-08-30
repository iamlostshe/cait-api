"""Инициализация директории как модуля."""

from .pars import CAITParser

__all__ = (
    "CAIT",
    "CAITParser",
    "NoDataForThisDayError",
    "UnknownError",
)
