N, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dst = [i for i in range(D+1)]

for i in range(D+1):
    dst[i] = min(dst[i], dst[i-1] + 1)

    for start, end, distance in graph:
        if i == start and end <= D and dst[i] + distance < dst[end]:
            dst[end] = dst[i] + distance
print(dst[D])

'''
graph = [
  # start, end, distance
    [0, 50, 10], 
    [0, 50, 20], 
    [50, 100, 10], 
    [100, 151, 10], 
    [110, 140, 90]
    ]
'''