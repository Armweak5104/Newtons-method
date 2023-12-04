from scipy.misc import derivative
import random
degree = input("What degree polynomial would you like to use"]
coeffs = []
for i in range(int(degree)):
  k = int(input(f"Enter coefficient for exponent {i}"))
  coeffs.append(k)
def f(x):
  out = 0
  for i in range(len(coeffs)):
    out+=coeffs[i]*(x**i)
  return out

initial_range = input("Enter a random range for which your polynomial is continuous eg [-100,100]")
initial_range = initial_range[1:-1]
initial_range.split(",")
sol = random.randint(int(initial_range[0]),int(initial_range[2]))

n = int(input("How many iterations would you like to run:"))
approximate = None
for i in range(1,n):
  approximate = sol - (f(sol)/derivative(f,sol))
  sol = approximate
print("The solution after",n,"iterations is",approximate)
