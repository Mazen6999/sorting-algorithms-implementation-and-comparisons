import numpy as np
import time

# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]

begin = time.time()


def select(arr, l, r):
    indexing_length = range(l, r)
    for i in indexing_length:
        minIdx = i
        for j in range(i + 1, r + 1):
            if arr[j] < arr[minIdx]:
                minIdx = j
        if minIdx != i:
            arr[minIdx], arr[i] = arr[i], arr[minIdx]


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r,threshold):
    if l < r and r - l > threshold:
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m,threshold)
        mergeSort(arr, m + 1, r,threshold)
        merge(arr, l, m, r)
    if r - l <= threshold:
        select(arr, l, r)



arr = np.random.randint(1, 100, 50)
n = len(arr)
mergeSort(arr, 0, n - 1,6)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i], end=" ")
finish = time.time()
print(f"\nTotal runtime of the program is {finish - begin}")
