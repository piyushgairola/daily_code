"""
Date: 22-7-2021
Problem: 838. Push Dominoes [https://leetcode.com/problems/push-dominoes/]
"""

def pushDominoes(dominoes):
    n = len(dominoes)
    dist = [0]*n
    res = list(dominoes)

    rdist = None
    for i,val in enumerate(dominoes):
        if val == "R":
            rdist=0
        elif val == "L":
            rdist = None
        
        elif rdist != None:
            rdist += 1
            dist[i] = rdist
            res[i] = "R"


    ldist = None
    for i in range(n-1,-1,-1):
        if dominoes[i] == "L":
            ldist = 0

        elif dominoes[i] == "R":
            ldist = None

        elif ldist != None:
            ldist +=1
            if ldist < dist[i] or res[i] == ".":
                res[i] = "L"
            elif ldist==dist[i]:
                res[i] = "."

    return "".join(res)

dom = ".L.R...LR..L.."
print(pushDominoes(dom))


