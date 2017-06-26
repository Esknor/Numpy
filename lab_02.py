from sympy import *

# # Graph
V = range(1, 8 + 1)
E = [ (1,2), (1,3), 
      (2,1), (2,4),
      (3,1), (3,4),
      (4,3), (4,2), (4,5), 
      (5,4), (5,8), (5,6),
      (6,5), (6,7),
      (7,6), (7,8),
      (8,7), (8,5) ]

# Graph symbols
Vx = [ Symbol('x' + str(i)) for i in V ]
Ex = [ (Vx[i-1], Vx[j-1]) for i, j in E ] 

# Calculaion of chrmatic number and Groebner's basis
chromatic = 0
for k in range(1, 6):
    Fk = [ x**k - 1 for x in Vx ]
    Fg = [ factor((x**k - y**k)/(x-y)) for x, y in Ex ]
    G = groebner(Fk + Fg, Vx)
    
    if (G != [1]):
	print(k)
        colorings = solve(G, Vx)

        print(G)
        print('Amount of ways for k =', k, 'is', len(colorings))

        if (chromatic == 0):
            chromatic = k
            print('Chromatic number is', chromatic)

    else:
        print('No solution for k =', k)

    if (chromatic > 0 and k >= 3):
        break

    print()
