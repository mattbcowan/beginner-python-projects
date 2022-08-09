def isAnagram(s: str, t: str) -> bool:
    s_dict = {}

    if len(s) != len(t):
        return False

    for ltr in s:
        if ltr in s_dict:
            s_dict[ltr] += 1
        else:
            s_dict[ltr] = 1

    for ltr in t:
        if ltr in s_dict and s_dict[ltr] > 0:
            s_dict[ltr] -= 1
        else:
            return False

    return True


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram("racecar", "acerrac"))
print(isAnagram("dsfsdf", "lol"))
