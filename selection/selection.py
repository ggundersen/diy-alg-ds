#!/usr/bin/env python

"""----------------------------------------------------------------------------
selection.py

Selection sort sorts a list with the following algorithm:
- Find the 1st smallest item in the array and exchange it with the 1st item.
- Find the 2nd smallest item in the array and exchange it with the 2nd item.
- And so on.
----------------------------------------------------------------------------"""


class Selection:

    @staticmethod
    def sort(lst):
        """Sort using selection sort."""
        print(lst)
        N = len(lst)
        for i in range(N):
            min_idx = i
            for j in range(i+1, N):
                if lst[j] < lst[i]:
                    min_idx = j
                    Selection._exch(lst, i, min_idx)
            print(lst)

    @staticmethod
    def _exch(lst, a, b):
        """Exchange a and b. Return void."""
        temp = lst[a]
        lst[a] = lst[b]
        lst[b] = temp


if __name__ == '__main__':
    Selection.sort([4,5,2,3])
