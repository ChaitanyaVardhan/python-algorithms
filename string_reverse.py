import sys


def string_reverse(s):
    if len(s) < 2:
        return s
    return s[len(s)-1] + string_reverse(s[0:len(s)-1])


if __name__ == "__main__":
    s = sys.argv[1]
    reverse_s = string_reverse(s)
    print(f"Reverse of {s}: {reverse_s}")
