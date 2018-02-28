'''
Sort a given set of n integer elements using Merge Sort method and compute its time
complexity. Run the program for varied values of n>5000, and record the time taken to sort.
Plot a graph of the time taken versus n on graph sheet. The elements can be read from a file or
can be generated using the random number generator. Demonstrate how the divide-
and-conquer method works along with its time complexity analysis: worst case, average case
and best case.
'''

n = 1000 #number of elements in the array
import matplotlib.pyplot as plt
import timeit
import math

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
    if n == 1:
        return [1]
    else:
        top = worstCaseArray(int(math.floor(float(n) / 2)))
        bottom = worstCaseArray(int(math.ceil(float(n) / 2)))
        return list(map(lambda x: x * 2, top)) + list(map(lambda x: x * 2 - 1, bottom)) #Worst case for mergesort isnt a reversed sorted array

def timeBest():
    SETUP = '''
from __main__ import mergeSort, n
    '''
    STMT = '''
arr = [i for i in range(n)]
mergeSort(arr, 0, len(arr) - 1)
    '''
    t = timeit.repeat(setup = SETUP, stmt = STMT, repeat = 2, number = 1000)
    print(min(t))

def timeWorst():
    SETUP = '''
from __main__ import mergeSort, worstCaseArray, n
    '''
    STMT = '''
arr = worstCaseArray(n)
mergeSort(arr, 0, len(arr) - 1)
    '''
    t = timeit.repeat(setup = SETUP, stmt = STMT, repeat = 2, number = 1000)
    print(min(t))

def timeAverage():
    SETUP = '''
from __main__ import mergeSort, n
import random
    '''
    STMT = '''
arr = [random.randint(0, n) for i in range(1000)]
mergeSort(arr, 0, len(arr) - 1)
    '''
    t = timeit.repeat(setup = SETUP, stmt = STMT, repeat = 2, number = 1000)
    print(min(t))

def main():
    while True:
        print("1. Best 2. Average 3. Worst")
        ch = int(input())
        if ch == 1:
            timeBest()
        if ch == 2:
            timeAverage()
        if ch == 3:
            timeWorst()
main()
