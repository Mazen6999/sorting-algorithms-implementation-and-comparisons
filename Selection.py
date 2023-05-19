import numpy as np
import time
begin = time.time()
def select(arr):
    indexing_length =range(0,len(arr)-1)
    for i in indexing_length:
        minIdx=i
        for j in range (i+1,len(arr)):
            if arr[j]<arr[minIdx]:
                minIdx=j
        if minIdx!=i:
         arr[minIdx], arr[i]=arr[i], arr[minIdx]

arr = np.random.randint(-20,100,50)
n = len(arr)
select(arr)
print("\n\nSorted array is")
for i in range(n):
	print("%d" % arr[i])
finish = time.time()
print(f"\nTotal runtime of the program is {finish - begin}")