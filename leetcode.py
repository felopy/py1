#14
def longest(ml):
    mk = ""
    ml.sort(key = len)
    mk = ml[0]
    l = 0
    for i in ml:
        if mk in i[:len(mk)]:
            l += 1
        if l == len(ml):
            return mk
    return None
m = ['amdsaa','am','amvor',"kam"]
print(longest(m))

#15
def roman_int(s):
    m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    c = 0

    if len(s) > 15:
        return "error value"

    i = 0
    while i < len(s):
        if s[i] in m:
            if i < len(s) - 1 and s[i:i+2] in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                c += m[s[i+1]] - m[s[i]]
                i += 2  # Skip the next character
            else:
                c += m[s[i]]
                i += 1
        else:
            return "Invalid Roman numeral"
    if c > 3999:
        return "Big value"
    else:
        return c

print(roman_int(input("Enter Roman numeral: ")))

