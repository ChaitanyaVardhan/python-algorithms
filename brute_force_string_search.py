def brute_force(S, P):
    l = len(P)
    i = 0
    start = 0
    while start < len(S) - len(P):
        while True:
            print(f"i: {i}")
            print(f"start: {start}")            
            if P[i] == S[start+i]:
                i += 1
            else:
                break
            if i == l:
                return start
        start += 1
        i = 0
    return -1


if __name__ == "__main__":
    pattern = input()
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    input_str = " ".join(line for line in lines)
    print(f"pattern: {pattern}")
    print(f"String: {input_str}")
    print(f"len of string: {len(S)}")
    print(f"len of pttern: {len(P)}")    
    index = brute_force(input_str, pattern)
    print(f"index {index}")
    print(f"inbuilt: {input_str.find(pattern)}")
