from sympy import *

x = symbols('x')
init_printing(use_unicode=True)

def coefficients(P):
    Pc = []
    for i in range(P.degree(), -1, -1):
        Pc.append(P.nth(i))
    return Pc


def sylvester(U, V):
    u_coeff = coefficients(U) 
    v_coeff = coefficients(V)
    
    m = len(u_coeff) - 2
    n = len(v_coeff) - 2

    matrix = []

    # top part of matrix
    row = u_coeff
    row += [0] * n
    matrix.append(row)
    for i in range(n):
        row = row[-1:] + row[:-1]
        matrix.append(row)

    # bottom part of matrix
    row = v_coeff
    row += [0] * m
    matrix.append(row)
    for i in range(m):
        row = row[-1:] + row[:-1]
        matrix.append(row)
    print("Matrix: ")
    for i in range(len(matrix)):
        print(matrix[i])
    return Matrix(matrix)
    
    return Matrix(matrix)


def resultant(P, Q):
    return sylvester(P, Q).det()


U = Poly(x**3 - 1, x)
V = Poly(x**2 + 2, x)
print('Resultant =', resultant(U, V))
u = x**3-1
v = x**2+2
print(factor(u))
print(factor(v))
