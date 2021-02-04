from collections import deque


def canChange(b_word: str, t_word: str) -> bool:
    cnt = 0
    for i in range(len(b_word)):
        if b_word[i] != t_word[i]:
            cnt += 1
        if cnt > 1:
            return False
    return True


def solution(begin, target, words):
    answer = 99999999
    queue = deque()  # 큐 만들기
    visited = [0 for _ in range(len(words))]  # 방문처리
    
    if target not in words:
        return 0
    
    for i, w in enumerate(words):
        if canChange(begin, w):  # 한 자리 문자만 바뀐 경우
            visited[i] = 1  # 방문처리
            queue.append((i, 1))  # 시작점 큐에 담기
    
    while queue:
        now_idx, now_cnt = queue.popleft()
        if words[now_idx] == target:
            if now_cnt < answer:
                answer = now_cnt
        
        for i, w in enumerate(words):
            if canChange(words[now_idx], w) and not visited[i]:
                visited[i] = 1  # 방문처리
                queue.append((i, now_cnt + 1))  # 시작점 큐에 담기

    return answer
