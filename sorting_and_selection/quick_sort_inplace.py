import time


def quick_sort_inplace(S,a,b):
    # sort array S with start index a and 
    # end index b including elem at b
    
    if b - a < 1:
        return
    
    left = a
    right = b - 1
    pivot = S[b]
    while left <= right:
        while left <= right and S[left] <= pivot:
            left += 1
        while left <= right and S[right] > pivot:
            right -= 1
        if left > right:
            S[left], S[b] = S[b], S[left]
        else:
            S[left], S[right] = S[right], S[left]

    quick_sort_inplace(S,a,left-1)
    quick_sort_inplace(S,left+1,b)

    
if __name__ == "__main__":
    count = int(input())
    input_arr = []
    for _ in range(count):
        input_arr.append(int(input()))
    start = time.time()
    quick_sort_inplace(input_arr,0,len(input_arr)-1)
    end = time.time()
    print(f"Time taken to sort {len(input_arr)} ints: {end-start}")
    for i in range(len(input_arr)):
        print(input_arr[i])
