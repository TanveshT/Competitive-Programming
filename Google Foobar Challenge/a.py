def solution(x, y):
      
    xDict = set()
    yDict = set()
    
    for i in x:
        xDict.add(i)
        
    for i in y:
        yDict.add(i)
        
    xLen = len(xDict)
    yLen = len(yDict)
    
    if yLen > xLen:
        return (yDict-xDict).pop()
    else:
        return (xDict-yDict).pop()

    

print(solution([13,5,6,2,5], [5,2,5,13]))