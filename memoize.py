def memize(f):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = f(*args)
        cache[args] = result
        return result
    return wrapper

@memize
def fibonacci(n):
    if n <=1 :
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
@memize
def factoriel(n):
    if n == 1 or n == 1:
        return 1
    else:
        return n * factoriel(n-1)
    
print(fibonacci(40))