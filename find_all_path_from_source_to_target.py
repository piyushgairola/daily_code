"""
Date: 08-06-2021
Author: Piyush Gairola
Problem Statement: 797. All Paths From Source to Target [https://leetcode.com/problems/all-paths-from-source-to-target/]
"""


def allPath(graph):
    def dfs(curr_node, path_covered):
        if curr_node == n:
            res.append(path_covered)
        else:
            for child in graph[curr_node]:
                dfs(child, path_covered+[child])

    n = len(graph)
    res=[]
    dfs(0,[0])

    return res