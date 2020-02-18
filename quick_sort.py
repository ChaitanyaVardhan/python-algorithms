import time


def quick_sort(arr):
    i = 1
    j = len(arr) - 1
    lo = 0
    hi = len(arr)
    v = arr[0]
    while True:
        while arr[i] <= v:
            i += 1
            if i == hi:
                break
        while arr[j] > v:
            j -= 1
            if j == lo:
                break
        arr[i], arr[j] = arr[j], arr[i]
        if i >= j:
            break        
    arr[0], arr[j] = arr[j], arr[0]
    return arr, j


if __name__ == "__main__":
    input_arr = []
    count = int(input())
    for i in range(count):
        input_arr.append(int(input()))

    start = time.time()
    sorted_arr, j = quick_sort(input_arr)
    print(sorted_arr)
    print(f"j:{j}")
    end = time.time()
    print(f"Time taken: {end-start}")
