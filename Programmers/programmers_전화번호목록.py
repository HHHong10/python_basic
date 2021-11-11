def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        sub = phone_book[i]
        sublen = len(sub)
        if sub == phone_book[i+1][:sublen]:
            return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))