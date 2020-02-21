import time


def merge_sort(S):
    if len(S) < 2:
        return
    n = len(S)
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)


def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and (S1[i] < S2[j])):
            S[j+i] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1
            

if __name__ == "__main__":
    count = int(input())
    arr = []
    for _ in range(count):
        arr.append(int(input()))
    start = time.time()
    merge_sort(arr)
    end = time.time()
    print(f"Time taken: {end-start}")
    for i in range(len(arr)):
        print(arr[i])

                   
    

                   
                   
                   
