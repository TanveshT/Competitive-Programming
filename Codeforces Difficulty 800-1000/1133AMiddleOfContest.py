h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))

start = h1*60 + m1
end = h2*60 + m2

mid = (end - start)//2

h3, m3 = h1+mid//60, m1 + mid%60

if m3 >= 60:
    m3 -= 60
    h3 += 1

print(f"{h3:02}", f"{m3:02}", sep = ":")