fibonacci_cache={}
def fibonacci(n):
    #implicit explaination of cache
    if type(n) !=int:
        raise TypeError("n must be positive integer")
    if(n<1):
        raise ValueError("n must be a Postive Integer")

    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n==1:
        value=1
    if n==2:
        value=1
    elif n>2:
        value= fibonacci(n-1)+fibonacci(n-2)

    fibonacci_cache[n]=value
    return value



print(":",fibonacci(100))