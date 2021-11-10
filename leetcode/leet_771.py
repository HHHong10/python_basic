import collections
def numJewelsInStones(jewels, stones):
    count = 0
    dict1 = collections.Counter(jewels).keys()
    dict2 = collections.Counter(stones)

    for k in dict1:
        if k in dict2.keys():
            count += dict2[k]

    # dict = collections.Counter(stones)
    # for j in jewels:
    #     if j in dict.keys():
    #         count += dict[j]
    return count
    # return sum(map(stones.count, jewels)) # 시간은 더 걸림. 메모리적게 사용.


print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))