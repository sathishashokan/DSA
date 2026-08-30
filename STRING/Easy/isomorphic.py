# Leet code Approach
def isomorphic(s,t):
    hash_s, hash_t = {}, {}
    for i in range(len(s)):
        if s[i] not in hash_s:
            hash_s[s[i]] = i
        if t[i] not in hash_t:
            hash_t[t[i]] = i

        if hash_s[s[i]] != hash_t[t[i]]:
            return False
    return True


s1 = "paper"
s2 = "title"
print(isomorphic(s1,s2))
