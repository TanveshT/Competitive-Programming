n = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)

count = 0
for i in range(0, n , 2):
    count += (max(arr[i], arr[i+1]) - min(arr[i], arr[i+1]))
    
print(count)