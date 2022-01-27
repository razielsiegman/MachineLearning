


def recursiveFib(n):
    if n == 0 or n == 1:
        return n
    return (recursiveFib(n-1) + recursiveFib(n-2))


def matrixFib(n):
    list = [0,1]
    for i in range(2, n+1):
        list.append(list[i-1] + list[i-2])
    return list[n]


def imperativeFib(n):
    secondPreceding, firstPreceding = 0,1
    for i in range (1, n):
        secondPreceding, firstPreceding = firstPreceding, secondPreceding+firstPreceding
    return firstPreceding


n = 2
print("Fibonacci of " + str(n) + " using recursion: " + str(recursiveFib(n)))
print("Fibonacci of " + str(n) + " using matrices: " + str(matrixFib(n)))
print("Fibonacci of " + str(n) + " using imperative: " + str(imperativeFib(n)))

n = 10
print("Fibonacci of " + str(n) + " using recursion: " + str(recursiveFib(n)))
print("Fibonacci of " + str(n) + " using matrices: " + str(matrixFib(n)))
print("Fibonacci of " + str(n) + " using imperative: " + str(imperativeFib(n)))