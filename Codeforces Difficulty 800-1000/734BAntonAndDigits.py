k2, k3, k5, k6 = map(int, input().split())
count = 0
count += 256*min(k2,k5,k6)
k2 -= min(k2,k5,k6)
count += 32*min(k2,k3)
print(count)