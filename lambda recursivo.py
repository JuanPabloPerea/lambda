def recursive(def_fun):
    def wrapper(p,**kw):
        fi = lambda p, **kw: def_fun(fi, p, **kw)
        return def_fun(fi, p, **kw)

    return wrapper

fibonaci = recursive(lambda f, n: f(n - 1) + f(n - 2) if n > 1 else 1)
print(fibonaci(10))

factorial = recursive(lambda f, n: 1 if n < 2 else n * f(n - 1))
print(factorial(10))
