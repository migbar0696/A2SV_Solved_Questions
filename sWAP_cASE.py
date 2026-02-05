def swap_case(s):
    res = []
    for ch in s:
        if ch.isupper():
            res.append(ch.lower())
        elif ch.islower():
            res.append(ch.upper())
        else:
            res.append(ch)
    return "".join(res)
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
