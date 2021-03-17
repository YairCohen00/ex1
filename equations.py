def regPow(x:float, i:float):
    if i == 0:
        return 1
    else:
        ans = x
        for r in range(1,i):
            ans *= x
    return ans

def factorial(i:float):
    if i < 1:
        return 1
    ans = i
    for x in range(1, i):
        ans *= x
    return ans

def absu (x:float):
    if x > 0:
        return x
    else:
        return x*-1

def odd(x:float):
    if x % 2 != 0:
        return True
    else:
        return False

# def exponent(x:float):
#     ans = 1
#     temp = 0.0
#     i = 1
#     while ans != temp:
#         temp = ans
#         ans += (regPow(x,i)) / (factorial(i))
#         i+=1
#     return ans



def exponent(x:float):
    ans = 1
    for i in range(1, 100):
        ans += (regPow(x,i)) / (factorial(i))
    return ans


def Ln(x:float):
    if x <= 0:
        return 0.0
    ans = x - 1.0
    temp = 0
    while absu(temp - ans) > 0.001:
        temp = ans
        ans = ans + 2 * ((x - exponent(ans)) / (x + exponent(ans)))
    return ans

def XtimesY(x:float,y:float):
    if x<0:
        return 0.0
    if y == 0:
        return 1.0
    elif y == 1:
        return float(x)
    else:
        ans = exponent(y * Ln(x))
        return ans

def sqrt(x:float,y:float):
    if y == 0:
        return 0.0
    if y < 0 and odd(x):
        ans = XtimesY(-y, 1 / x)
        return ans*-1
    ans = XtimesY(y,1/x)
    return ans

def calculate(x:float):
    ans = exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
    return float('%0.6f' % ans)
