"""
핵심: 행렬을 그래프로 볼 수 있다.
- 인접 정점끼리 간선으로 연결되어 있다.
- 정점의 id는 행렬에서의 인덱스로 계산한 r*N+c 값으로 줄 수 있다.
- 인접 정점의 인덱스 r', c'가 범위에 들어오는 지 확인해야 한다.
  패딩을 이용할 수도 있다.
"""

import sys
from collections import defaultdict

root = {}

def find(x):
    """
    목표: x의 root를 찾는다.
    - 경로압축: x에서 root까지의 모든 노드의 root를 찾는다.
      (path의 모든 노드들을 저장해놓고, root를 할당하는 것과 같다.)
    """
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]

def union(r1, r2):
    """
    목표: 두 root를 하나로 합친다. (r2를 r1 아래에 둔다.)
    """
    root[find(r2)] = find(r1)

def adj(p, W):
    yield p - W
    yield p - 1
    yield p + 1
    yield p + W

def main():
    # 1. 데이터 입력 및 가공
    input = sys.stdin.readline
    
    # 패딩을 위해 P와 W를 사용한다.
    # 4방향의 이웃들에 대해, 패딩인 이웃은 무시하고 넘어가게 된다.
    N = int(input()) # 원래 한 열의 크기
    P = 1            # 4방향 패딩 크기
    W = N + 2*P      # 패딩된 한 열의 크기

    h2i = defaultdict(list) # 높이별 위치의 인덱스들
    for r in range(P, N+P):
        heights_line = list(map(int, input().split()))
        for h, i in zip(heights_line, range(r*W+1, (r+1)*W-1)):
            h2i[h].append(i)
    
    # 2. 메인 프로세스
    # 땅의 높이 heights에 대해 for문을 돌며, 물의 높이는 h - 1라고 놓는다.
    
    # 땅의 높이를 내림차순으로 정렬한다.
    # 그러면 물의 높이도 줄어들면서 진행하는데,
    # 한 번 물에 잠기지 않은 지역은 끝까지 물에 잠기지 않는다.
    heights = sorted(h2i, reverse=True)
    
    heights.pop() # 최저 높이 heights[-1]에 대해서는 모두 잠기지 않음, cnt = 1 (= min_cnt)
    cnt = 1
    rep = []
    for h in heights: # 물의 높이 = h - 1
        # root 초기화
        for i in h2i[h]:
            root[i] = i
        
        # 현재 위치(의 인덱스 i)를 특정 인접 위치들의 root로 만든다.
        # 인접 위치(의 인덱스 j)가 root를 가져야 한다.
        # (이전과 현재 높이의 위치들이 포함될 것이다.)
        for i in h2i[h]:
            for j in adj(i, W):
                if j in root:
                    union(i, j)
                    
        # 스스로 root인 위치를 구역의 대표로 사용한다.
        # 이전까지의 대표 중, 아직도 대표인 것
        rep = [i for i in rep if root[i] == i]
        # 현재 높이의 위치 중, 대표인 것
        for i in h2i[h]:
            if root[i] == i:
                rep.append(i)
        cnt = max(cnt, len(rep))

    print(cnt)

main()