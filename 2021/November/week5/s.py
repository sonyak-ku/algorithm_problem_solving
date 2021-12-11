def solution(numbers, target):  # 숫자는 리스트로 나옴, target 과 같은 숫자인지 확인해야 함
    answer_list = []

    for i, number in enumerate(numbers):
        if i == len(numbers) - 1:
            count = get_numbers(number, answer_list, target, True)
            return count
        else:
            answer_list = get_numbers(number, answer_list, target, False)

def get_numbers(number, li, target, flag):
    answer = []
    count = 0
    if flag:
        for l in li:
            if l + number == target:
                count += 1
            if l - number == target:
                count += 1
        return count
    else:
        for l in li:
            answer.append(l + number)
            answer.append(l - number)
        return answer
