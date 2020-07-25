# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    output = ""
    i = 0
    while i < len(l1):
        if s[i] in s2:
            val = s[i]
            while val not in s2:
                i += 1
                if i >= len(s1):
                    if len(val) > len(output) or (len(val) == len(output) and val < output):
                        output = val
                    break
                val += s[i]
            if len(val) > len(output) or (len(val) == len(output) and val < output):
                    output = val
        i += 1
    return output
