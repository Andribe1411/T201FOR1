from scipy.optimize import fsolve

def equation(c):
    return 4*c**3 - 12*c**2 + 12*c - 4

c_initial_guess = 1.0
c_solution = fsolve(equation, c_initial_guess)

print("The solution is c =", c_solution)