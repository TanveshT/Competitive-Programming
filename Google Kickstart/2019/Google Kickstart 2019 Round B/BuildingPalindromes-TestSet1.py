# Ran Succesfully on Test Set 1

t = int(input())
result = []

for _ in range(t):

    n, q = map(int, input().split())
    s = input()

    numberOfYes = 0
    
    for i in range(q):

        l, r = map(int, input().split())
        unique = {}

        for j in range(l-1, r):
            if s[j] not in unique:
                unique[s[j]] = 0
            unique[s[j]] += 1

        noOfLettersInSub = r-l+1

        if noOfLettersInSub == 1:
            numberOfYes += 1
        elif noOfLettersInSub % 2 == 0:
            #FOR EVEN
            flag = True
            for x in unique:
                if unique[x] % 2 != 0: flag = False; break

            if flag: numberOfYes += 1
        else:
            #FOR ODD
            oddFlag = False
            flag = True

            for x in unique:
                if unique[x] % 2 != 0: 
                    if oddFlag: flag = False; break
                    oddFlag = True

            if flag: numberOfYes += 1

    result.append(numberOfYes)

for i in range(t):
    print("Case #"+str(i+1)+":", result[i], sep = " ")
