def letter_combinations(digits):
    res = []
    hash_pad = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def backtrack(index, curr):
        if index == len(digits):
            res.append(curr[:])
            return

        for letter in hash_pad[digits[index]]:
            backtrack(index + 1, curr + letter)

    backtrack(0, "")
    return res

print(letter_combinations("23"))