def getNext():
    idx = -1
    highest = 0

    for i in range(len(ratio)):
        if ratio[i] > highest:
            highest = ratio[i]
            idx = i
    return idx

def fill():
    currentWeight = 0
    currentProfit = 0.0

    while currentWeight < capacity:
        item = getNext()
        if item == -1:
            break
        print(item + 1, end = " ")

        if currentWeight + weight[item] <= capacity:
            currentWeight += weight[item]
            currentProfit += float(profit[item])
            solnVector[item] = 1
            ratio[item] = 0
        else:
            currentProfit += float(ratio[item]) * float((capacity - currentWeight))
            solnVector[item] = (capacity - currentWeight) / weight[item]
            break
    print("\nMaximum profit is: %d" %currentProfit)
    print("Solution Vector:", solnVector)
    input()


if __name__ == '__main__':
    n = int(input("Enter number of items: "))

    weight = []
    profit = []
    ratio = []
    solnVector = [0] * n

    print("Enter weights of items")
    for i in range(n):
        weight.append(int(input()))
    print("Enter profits of items")
    for i in range(n):
        profit.append(int(input()))
        ratio.append(float(profit[i]) / float(weight[i]))
    capacity = int(input("Enter capacity of knapsack: "))

    fill()
