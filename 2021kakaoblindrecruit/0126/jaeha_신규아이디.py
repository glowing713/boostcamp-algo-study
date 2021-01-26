import re
def solution(new_id):
    answer = ''
    new_id = new_id.lower() #1

    new_id = re.sub('[^a-z0-9-_.]',  '', new_id) #2

    new_id = re.sub('\.{2,}', '.', new_id) #3

    new_id = re.sub('^\.|\.$', '', new_id) #4

    if not new_id:
        new_id += 'a' #5

    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = re.sub('\.$', '', new_id) #6
  
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
  
    answer = new_id
    return answer