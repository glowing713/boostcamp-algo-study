def dfs(begin, target, words):
    visit = [0]*len(words)
    result = 0
    stack = [begin]
    while stack:
        now = stack.pop()
        if now == target:
            return result
        for i in range(len(words)):
            count = 0
            for x,y in zip(now,words[i]):
                if x != y:
                    count += 1
            if count == 1:
                if visit[i] != 0:
                    continue
                visit[i] = 1
                stack.append(words[i])
        result += 1



def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    answer = dfs(begin, target, words)
    
    return answer