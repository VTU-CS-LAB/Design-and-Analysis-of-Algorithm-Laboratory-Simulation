import random
import matplotlib.pyplot as plt
import time

n = 100000

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

timeBestCase = []
timeWorstCase = []
timeAverageCase = []

bestCase = [i for i in range(n)]
worstCase = bestCase[::-1]
averageCase = [random.randint(0, n) for i in range(n)]

def findTime(bestCase, worstCase, averageCase):
    for i in range(int(n/2), int(n), int(n/50)):
        print(i)
        t1 = time.time()
        mergeSort(bestCase, 0, i)
        timeBestCase.append(time.time() - t1)
        t2 = time.time()
        mergeSort(worstCase, 0, i)
        timeWorstCase.append(time.time() - t2)
        t3 = time.time()
        mergeSort(averageCase, 0, i)
        timeAverageCase.append(time.time() - t3)

findTime(bestCase, worstCase, averageCase)

plt.plot([i for i in range(5000, 10000, int(n/50))], timeBestCase)
plt.plot([i for i in range(5000, 10000, int(n/50))], timeWorstCase)
plt.plot([i for i in range(5000, 10000, int(n/50))], timeAverageCase)
plt.xlabel('Number of inputs')
plt.ylabel('Time of execution in seconds')
plt.show()
