__author__ = 'kpeterson'

N, K = map(int, raw_input().split())

arr = map(int, raw_input().split())
sorted = []

while K > 0:
    maxNum = max(arr)
    if maxNum != arr[0]:
        indexSpot = arr.index(maxNum)
        arr[0], arr[indexSpot] = arr[indexSpot], arr[0]

    sorted.append(arr.pop(0))
    K -= 1

results = sorted + arr

print results
