def get_roots(h):

    dictionary = {}

    level = 0

    roots = [2**h-1]

    ele = 2**h

    dictionary[roots[0]]= -1

    while(level < h-1):

        children = []
        for x in roots:
            children.append(x-(ele//2))
            children.append(x-1)
            dictionary[x-1] = x
            dictionary[x-(ele//2)] = x
        
        roots = children
        level += 1
        ele = (ele+1)//2

    return dictionary

def solution(h,q):

    result = []
    rootDict = get_roots(h)

    for x in q:
        result.append(rootDict[x])

    return result

