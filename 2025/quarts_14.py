# Define a function to calculate the sum of the digits of a number
def digit_sum(n):
    return sum(int(digit) for digit in str(n))


def function(n):
    return n + 2 * digit_sum(n)


def forward_sequence(n, target_number, verbose=False):
    seq = [n]
    while n < target_number:
        n = function(n)
        seq.append(n)
    if n == target_number:
        if verbose:
            print(seq)
        return True
    return False


# Target 2025 and compute forwards paths
target_number = 2025

solutions = []
for i in range(1, 2024):
    if forward_sequence(i, target_number):
        solutions.append(i)

print(solutions)
print(len(solutions))
for sol in solutions:
    forward_sequence(sol, target_number, verbose=True)
