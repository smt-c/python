x = 9
epsilon = 0.01
num_guesses = 0
if x >= 1:
    low = 0.0
    high = x
else:
    high = 1.0
    low = x

guess = (high + low) / 2.0

# square root
# while abs(guess**2 - x) >= epsilon:
#     if guess**2<x:
#         low = guess
#     else:
#         high = guess

#     guess = (high+low) / 2.0
#     num_guesses += 1
# print('num guess:', num_guesses)
# print('cloose sq root of x:', guess)

    # guess = guess - ((guess**2 - x) / (2 * guess))
    # num_guesses += 1


# cubic root
# cube = lambda y: y ** 3
# cubic = cube(guess)
# print(cubic)

# while abs(cubic - x) > epsilon:

#     if cubic > x:
#         high = guess
#     else:
#         low = guess

#     guess = (high+low) / 2.0
#     cubic = cube(guess)
#     num_guesses += 1

# print('num guess:', num_guesses)
# print('cloose cb root of x:', guess)

# Newthon - rapson method



from sympy import symbols, diff

# take inputs
x_val, epsilon = map(float, input("Enter x and epsilon separated by space: ").split())

def new_rap(x, epsilon):
    y = symbols('y')
    f = y**3 - x  # define equation dynamically
    f_prime = diff(f, y)  # derivative wrt y

    guess = x / 2.0

    while True:
        fx = f.subs({y: guess})
        fpx = f_prime.subs({y: guess})
        new_guess = guess - fx / fpx

        if abs(new_guess - guess) < epsilon:
            break

        guess = new_guess

    return new_guess

print(f"Approximate square root of {x_val} is {new_rap(x_val, epsilon)}")
