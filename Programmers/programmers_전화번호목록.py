# 테스트 케이스 전체 통과, 효율성 테스트 2/4
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        sub = phone_book[i]
        sublen = len(sub)
        if sub == phone_book[i+1][:sublen]:
            return False
    return True

    # for p in phone_book:
    #     plen = len(p)
    #     cnt = 0
    #     for y in phone_book:
    #         if len(y) < plen:
    #             continue
    #         elif y[:plen] == p:
    #             cnt+= 1
    #     if cnt > 1:
    #         return False

    # phone_book = sorted(phone_book, key= lambda x: len(x))
    # plen = len(phone_book)

    # for i in range(plen):
    #     cnt = 0
    #     sub = phone_book[i]
    #     sublen = len(sub)
    #     for j in range(i+1, plen):
    #         if phone_book[j][:sublen] == sub:
    #             cnt += 1
    #     if cnt > 0:
    #         return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))