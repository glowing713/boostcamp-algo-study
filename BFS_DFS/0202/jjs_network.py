def solution(n, computers):
    network = 0
    connected = set()
    # 전체 컴퓨터를 순서대로 확인
    for i in range(n):
        if i in connected: # 이미 연결됐으면 다음으로
            continue
        
        # 연결이 안돼있으면 새로운 네트워크의 첫 컴퓨터
        network += 1
        connected.add(i)
        stack = [i]
        while stack:
            com = stack.pop()
            for other, direct in enumerate(computers[com]):
                # direct는 두 컴퓨터의 직접 연결 여부
                # other가 com과 direct고, 연결에 포함돼있지 않으면
                if direct and (other not in connected):
                    connected.add(other)
                    stack.append(other)
    return network