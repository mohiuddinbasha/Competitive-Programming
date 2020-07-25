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
    while i < len(s1):
        if s1[i] in s2:
            val = s1[i]
            j = i
            while val not in s2:
                j += 1
                if j >= len(s1):
                    if len(val) > len(output) or (len(val) == len(output) and val < output):
                        output = val
                    i = j
                    break
                val += s1[j]
            if len(val) > len(output) or (len(val) == len(output) and val < output):
                    output = val
        i += 1
    return output
print(longestcommonsubstring("abcdef","abqrcdest"))
