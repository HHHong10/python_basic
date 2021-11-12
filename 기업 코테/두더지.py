import collections



n = int(input())
du = {}
ducnt = n*n
maxt = 0
# 내 풀이
# for i in range(ducnt):
#     x = input()
#     c, r = map(int, x[:4].split())
#     sub = list(map(int, x[4:].split()))
#     maxt = max(maxt, max(sub))
#     du[c] = sub

# answer = 0
# for t in range(1, maxt+1):
#     maxs = 0
#     for [k, v] in du.items():
#         if t in v:
#             maxs = max(maxs, k)
#     answer += maxs

# 강사님 해설로
du = collections.defaultdict(list)
for i in range(ducnt):
    x = input()
    c, r = map(int, x[:4].split())
    sub = list(map(int, x[4:].split()))
    for s in sub:
        du[s].append(c)

answer = 0
for score in du.values():
    answer += max(score)

print(answer)