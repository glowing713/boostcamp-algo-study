import re


def to_lower(id):
    return id.lower()


def make_clear_sentence(raw_id):
    return re.sub('[^a-z0-9-_.]', '', raw_id)


def make_single_close(raw_id):
    return re.sub('[.]{2,1000}', '.', raw_id)
    # '^\.|\.$'
    # {2, }


def del_frnt_end_close(raw_id):
    # if len(raw_id) > 0 and raw_id[0] == '.':
    #     raw_id = raw_id[1:]
    # if len(raw_id) > 0 and raw_id[-1] == '.':
    #     raw_id = raw_id[:-1]
    # return raw_id
    return raw_id.strip('.')


def make_emty_str_a(raw_id):
    if len(raw_id) == 0:    # 이거 if not raw_id로 할 수 있음!!
        return 'a'
    else:
        return raw_id


def make_str_shorter(raw_id):
    if len(raw_id) > 15:
        raw_id = raw_id[:15]
    return del_frnt_end_close(raw_id)


def make_str_longer(raw_id):
    if len(raw_id) < 3:
        raw_id = raw_id + raw_id[-1]*(3-len(raw_id))
    return raw_id


def solution(new_id):
    answer = ''
    answer = to_lower(new_id)  # 소문자로 치환
    answer = make_clear_sentence(answer)  # 2
    answer = make_single_close(answer)  # 3
    answer = del_frnt_end_close(answer)  # 4
    answer = make_emty_str_a(answer)  # 5
    answer = make_str_shorter(answer)  # 6
    answer = make_str_longer(answer)  # 7

    return answer
