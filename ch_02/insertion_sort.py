"""
Learning about insertion sort algorithm
"""

from typing import List
from timeit import default_timer as timer


def insertion_sort(x: List[int], ascending: bool = True) -> List[int]:
    """Sort a small number of integers in ascending/descending order.

    Insertion sort works the way many people sort a hand of playing cards:
    \t * Start with an empty left hand and the cards face down on the table
    \t * Then remove one card at a time from the table and insert it into \
    the correct position in the left hand.
    \t * To find the corret position for a card, it is compared with each of \
    the cards already in hand, from right to left.
    \t * At all times, the cards held in the left hand are sorted, and these \
    cards were originally the top cards of the pile on the table
    """
    start = timer()
    for ind, val in enumerate(x):
        i = ind - 1
        if ascending:
            comparison = x[i] > val
        else:
            comparison = x[i] < val
        while i > -1 and comparison:
            x[i + 1] = x[i]
            i = i - 1
            # TODO: figure out way to avoid duplicate if-else statements
            if ascending:
                comparison = x[i] > val
            else:
                comparison = x[i] < val
        x[i + 1] = val
    print(timer() - start)
    return x
