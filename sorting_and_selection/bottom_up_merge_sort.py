import time
import math


def merge(src, result, start, inc):
    end1 = start + inc
    end2 = min(start + 2*inc, len(src))
    x, y, z = start, start + inc, start
    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z] = src[x]
            x += 1
        else:
            result[z] = src[y]
            y += 1
        z += 1
    if x < end1:
        result[z:end2] = src[x:end1]
    else:
        result[z:end2] = src[y:end2]


def merge_sort(S):
    n = len(S)
    logn = math.ceil(math.log(n,2))
    src, dest = S, [None] * n
    for i in (2**k for k in range(logn)):
        for j in range(0, n, 2*i):
            merge(src, dest, j, i)
        src, dest = dest, src

    if S is not src:
        S[0:n] = src[0:n]

        
if __name__ == "__main__":
    count = int(input())
    input_arr = []
    for _ in range(count):
        input_arr.append(int(input()))
    start = time.time()
    merge_sort(input_arr)
    end = time.time()
    print(f"Num of ints: {len(input_arr)} Time taken {end-start}")
    for i in range(len(input_arr)):
        print(input_arr[i])
