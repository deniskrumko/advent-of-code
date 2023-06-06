import random
import time

import numpy
import pytest

ARRAY_SIZE = 5000


@pytest.fixture(scope='session')
def rand_array():
    return numpy.random.randint(1, 1000, size=ARRAY_SIZE).tolist()


def bubble_sort(array, flag=True):
    """Bubble sort.

    Sort by swapping in-place.

    - Memory: O(1)
    - Best case: O(n)
    - Worst case: O(n * n)
    """
    while flag:
        flag = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = True
    return array


def quick_sort(array) -> list:
    """Quick sort.

    First dumb solution without using randomization.

    - Memory: O(1)
    - Best case: O(n * log(n))
    - Worst case: O(n * n)
    """
    array_len = len(array)
    if array_len < 2:
        return array

    # better to use random for large array sizes
    pivot_index = array_len // 2
    pivot = array.pop(pivot_index)
    return (
        quick_sort([i for i in array if i <= pivot])
        + [pivot]
        + quick_sort([i for i in array if i > pivot])
    )


def quick_sort_with_rand(array) -> list:
    """Quick sort with randomization.

    Randomization allows to select best pivot in average.

    - Memory: O(1)
    - Best case: O(n * log(n))
    - Worst case: O(n * n)
    """
    array_len = len(array)
    if array_len < 2:
        return array

    pivot_index = random.randint(0, array_len - 1)
    pivot = array.pop(pivot_index)
    return (
        quick_sort([i for i in array if i <= pivot])
        + [pivot]
        + quick_sort([i for i in array if i > pivot])
    )


def quick_sort_chatgpt(arr):
    """Quick sort implementation from ChatGPT.

    Shows interesting thing with middle array instead of middle element.

    - Memory: O(1)
    - Best case: O(n * log(n))
    - Worst case: O(n * n)
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_with_rand_and_optimization(array) -> list:
    """Quick sort - my best implementation.

        1. Uses randomization
        2. Uses optimization from ChatGPT solution
        3. It's really is fastest (on average) among other solutions

    - Memory: O(1)
    - Best case: O(n * log(n))
    - Worst case: O(n * n)
    """
    array_len = len(array)
    if array_len < 2:
        return array

    pivot = array[random.randint(0, array_len - 1)]
    return (
        quick_sort([i for i in array if i < pivot])
        + [i for i in array if i == pivot]
        + quick_sort([i for i in array if i > pivot])
    )


@pytest.mark.parametrize('sorting_func', (
    bubble_sort,
    quick_sort,
    quick_sort_with_rand,
    quick_sort_chatgpt,
    quick_sort_with_rand_and_optimization,
))
def test_all_sorting_algorithms(rand_array, sorting_func):
    time_start = time.time()
    sort_result = sorting_func(rand_array[:])
    time_end = time.time()
    print(f'\n\tOperation done in {time_end - time_start:.5f} seconds')
    assert sort_result == sorted(rand_array[:])
