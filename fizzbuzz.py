print("Hello~ FiveCoders It Works")
for i in range(1, 20):
    print(f"{i}")


# Fibonacci Sequence by @github/coevol
print("Recurrent Fibonacci Sequence")
print("Enter fibo(number) with a number")
def fibo(n:int):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

