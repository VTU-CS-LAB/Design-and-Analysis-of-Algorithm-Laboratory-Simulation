'''
Plots graph for MergeSort's time complexity.
'''
import matplotlib.pyplot as plt
import timeit
import math
import random
import sys

sys.setrecursionlimit(1000)

def mergeSort(li, l, h):
    if l < h:
        m = (l + (h - 1)) // 2
        mergeSort(li, l, m)
        mergeSort(li, m + 1, h)
        merge(li, l, m, h)
def merge(li, l, m, h):
    n1 = m - l + 1
    n2 = h - m

    L = []
    R = []

    for i in range(n1):
        L.append(li[l+i])
    for i in range(n2):
        R.append(li[m + 1 + i])

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            li[k] = L[i]
            i += 1
        else:
            li[k] = R[j]
            j += 1
        k += 1

    while i < n1:
            li[k] = L[i]
            i += 1
            k += 1
    while j < n2:
            li[k] = R[j]
            j += 1
            k += 1
def worstCaseArray(n):
    arr = [i for i in range(n)]
    final = []
    def shuffle(arr):
        if len(arr) <= 1:
            return
        if len(arr) == 2:
            arr[0], arr[1] = arr[1], arr[0]
            final.append(arr[0])
            final.append(arr[1])
        l = []
        r = []
        for i in range(len(arr)):
            if i % 2 == 0:
                l.append(arr[i])
            else:
                r.append(arr[i])
        shuffle(l)
        shuffle(r)
    shuffle(arr)
    return final
def bestCaseArray(n):
    return [i for i in range(n)]
def averageCaseArray(n):
    return [random.randint(0, n) for i in range(n)]

# print(worstCaseArray(1000))
# n = 100000
# print(timeit.timeit('mergeSort(bestCaseArray(n), 0, n - 1)', number = 10, globals = globals()))

t = []

# for n in range(100):
    #s tBest = timeit.timeit('mergeSort(bestCaseArray(n), 0, n - 1)', number = 1, globals = globals())
    #tAverage = timeit.timeit('mergeSort(averageCaseArray(n), 0, n - 1)', number = 1, globals = globals())
    # tWorst = timeit.timeit('mergeSort(worstCaseArray(n), 0, n - 1)', number = 1, globals = globals())
    # t.append((tBest * (10 ** 6), tAverage * (10 ** 6), tWorst * (10 ** 6)))

# print(t)
