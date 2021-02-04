from collections import deque

def convertible(word, candi):
    # same length
    diff = 0 # diff > 0 (no same word)
    for i, ch in enumerate(word):
        if ch != candi[i]:
            diff += 1
        if diff > 1:
            return False
    return True

def solution(begin, target, words):
    if target not in words:
        return 0
    
    # begin != target
    # same word lengths
    visit = {begin} # not set(begin)
    queue = deque()
    queue.append((0, begin))
    while queue:
        step, word = queue.popleft()
        for candi in words:
            if candi in visit:
                continue
            elif not convertible(word, candi):
                continue
            elif candi == target:
                return step + 1
            else:
                visit.add(candi)
                queue.append((step + 1, candi))
    return 0