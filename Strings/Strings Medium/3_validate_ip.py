# Validate an IP Address

def isValid(str):
    if str[0] == '.':
        return False
    
    count = 0
    ans = 0
    max_count = 0
    
    for i in range(len(str)):
        ch = str[i]
        
        if ch == '.':
            if i + 1 < len(str) and str[i + 1] == '.':
                return False
            count += 1
            ans = 0
            max_count = 0
        else:
            if '0' <= ch <= '9':
                digit = int(ch)
                if 0 <= ans <= 255:
                    if ans == 0 and max_count >= 1:
                        return False
                    ans = ans * 10 + digit
                    max_count += 1
                else:
                    return False
            else:
                return False
    
    if count == 3 and 0 <= ans <= 255:
        return True
    else:
        return False