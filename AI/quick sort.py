import random
import time

def deterministic_quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x<pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x >pivot ]
    return deterministic_quicksort(left) +  middle + deterministic_quicksort(right)

def randomized_quicksort(arr):
    if len(arr)<=1:
        return arr
    
    pivot = random.choice(arr)
    left = [x for x in arr if x<pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x >pivot ]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)


if __name__ == "__main__":
    data_size =5000
    data = [random.randint(1,1000) for i in range(data_size)]


    start_time = time.time()
    sorted_data = deterministic_quicksort(data)
    end_time = time.time()
    deterministic_time = end_time - start_time


    start_time = time.time()
    randomized_sorted_data = randomized_quicksort(data)
    end_time = time.time()
    randomized_time = end_time - start_time

    print(f"Deterministic Quick Sort Time: {deterministic_time:.6f} seconds")
    print(f"Randomized Quick Sort Time: {randomized_time:.6f} seconds")