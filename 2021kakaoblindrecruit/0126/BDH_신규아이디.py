import re


def solution(new_id):
    answer = new_id

    # 1단계
    answer = answer.lower()

    # 2단계
    answer = re.sub('[^a-z0-9-_.]', '', answer)

    # 3단계
    # 그냥 . ==> 모든 문자, \. ==> 점
    answer = re.sub('\.+', '.', answer)

    # 4단계
    answer = answer.strip('.')

    # 5단계
    if not answer:
        answer = 'a'

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    answer = answer.rstrip('.')

    # 7단계
    if len(answer) <= 2:
        last_char = answer[-1]
        while len(answer) < 3:
            answer += last_char

    return answer