
def fibo1(n) :
    a, b = 0, 1
    while a < n: 
        print(a, end=" ")
        a, b = b, a+b
    print()

def fibo2(n):
    resultado = []
    a, b = 0, 1
    while a < n :
        resultado.append(a)
        a, b = b, a+b
    return resultado

# Fibonacci con recursión
def fibo3(n, temp={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n not in temp:
        temp[n] = fibo3(n-1, temp) + fibo3(n-2, temp)
    return temp[n]
