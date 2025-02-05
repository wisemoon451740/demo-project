import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


a = 10
b = 5
print(add(a, b))
print(substract(a, b))
print(multiply(a, b))
print(divide(a, b))
