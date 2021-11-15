def solution(phone_book):  # N = 100 만 -> 접두어!! O(N) 으로만 풀어야 댐.
    hashs = {}
    phone_book.sort()
    # 이 해싱의 단점은 119 랑 191 이랑 저장하는 해싱값을 똑같이 본다는 점 -> enumerate 로 숫자 곱해서 저장 -> 답이 소수가 틀린거보니 이거도 겹치는 부분이 잇나봐(12 == 21 같게봄)
    for book in phone_book:
        l = len(book) - 1
        item = ''
        for i, num in enumerate(book):
            item += num
            if hashs.get(item, 0):  # 0 이 나오지 않을 때 -> 접두라는 뜻!
                return False
        hashs[book] = 1  # 해시 숫자를 1 로 저장한다.
    ## 1191 이 먼저오고, 그다음 119 가 나올때 true 가 나올듯 --> 잡아내지 못함 --> 이래서 hash() 를 쓰는건가? -> 정렬하고 풀면 될듯?

    return hashs
# print(hash(4))
print(solution(["1191", "119"]))