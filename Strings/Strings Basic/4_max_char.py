# Maximum Occuring Character

def getMaxOccurringChar(str):
    n = len(str)
    cnt = 0
    map = {}

    for ch in str:
        map[ch] = map.get(ch, 0) + 1
        if cnt < map[ch]:
            cnt = map[ch]
            maxOccur = ch
        elif cnt == map[ch] and maxOccur > ch:
            maxOccur = ch
            
    return maxOccur
