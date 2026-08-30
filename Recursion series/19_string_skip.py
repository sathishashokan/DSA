# to skip the char in a string


def skip_a_char(s, res):
    if not s:
        print(res)
        return

    if s[0] == "a":
        skip_a_char(s[1:], res)
    else:
        skip_a_char(s[1:], res + s[0])


# to skip a word in a string

def skip_a_word(s, res):
    if not s:
        print(res)
        return

    if s.startswith("apple"):
        skip_a_word(s[5:], res)
    else:
        skip_a_word(s[1:], res + s[0])

# to skip a word in a string if it is not start of a particular string

def skip_a_word_if_not(s, res):
    if not s:
        print(res)
        return

    if s.startswith("app") and not s.startswith("apple"):
        skip_a_word_if_not(s[3:], res)
    else:
        skip_a_word_if_not(s[1:], res + s[0])

s = "abcappledc"
skip_a_word(s, "")