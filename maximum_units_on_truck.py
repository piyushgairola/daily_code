"""
Date: 14-06-2021
Author: Piyush Gairola
Problem: 1710. Maximum Units on a Truck [https://leetcode.com/problems/maximum-units-on-a-truck/]
"""

def maximumUnits(boxTypes, truckSize):
    boxTypes = sorted(boxTypes, key= lambda x: x[1], reverse= True)
    ans = 0

    for box, units in boxTypes:
        if truckSize >0:
            if box <= truckSize:
                ans += box*units
                truckSize -= box

            else:
                ans += truckSize*units
                break

    return ans