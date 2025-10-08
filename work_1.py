
# class Work:
#     def __init__(self, name):
#         self.name = name

#     def perform_task(self):
#         print(f'{self.name} is performing a task.')

# do_it = Work('Alice')
# do_it.perform_task()

def sqrt_approx(number, tolerance=0.001, max_iterations=10):
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    
    guess = number / 2.0  # Initial guess

    for i in range(max_iterations):
        new_guess = 0.5 * (guess + number / guess)
        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess

    return guess  # Return best guess after max_iterations

# Example usage
num = float(input("Enter a number to approximate its square root: "))
approx = sqrt_approx(num)
print(f"Approximate square root of {num} is {approx}")

