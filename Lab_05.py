from sympy import *

x = symbols('x')


def kronecker(expr):
    expr_top = degree(expr) // 2 + 1

    for i in range(expr_top):
        if expr.subs(x, i) == 0:
            return Poly(x - i), 1

    divs = FiniteSet(*divisors(expr.subs(x, 0)))
    for i in range(1, expr_top):
        divs_i = FiniteSet(*divisors(expr.subs(x, i)))
        divs = ProductSet(divs, divs_i)
        for cart in divs:
            points = [(j, cart[j]) for j in range(0, i + 1)]
            fact = Poly(interpolate(points, x), x)
            if (fact.degree() == i) and (prem(expr, fact) == Poly(0, x)):
                # print(i, cart, fact, prem(expr, fact))
                return fact, i

    return expr, 0


def kfactor(expr):
    prod = [];

    if expr.nth(expr.degree()) < 0:
        prod.append(Poly(-1, x))
    
    div, deg = kronecker(expr)
    if (deg <= 1):
        prod.append(div)
    else:
        prod += kfactor(div)
    
    expr, rest = pdiv(expr, div)
    if rest != 0:
        raise 'Error in rest of polynomial division'

    return prod + (kfactor(expr) if (degree(expr) > 0) else [])




tests = [
    -x**5 - x**4 + 12*x**3 - 5*x**2 - 5*x + 60,
    x**4 + 2*x**3 - 72*x**2 - 416*x - 640
]

for p in tests:
    # factorization and pretty output
    fact = '' 
    for item in kfactor(Poly(p)): 
        elem = str(item) 
        fact += '(%s)' % elem[elem.find('(') + 1:elem.find(',')]

    print('Test:     ', p)
    print('Result:   ', fact)
    print('Expected: ', factor(p))
    print('---')
