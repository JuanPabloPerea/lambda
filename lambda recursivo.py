def recursivo(funtion):
    def envoltura(num1,**num2):
        fi = lambda num1, **num2: funtion(fi, num1, **num2)
        return def_fun(fi, num1, **num2)

    return wrapper

fibonaci = recursive(lambda f, n: f(n - 1) + f(n - 2) if n > 1 else 1)
print(fibonaci(10))

