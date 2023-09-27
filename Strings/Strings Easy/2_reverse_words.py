# Reverse words in a given string

def reverseWords(str):
    ans = ""
    t = ""

    n = len(str)
    for i in range(n - 1, -1, -1):
        if str[i] != '.':
            t = str[i] + t
        else:
            ans = ans + t + str[i]
            t = ""
    
    ans = ans + t
    return ans

str = "i.like.this.program.very.much"
print(reverseWords(str))
# Output = much.very.program.this.like.i

