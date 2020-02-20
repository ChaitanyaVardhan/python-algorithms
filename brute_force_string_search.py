def brute_force(string, pattern):
    l = len(pattern)
    j = 0
    start = 0
    print(f"len of string: {len(string)}")
    print(f"len of pttern: {len(pattern)}")
    while j < len(string) - len(pattern):
        i = 0
        j = start
        print(f"i: {i}")
        print(f"j: {j}")
        while (pattern[i] == string[j]
               and i < len(pattern)):
            i += 1
            j += 1
        if i == l:
            return start
        else:
            start += 1
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
    index = brute_force(input_str, pattern)
    print(f"index {index}")
