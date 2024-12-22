

n = int(input())
arr = list(map(int, input().split()))

# out = sum(arr)
if len(arr) == 1:
    print(arr[0])
else:
    arr = [3*i for i in arr]
    print(sum(arr))