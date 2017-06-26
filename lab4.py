from sympy import *
x = symbols('x')
init_printing(use_unicode=True)

data_x = [ -1 , 1 , 3]
data_y = [17 , -7 , -10]

func = data_y[:]
for k in range(1, len(data_x)):
  for i in range(len(data_x) - k):
    prev_func = func[:]
    func[i] = \
      ((x - data_x[i + k]) * prev_func[i] + (data_x[i] - x) * prev_func[i + 1]) \
      / (data_x[i] - data_x[i + k])


func = simplify(func[0])
pol = func.subs({x:0})
print('y(x) =' , func)
print(pol)
