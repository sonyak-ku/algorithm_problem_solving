import re
def solution(new_id):
    special_char = {'-', '_', '.'}
    first_step_id = new_id.lower()

    second_step_id = ''
    for char in first_step_id:
        if char.isalnum() or char in special_char:
            second_step_id += char

    thir_step_id = re.sub('[.]+', '.', second_step_id) # 여기가 틀림, 두번 이상연속된 부분임

    four_step_id = thir_step_id.strip('.')

    fiv_step_id = 'a' if four_step_id == '' else four_step_id

    six_step_id = fiv_step_id[:15].strip('.')

    while len(six_step_id) < 3:
        six_step_id += six_step_id[-1]

    return six_step_id

print(solution("SHDKsdkha__......dhs..skhq.."))

