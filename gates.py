"""
gates.py
--------
Truth-table data for all logic gates supported by this project.
Each gate is a dictionary with:
  - 'y' : expected output
  - 'linearly_separable': linearly seprable or not
"""

import numpy as np

INPUTS = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
])

GATES = {
    "INPUTS":INPUTS,
    "AND": {
        "y": np.array([0, 0, 0, 1]),
        "linearly_separable": True,
    },
    "OR": {
        "y": np.array([0, 1, 1, 1]),
        "linearly_separable": True,
    },
    "NAND": {
        "y": np.array([1, 1, 1, 0]),
        "linearly_separable": True,
    },
    "NOR": {
        "y": np.array([1, 0, 0, 0]),
        "linearly_separable": True,
    },
    "XOR": {
        "y": np.array([0, 1, 1, 0]),
        "linearly_separable": False,
    },
}
