# condição básica: f(1) = 1
def f(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return f(n-1) + f(n-2)

# condição básica: f(1) = 1

m = {}
def f_memo(n):    
    if n < 2:
        return n
    elif n in m:
        return m[n]
    else:
        m[n] = f_memo(n-1) + f_memo(n-2)
        return m[n]

f(33)
f_memo(33)





def func(n): 
    if n <= 1: 
        return 1 
    else: 
        return n * func(n - 1) 
 
print(func(4)) 