'''
Plots graph for MergeSort's time complexity.
'''
import matplotlib.pyplot as plt
import timeit
import math
import random
import sys

num = 500
sys.setrecursionlimit(1000)

def quickSort(li, l, h):
    if l < h:
        p = partition(li, l, h)
        quickSort(li, l, p - 1)
        quickSort(li, p + 1, h)
def partition(li, l, h):
    pivot = li[l]

    i = l
    j = h

    while i < j:
        while i < h and li[i] <= pivot:
            i = i + 1
        while j > l and li[j] >= pivot:
            j = j - 1
        if i < j:
            li[i], li[j] = li[j], li[i]

    li[l] = li[j]
    li[j] = pivot
    return j
def worstCaseArray(n):
    return [i for i in range(n)]
def averageCaseArray(n):
    return [random.randint(0, n) for i in range(n)]

if __name__ == '__main__':
    t = []
    for n in range(num):
        tAverage = timeit.timeit('quickSort(averageCaseArray(n), 0, n - 1)', number = 5, globals = globals())
        tWorst = timeit.timeit('quickSort(worstCaseArray(n), 0, n - 1)', number = 5, globals = globals())
        t.append((tAverage * (10 ** 6), tWorst * (10 ** 6)))

    tAverage = [a[0] for a in t]
    tWorst = [a[1] for a in t]

    time = [i for i in range(num)]

    plt.plot(time, tAverage)
    plt.plot(time, tWorst)
    plt.show()
