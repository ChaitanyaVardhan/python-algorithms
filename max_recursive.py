def max_recursive(S):
    if len(S) < 2:
        return S[0]

    a = S[0]
    b = max_recursive(S[1:])
    if a > b:
        return a
    else:
        return b

    
if __name__ == "__main__":
    count = int(input())
    S = []
    for _ in range(count):
        S.append(int(input()))
    max = max_recursive(S)
    print(f"Max is {max}")
