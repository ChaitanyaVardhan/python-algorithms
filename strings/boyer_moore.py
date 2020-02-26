import sys


def find_boyer_moore(T, P):
    n,m = len(T), len(P)
    if m == 0: return
    last = {}
    for k in range(m):
        last[P[k]] = k
    print(last)
    i = m - 1
    k = m - 1
    while i < n:
        print(f"i: {i}")
        if T[i] == P[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j+1)
            k = m - 1
    return -1

    
if __name__ == "__main__":
    input_str = sys.argv[1]
    input_pattern = sys.argv[2]
    pos = find_boyer_moore(input_str, input_pattern)
    print(f"idx: {pos}")
