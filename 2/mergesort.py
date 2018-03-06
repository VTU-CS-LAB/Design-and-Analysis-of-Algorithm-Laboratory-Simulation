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
    def generate(li, l, h):
        if l < h:
            mid = (l + h) // 2
            partition(li, l, h)
            generate(li, l, mid)
            generate(li, mid + 1, h)
    def partition(li, l, h):
        n = h - l + 1
        k = 0
        t = []
        for i in range(l, h + 1, 2):
            t.append(li[i])
        for i in range(l + 1, h + 1, 2):
            t.append(li[i])

        for i in range(l, n):
            li[l + i] = t[i]
    generate(arr, 0, len(arr) - 1)
    return arr
def bestCaseArray(n):
    return [i for i in range(n)]
def averageCaseArray(n):
    return [random.randint(0, n) for i in range(n)]

t = []

for n in range(num):
    tBest = timeit.timeit('mergeSort(bestCaseArray(n), 0, n - 1)', number = 3, globals = globals())
    tAverage = timeit.timeit('mergeSort(averageCaseArray(n), 0, n - 1)', number = 3, globals = globals())
    tWorst = timeit.timeit('mergeSort(worstCaseArray(n), 0, n - 1)', number = 3, globals = globals())
    t.append((tBest * (10 ** 6), tAverage * (10 ** 6), tWorst * (10 ** 6)))

tBest = [a[0] for a in t]
tAverage = [a[1] for a in t]
tWorst = [a[2] for a in t]

time = [i for i in range(num)]

plt.plot(time, tBest)
plt.plot(time, tAverage)
plt.plot(time, tWorst)
plt.show()
