# MY APPROACH
def reverse_word(s):
    result = ""
    word = ""
    for c in s:
        if c != " ":
            word += c
        elif word:
            if result:
                result = word+" "+result
            else:
                result = word
            word = ""
    if word:
        if result:
            result = word + " " + result
        else:
            result = word
    return result


s1 = "the sky is blue"
s2 = "  hello world  "
s3 = "a good   example"
s4 = "sathish"
print(reverse_word(s4))