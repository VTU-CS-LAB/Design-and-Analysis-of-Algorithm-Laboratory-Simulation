def subSet(total, index, solution):
    if total == 0:
        printSolution(solution)
    elif total < 0 or index < 0:
        return
    else:
        tempSolution = solution
        tempSolution[index] = False
        subSet(total, index - 1, tempSolution)
        tempSolution[index] = True
        subSet(total - arr[index], index - 1, tempSolution)
def printSolution(solution):
    global count
    count += 1
    if count == 1:
        print("Solution:")
    else:
        print("\nSolution")
    for i in range(len(solution)):
        if solution[i]:
            print(arr[i], end = " ", sep = "\n")
if __name__ == '__main__':
    count = 0
    arr = [1, 2, 5, 6, 8]
    n = 5
    total = 9
    subSet(total, n - 1, [False] * n)
    if count == 0:
        print("No solution")
