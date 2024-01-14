import random
import timeit


def merge_sort(arr):
    """Implementing merge sorting"""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def insertion_sort(arr):
    """Implementing insert sorting"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def measure_time(sort_function, data):
    """Function for measuring sorting execution time"""
    time = timeit.timeit(lambda: sort_function(data.copy()), number=1)
    formated_time = f"{time:.6f}"
    return formated_time

# Generating random data for testing
data_small = random.sample(range(1000), 100)   # small array
data_medium = random.sample(range(10000), 1000) # medium array
data_large = random.sample(range(100000), 10000) # large array

# Runtime measurement for different algorithms and data sizes
times = {}
for size, data in zip(['small', 'medium', 'large'], [data_small, data_medium, data_large]):
    times[(size, 'merge_sort')] = measure_time(merge_sort, data)
    times[(size, 'insertion_sort')] = measure_time(insertion_sort, data)
    times[(size, 'timsort (sorted)')] = measure_time(sorted, data)


def print_results(times):
    """Function for displaying results"""
    print(f"{'Data size':<12} | {'Algorithm':<17} | {'Execution Time (seconds)':<30}")
    print("-" * 60)

    for (size, algorithm), time in times.items():
        print(f"{size:<12} | {algorithm:<17} | {time:<30}")

print_results(times)
