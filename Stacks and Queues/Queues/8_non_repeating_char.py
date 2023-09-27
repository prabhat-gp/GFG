# Queue based approach or first non-repeating character in a stream.

from collections import deque

def FirstNonRepeating(A):
    i = 0
    x = []
    q = deque()
    map = {}

    while i < len(A):
        if A[i] in map:
            map[A[i]] += 1
        else:
            map[A[i]] = 1
            q.append(A[i])

        while q and map[q[0]] > 1:
            q.popleft()

        x.append(q[0] if q else '#')
        i += 1

    return ''.join(x)