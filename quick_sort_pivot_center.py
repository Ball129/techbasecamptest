from math import floor

# Test 1000 times, 100,000 items each
# Average time: 0.43 s (198.13 times of builtin sorted)
# Average recursive depth 40.174
# Average swap 465013.845
# algorithm ref: https://en.wikipedia.org/wiki/Quicksort, https://www.geeksforgeeks.org/quick-sort/


def partition_sort(array: list, low: int, high: int):
    i = low
    j = high
    swap_count = 0
    loop_limit = high + 1 - low

    # Find true median of three
    mid = floor((low + high) / 2)

    if array[low] > array[mid]:
        array[low], array[mid] = array[mid], array[low]
        swap_count += 1

    if array[low] > array[high]:
        array[low], array[high] = array[high], array[low]
        swap_count += 1

    if array[mid] > array[high]:
        array[mid], array[high] = array[high], array[mid]
        swap_count += 1

    # Set pivot
    pivot = array[mid]

    # Do sort
    while True:
        if loop_limit <= 0:
            raise OverflowError

        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i >= j:
            break

        array[i], array[j] = array[j], array[i]

        swap_count += 1
        loop_limit -= 1

    return i, swap_count


def quick_sort(array: list, low: int, high: int,
               # Use to measure performance for this test.
               depth: int = 0, depth_count: int = 0, swap_count: int = 0):

    if depth > depth_count:
        depth_count = depth

    if low < high:
        # Find partition point
        partition_point, _swap_count = partition_sort(array, low, high)
        swap_count += _swap_count

        # Left partition
        array, depth_count, swap_count = quick_sort(array, low, partition_point,
                                                    depth+1, depth_count, swap_count)

        # Right partition
        array, depth_count, swap_count = quick_sort(array, partition_point + 1, high,
                                                    depth+1, depth_count, swap_count)

    return array, depth_count, swap_count
