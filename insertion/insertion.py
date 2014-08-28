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
        print(lst)
        N = len(lst)
        for i in range(N):
            curr = lst[i]
            print('curr: ' + str(curr))
            for j in range(i, -1, -1):
                if lst[j] > lst[i]:
                    print('breaking early: --------')
                    print(lst[i])
                    print(lst[j])
                    print('--------')
                    break
                Insertion._exch(lst, j, i)
            print(lst)
        print(lst)

    @staticmethod
    def _exch(lst, a, b):
        """Exchange a and b. Return void."""
        temp = lst[a]
        lst[a] = lst[b]
        lst[b] = temp


if __name__ == '__main__':
    Insertion.sort([4,5,2,3])
