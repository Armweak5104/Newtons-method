from scipy.misc import derivative
def f(x):
  return x**2 +5*x + 1
sol = int(input("What is your first guess:"))
n = int(input("How many iterations would you like to run:"))
approximate = None
for i in range(1,n):
  approximate = sol - (f(sol)/derivative(f,sol))
  sol = approximate
print("The solution after",n,"iterations is",approximate)
