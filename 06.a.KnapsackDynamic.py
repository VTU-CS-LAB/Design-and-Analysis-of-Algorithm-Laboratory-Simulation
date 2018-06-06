import numpy as np

def fill(n, capacity, profit, weight):
    K = np.zeros((n + 1, capacity + 1))
    for i in range(n + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                K[i, j] = 0
            elif j < weight[i - 1]:
                K[i, j] = K[i - 1, j]
            else:
                K[i, j] = max(K[i - 1, j], profit[i - 1] + K[i - 1, j - weight[i - 1]])

    print("Max profit:", K[n, capacity])
    print("Matrix: ", sep = "\n")
    print(K)
    print("Items considered:", sep = "\n")
    i = n
    j = capacity
    while i > 0 and j > 0:
        if K[i, j] != K[i - 1, j]:
            print(i, end = " ")
            j -= weight[i - 1]
        i -= 1
if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    weight = []
    profit = []
    print("Enter weights and profits of items\n")
    for i in range(n):
        weight.append(int(input()))
        profit.append(int(input()))
    capacity = int(input("Enter capacity of knapsack: "))
    fill(n, capacity, profit, weight)
