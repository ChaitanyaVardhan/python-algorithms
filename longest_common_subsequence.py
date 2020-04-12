def compute_lcs(s1, s2):
    # print("s1, s2: {} {}".format(s1, s2))
    if s1 == "" or s2 == "":
        return ""
    
    if s1[len(s1) - 1] == s2[len(s2) - 1]:
        s = compute_lcs(s1[0:len(s1) - 1], s2[0:len(s2) - 1]) + s1[len(s1) - 1]
    else:
        cand1 = compute_lcs(s1, s2[0:len(s2) - 1])
        cand2 = compute_lcs(s1[0:len(s1) - 1], s2)
        if len(cand1) > len(cand2):
            s = cand1
        else:
            s = cand2

    return s


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        s1, s2 = [s for s in input().split(" ")]
        s = compute_lcs(s1, s2)
        print("Case #{}: {}".format(str(i+1), s))
    
        
