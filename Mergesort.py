# Python program for implementation of Insertion Sort
import numpy as np
import time
begin = time.time()
# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key


# Driver code to test above
arr = np.random.randint(1,10000,100000)
insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i])
finish = time.time()
A=(finish-begin)*1000000
print(f"\nTotal runtime of the program is {A}")