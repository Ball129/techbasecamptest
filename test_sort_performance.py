#!/usr/bin/python
from random import shuffle
from time import time


# Create sample data
from quick_sort_pivot_center import quick_sort

total_function_time = 0
total_builtin_time = 0
total_depth_count = 0
total_swap_count = 0
test_number = 1
test_items = int(1e+5)

f = open('test_result.txt', 'w')


def do_print(txt):
    if i % 10 == 0:
        print(f'{i}:> {txt}')
        f.write(f'{i}:> {txt}\n')


for i in range(test_number):
    unsorted_list = [i for i in range(1, test_items + 1)]
    shuffle(unsorted_list)

    # Use Quicksort
    do_print(f'Start sorting {len(unsorted_list)} numbers ({min(unsorted_list)} - {max(unsorted_list)})')
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

    do_print(f'Total time: {my_sorted_time:.2f} s ({my_sorted_time/builtin_time:.2f} times of builtin sorted)')
    do_print(f'Max recursive depth {depth_count}')
    do_print(f'Total swap {swap_count}')


print(f'Average time: {total_function_time/test_number:.2f} s '
      f'({total_function_time / total_builtin_time:.2f} times of builtin sorted)')
print(f'Average recursive depth {total_depth_count/test_number}')
print(f'Average swap {total_swap_count/test_number}')

f.write(f'Average time: {total_function_time/test_number:.2f} s '
        f'({total_function_time / total_builtin_time:.2f} times of builtin sorted)\n')
f.write(f'Average recursive depth {total_depth_count/test_number}\n')
f.write(f'Average swap {total_swap_count/test_number}\n')
f.close()
