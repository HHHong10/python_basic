import collections
def numJewelsInStones(jewels, stones):
    count = 0
    jewels = list(jewels)
    dict = collections.Counter(stones)

    for j in jewels:
        if j in dict.keys():
            count += dict[j]
    return count
    
    # dict = collections.Counter(stones)
    # for j in jewels:
    #     if j in dict.keys():
    #         count += dict[j]

    # return sum(map(stones.count, jewels)) # 시간은 더 걸림. 메모리적게 사용.


print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))