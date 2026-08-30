def phone_pad(p, up):
    if not up:
        print(p)
        return
    digit = int(up[0])
    for i in range((digit-1)*3, digit*3):
        s = chr(97+i)
        phone_pad(p+s, up[1:])

def phone_pad_list(p, up):
    if not up:
        res = [p]
        return res
    digit = int(up[0])
    final = []
    for i in range((digit-1)*3, digit*3):
        s = chr(97+i)
        final.extend(phone_pad_list(p+s, up[1:]))
    return final

def phone_pad_count(p, up):
    if not up:
        return 1
    digit = int(up[0])
    count = 0
    for i in range((digit-1)*3, digit*3):
        s = chr(97+i)
        count += phone_pad_count(p+s, up[1:])
    return count

s = "12"
phone_pad("", s)
print(phone_pad_list("", s))
print(phone_pad_count("", s))