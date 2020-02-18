def main():
    arr1 = []
    l1 = int(input())
    for i in range(l1):
        arr1.append(int(input()))
    mid = l1 // 2
    print(arr1[0:mid])
    print(arr1[mid:l1])    
    half1 = divide(arr1[0:mid])
    half2 = divide(arr1[mid:l1])
    merged_arr = merge(half1, half2)
    print(merged_arr)


def divide(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    h1 = divide(arr[0:mid])
    h2 = divide(arr[mid:len(arr)])
    merged_arr = merge(h1, h2)
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
    main()
