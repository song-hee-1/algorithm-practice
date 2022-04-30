# 테스트는 통과하였으나 정확성 및 효율성 테스트에서 실패
def solution1(phone_book):
    standard = phone_book[0]
    num = 0
    for x in phone_book[1:]:
        if standard in x:
            num += 1
            break
    if num == 0:
        return True
    else:
        return False


# startswith 이용 -> 테스트는 통과하였으나 정확성 및 효율성 테스트에서 실패
def solution2(phone_book):
    phone_book = sorted(phone_book)
    std = phone_book[0]
    for x in phone_book[1:]:
        if x.startswith(std):
            return False
    return True


# startswith + zip 이용 -> 정확성 및 효율성 테스트에서 또 실패
def solution3(phone_book):
    phone_book = sorted(phone_book)
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
        return True


# sort를 하지 않
# list안의 요소들을 모두 확인하여 그 중 하나라도 다른 요소의 접두어인 경우가 있을때만 false로 반환하는 점을 적절히 표현하지 못함

# Hash를 이용 - 통과
def solution4(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
