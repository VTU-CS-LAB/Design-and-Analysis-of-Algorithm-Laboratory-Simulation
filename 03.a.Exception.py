if __name__ == '__main__':
    m, n = input("Enter two numbers: ").split()
    m = int(m)
    n = int(n)
    try:
        print(float(m / n))
    except ZeroDivisionError as e:
        print("ZeroDivisionError: {0}".format(e))
