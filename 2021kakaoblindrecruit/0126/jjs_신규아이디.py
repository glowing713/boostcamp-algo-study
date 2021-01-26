import re

def solution(new_id):
    answer = new_id.lower()
    answer = re.sub("[^a-z0-9-_.]", "", answer)
    answer = re.sub("[.]{2,}", ".", answer)
    answer = answer.strip(".")
    
    if not answer:
        answer = "a"
        
    if len(answer) >= 16:
        answer = answer[:15].rstrip(".")
        
    if len(answer) <= 2:
        n_need = 3 - len(answer)
        answer = answer + answer[-1]*n_need
        
    return answer