#!/usr/bin/python3
"""
Compute size data about hypercube and other cool object
"""

# time measures:
# time ./test.py 1000 > /dev/nul
# 1.69sec

import argparse
import itertools
import math
import shutil

from colorama import Style

MAX_DIM = 20


def compute(max_dim, cell_size, no_highlight=False):
    """
    Create a node, and then print dimensions of each object of greater dimension
    """
    obj = increase(tuple())
    for cardinality in local_range(max_dim):
        tee = itertools.tee(obj)
        obj = increase(tuple())
        display(tee[0], cell_size, cardinality, no_highlight)
        obj = increase(tee[1])


def increase(hyper):
    """
    Transform an hyper cube (or point, line, cube def) of dimension N to N+1
    hc is a set of number of object of each dimensions).
    ex: for a cube there is 1 object of dimension 3, 4 edges, 8 nodes.
    """
    last = 0
    for dim in hyper:
        yield last + dim*2
        last = dim
    yield 1


def display(obj, cell_size, cardinality, no_highlight):
    """
    Pretty display of a array

    TODO, usage of multiple print(, end='') is slower than putting on in an
    array print(' '.join(array))
    """
    tee = itertools.tee(obj)
    maximum = max(tee[1])
    id_elem = 0
    for cnt in tee[0]:
        if not no_highlight and cnt == maximum:
            print(f'{Style.BRIGHT}{cnt:-{cell_size}}{Style.RESET_ALL}', end='')
        else:
            print(f'{cnt:-{cell_size}}', end='')
        if id_elem != cardinality:
            print(' ', end='')
            id_elem += 1
    print()


def build_argp():
    """
    Build the argument parser
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'max_dim',
        type=int,
        default='5',
        nargs='?',
        help="Maximum dimension cardinality, horizontal fill if set to 0, "
             "infinite if set to -1")
    parser.add_argument(
        '--cell-size', type=int, default=0, dest='size',
        help="Maximum cell size for display, '0' means auto")
    parser.add_argument(
        '--raw', '-r', action="store_true",
        help="Sets cell size to 1 and disable highlights")
    parser.add_argument(
        '--no-highlight', '-c', action="store_true",
        help="Do not highlight elements")
    parser.add_argument(
        '--force', '-f', action="store_true",
        help="Run, even if it breaks display")
    return parser


def local_range(stop):
    """
    Locally defined range() to support infinite loop
    """
    pos = 0
    while stop is None or (pos < stop):
        yield pos
        pos += 1


def ideal_max_dim(term_size):
    """
    Compute ideal maximal dimension for a pretty display
    """
    delta = 1 + 2*(term_size+1)
    sol = (-1 + math.sqrt(delta))
    return math.floor(sol)


def main():
    """
    Parse argument and then compute output
    """
    parser = build_argp()
    parameters = parser.parse_args()
    max_dim = parameters.max_dim
    cell_size = parameters.size
    no_highlight = parameters.no_highlight
    terminal_width = shutil.get_terminal_size()[0]
    if max_dim == 0:
        max_dim = ideal_max_dim(terminal_width)
    if max_dim == -1:
        max_dim = None
    if parameters.raw:
        cell_size = 1
        no_highlight = True
    if cell_size == 0:
        if max_dim is None:
            cell_size = 1
        else:
            cell_size = math.ceil(max_dim/2)
    if max_dim is not None:
        max_line_size = max_dim*(1 + cell_size) - 1
        if not parameters.force and max_line_size > terminal_width:
            print('Line will be too long')
            raise SystemExit(1)
    compute(max_dim, cell_size, no_highlight)

if __name__ == "__main__":
    main()
