def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, partition_pos+1, right)
        quicksort(arr, left, partition_pos-1)

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i

def binary_search(arr, x, start_index = 0, end_index = None):
    if end_index == None:
        end_index = len(arr) - 1
    
    if start_index > end_index:
        return False
    
    midpoint = (start_index + end_index) // 2
    
    if x == arr[midpoint]:
        return f"Aradığınız elemanın sıralannmış listedeki indeksi:{midpoint}'dir "
    if x < arr[midpoint]:
        return binary_search(arr, x, start_index, midpoint - 1)
    if x > arr[midpoint]:
        return binary_search(arr, x, midpoint + 1, end_index)
#sample use
liste = [2,75,61,58,44,80,1,31,56,17,89]
quicksort(liste, 0, len(liste)-1)    
print(binary_search(liste, 80, 0, None))
print(f"Sıralanmış liste:{liste}")
