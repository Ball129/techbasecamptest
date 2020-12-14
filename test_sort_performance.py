#!/usr/bin/python
from random import shuffle
from time import time

import sys

from quick_sort_pivot_center import quick_sort


f = open('test_result.txt', 'w')


def print_with_log(txt):
    print(f'{txt}')
    f.write(f'{txt}\n')


def test(test_number: int):
    total_function_time = 0
    total_builtin_time = 0
    total_depth_count = 0
    total_swap_count = 0
    test_items = int(1e+5)

    for i in range(test_number):
        # Create sample data
        unsorted_list = [i for i in range(1, test_items + 1)]
        shuffle(unsorted_list)

        # Use Quicksort
        start = time()
        sorted_list, depth_count, swap_count = quick_sort(unsorted_list, 0, len(unsorted_list) - 1)
        end = time()

        # Compare with python sorted (tim-sort)
        start_builtin_time = time()
        builtin_sorted_list = sorted(unsorted_list)
        end_builtin_time = time()

        # Check if sorted correctly
        assert sorted_list == builtin_sorted_list

        my_sorted_time = end-start
        builtin_time = end_builtin_time - start_builtin_time
        total_function_time += my_sorted_time
        total_builtin_time += builtin_time
        total_depth_count += depth_count
        total_swap_count += swap_count

        if i % 10 == 0:
            print_with_log(f'Sorting {len(unsorted_list)} numbers ({min(unsorted_list)} - {max(unsorted_list)})')
            print_with_log(f'Loop {i}:> Total time: {my_sorted_time:.2f} s ({my_sorted_time/builtin_time:.2f} '
                           f'times of builtin sorted)')
            print_with_log(f'Loop {i}:> Max recursive depth {depth_count}')
            print_with_log(f'Loop {i}:> Total swap {swap_count}')

            print_with_log('')

    print_with_log(f'Average time: {total_function_time/test_number:.2f} s '
                   f'({total_function_time / total_builtin_time:.2f} times of builtin sorted)')
    print_with_log(f'Average recursive depth {total_depth_count/test_number}')
    print_with_log(f'Average swap {total_swap_count/test_number}')

    f.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        times = 1
    else:
        times = sys.argv[1]

    print(f'Start test performance {times} times.')
    test(int(times))
