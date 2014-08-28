#!/usr/bin/env python

"""----------------------------------------------------------------------------
insertion.py

Insertion sort sorts a list with the following algorithm:
- Insert the current item into its sorted place among the items already
  considered. Everything to the left of the current item should always be
  sorted.
----------------------------------------------------------------------------"""


class Insertion:

    @staticmethod
    def sort(lst):
        """Insertion sort list. Return list."""
        N = len(lst)
        for i in range(1, N):
            for j in range(i, 0, -1):
                if lst[j-1] < lst[j]:
                    break
                Insertion._exch(lst, j-1, j)
        return lst

    @staticmethod
    def _exch(lst, a, b):
        """Exchange a and b. Return void."""
        temp = lst[a]
        lst[a] = lst[b]
        lst[b] = temp


if __name__ == '__main__':
    print(Insertion.sort([4,5,99,3]))
