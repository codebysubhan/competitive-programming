n = int(input())
arr = list(map(int, input().split()))
print(arr)
arr.sort()
def toast(tot,inp):
    tot += sum(inp)
    return (tot, inp)
def apple(grp):
    if len(grp)<=1:
        return grp
    mid = len(arr)//2
    return (grp[:mid], grp[mid:])


print(apple(arr))

