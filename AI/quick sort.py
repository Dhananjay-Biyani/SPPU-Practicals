import random
import time

def deterministic_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quicksort(arr, low, high):
    if low < high:
        pivot_index = deterministic_partition(arr, low, high)

        deterministic_quicksort(arr, low, pivot_index - 1)
        deterministic_quicksort(arr, pivot_index + 1, high)

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return deterministic_partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)

        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

def analyze_quicksort_performance(sort_function, arr):
    start_time = time.time()
    sort_function(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

# Example usage and analysis
arr = [random.randint(1, 1000) for i in range(1000)]

# Analyzing deterministic QuickSort
deterministic_time = analyze_quicksort_performance(deterministic_quicksort, arr.copy())
print(f"Deterministic QuickSort took {deterministic_time:.6f} seconds")

# Analyzing randomized QuickSort
randomized_time = analyze_quicksort_performance(randomized_quicksort, arr.copy())
print(f"Randomized QuickSort took {randomized_time:.6f} seconds")
