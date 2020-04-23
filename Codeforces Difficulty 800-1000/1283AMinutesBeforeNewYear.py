t = int(input())
for _ in range(t):
    hh, mm = map(int, input().split())
    print(((23-hh)*60) + (60-mm))