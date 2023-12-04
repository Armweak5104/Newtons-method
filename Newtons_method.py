import random
degree = input("What degree polynomial would you like to use: ")
coeffs = []
for i in range(int(degree)+1):
  k = input(f"Enter coefficient for exponent {i}: ")
  if k[0] == "-":
    coeffs.append(-int(k[1:]))
  else:
    coeffs.append(int(k))

def f(x):
  out = 0
  for i in range(len(coeffs)):
    out+=coeffs[i]*(x**i)
  return out

def derivative(x):
  h = 0.001
  return (f(x+h)-f(x-h))/(2*h)

initial_range = input("Enter a random range for which your polynomial is continuous eg [-100,100]: ")
initial_range = initial_range[1:-1]
initial_range = initial_range.split(",")

if initial_range[0][0] == "-":
  lower = -int(initial_range[0][1:])
else:
  lower = int(initial_range[0])

if initial_range[1][0] == "-":
  upper = -int(initial_range[1][1:])
else:
  upper = int(initial_range[1])

sol = random.randint(lower, upper)

n = int(input("How many iterations would you like to run:"))
approximate = None
for i in range(1,n+1):
  approximate = sol - (f(sol)/derivative(sol))
  print(f"After {i} iterations, the solution is approximated to be {approximate}")
  sol = approximate

print(f"Final solution: {sol}")
