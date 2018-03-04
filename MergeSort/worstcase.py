
def swapperooni(a,low,high):
    L = []
    R = []
    if((high - low) == 1):
        a[low],a[low+1] = a[low+1],a[low]
    elif((high - low) == 0):
        return
    else:
        num = (high+1) - low
        for i in range(num):
            if ((i%2)==0):
                L.append(a[low + i])
            else:
                R.append(a[low + i])
        a[low:(high+1)] = L + R

def create(a,low,high):
    if(low<high):
        mid = (low+high)/2
        swapperooni(a,low,high)
        create(a,low,mid)
        create(a,mid+1,high)

def worstCaseArray(n):
    a = []
    low = 0
    high = n-1
    for i in range(n):
        a.append(i)
    create(a,low,high)
    return a
