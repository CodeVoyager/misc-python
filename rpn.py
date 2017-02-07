"""
Module for RPN computation.
Will be updated for using folding
"""

import sys

def rpn(i):
    """
    Function for calculating expresions in RPN (reverse polish notation)

    Parameters:
    -----------
    i
        input

    Returns
    -------
    float
        Result of computation
    """
    h = []
    for el in i.strip().split(' ')[::-1]:
        if el.isdigit():
            h.append(float(el))
        else:
            if '+' == el:
                h.append(h.pop() + h.pop())
            if '-' == el:
                h.append(h.pop() - h.pop())
            if '*' == el:
                h.append(h.pop() * h.pop())
            if '**' == el:
                h.append(h.pop() ** h.pop())
            if '/' == el:
                h.append(h.pop() / h.pop())
            if '//' == el:
                h.append(h.pop() // h.pop())
            if '%' == el:
                h.append(h.pop() % h.pop())
    return h[0] if len(h) else 0

# print(rpn(sys.argv[1]))
