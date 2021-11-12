from collections import deque



def solution(n, flights, src, dst, k):
    answer = 0
    dist = [100000] * n
    graph = [[] for _ in range(n)]
    for [a, b, c] in flights:
        graph[a].append([b, c])

    Queue = deque()
    dist[src] = 0
    Queue.append([src, 0])

    L = 0
    while Queue:
        qlen = len(Queue)
        for _ in range(qlen):
            x = Queue.popleft()
            now = x[0]
            nowcost = x[1]
            for [nx, nprice] in graph[now]:
                if nowcost + nprice < dist[nx]:
                    dist[nx] = nowcost + nprice
                    Queue.append([nx, dist[nx]])
        L+=1
        if L > k:
            break

    if dist[dst] == 100000:
        answer = -1
    else:
        answer = dist[dst]

    return answer


# print(solution(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
# print(solution(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
# print(solution(2, [[0,1,2]], 1, 0, 0))
print(solution(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1))
