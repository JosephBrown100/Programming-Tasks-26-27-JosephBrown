"""
TASK: 03 Grid Path Counter

# Grid Path Counter - https://bk2coady.medium.com/daily-coding-problem-62-bfe0e398247b
Given an NxM grid:
- Count paths using recursion
- Count paths using iteration
Movement allowed: RIGHT or DOWN only.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random

def main(n,m):
    print(countpathsr(n,m))
    print(countpathi(n,m))


def countpathi(n,m):
    grid = [[1]*m for _ in range[n]]
    for row in range(1,n):
        for col in range(1,m):
            grid[row][col]= grid[row-1][col]+grid[row][col-1]
    return grid[n-1][m-1]

def countpathsr(n,m):
    if n==1 or m==1:
        return 1
    return countpathsr(n-1,m) + countpathsr(n,m-1)



            



if __name__ == "__main__":
    num = int(input())
    mun = int(input())
    main(num,mun)
