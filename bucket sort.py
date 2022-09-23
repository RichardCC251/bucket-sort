import random
 
def bucketSort(array):
    largest = max(array)
    length = len(array)
    size = largest/length
 
    buckets = [[] for i in range(length)]
 
    for i in range(length):
        index = int(array[i]/size)
        if index != length:
            buckets[index].append(array[i])
        else:
            buckets[length - 1].append(array[i])
 
 
    for i in range(len(array)):
        buckets[i] = sorted(buckets[i])
 
 
    
    result = []
    for i in range(length):
        result = result + buckets[i]
             
    return result
 
 
arr = [20, 14, 12, 17, 8, 55, 12, 21, 34, 55, 81, 42]
output = bucketSort(arr)
print(output)