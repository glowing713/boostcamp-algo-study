def solution(numbers, target):
    results = [0]
    for number in numbers:
        tmp = []
        for result in results:
            tmp.append(result + number)
            tmp.append(result - number)
        results = tmp
    
    return results.count(target)