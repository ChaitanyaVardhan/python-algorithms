import time


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    arr_lh = arr[0:mid]
    arr_rh = arr[mid:len(arr)]
    # print(arr_lh)
    # print(arr_rh)
    arr_lh = merge_sort(arr_lh)
    arr_rh = merge_sort(arr_rh)
    merged_arr = merge(arr_lh, arr_rh)
    # print(merged_arr)
    return merged_arr


def merge(arr1, arr2):
    i = 0
    j = 0
    k = 0
    aux = [0] * (len(arr1) + len(arr2))
    while True:
        if (i + j) == len(arr1) + len(arr2):
            break
        if i == len(arr1):
            aux[k] = arr2[j]
            j += 1
            k += 1
        elif j == len(arr2):
            aux[k] = arr1[i]
            i += 1
            k += 1        
        elif arr1[i] < arr2[j]:
            aux[k] = arr1[i]
            i += 1
            k += 1
        else:
            aux[k] = arr2[j]
            j += 1
            k += 1
    return aux


if __name__ == "__main__":
    arr1 = []
    l1 = int(input())
    for i in range(l1):
        arr1.append(int(input()))    
    start = time.time()
    sorted_array = merge_sort(arr1)
    end = time.time()
    print(f"Total time: {end-start}")
    for i in range(len(sorted_array)):
        print(sorted_array[i])
    
