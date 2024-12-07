from random import randint
from tqdm import tqdm


def play(urne_blanc_a, urne_blanc_b, urne_noir_a, urne_noir_b):
    # A plays
    tmp = urne_blanc_a.pop(randint(0, 1))
    urne_blanc_a.append(urne_noir_a.pop(randint(0, 1)))
    urne_noir_a.append(tmp)

    # B plays
    urne_blanc_b.append(urne_noir_b.pop(randint(0, 1)))
    urne_noir_b.append(urne_blanc_b.pop(randint(0, 2)))

    # print(urne_blanc_a, urne_blanc_b, urne_noir_a, urne_noir_b)
    return urne_blanc_a, urne_blanc_b, urne_noir_a, urne_noir_b


num_iter = 1000000
num_win = 0
for _ in tqdm(range(num_iter)):
    urne_blanc_a = ["noir", "noir"]
    urne_blanc_b = ["noir", "noir"]

    urne_noir_a = ["blanc", "blanc"]
    urne_noir_b = ["blanc", "blanc"]

    while True:
        urne_blanc_a, urne_blanc_b, urne_noir_a, urne_noir_b = play(
            urne_blanc_a, urne_blanc_b, urne_noir_a, urne_noir_b
        )

        if all(x == "blanc" for x in urne_blanc_a):
            num_win += 1
            # print("A wins")
            break
        elif all(x == "blanc" for x in urne_blanc_b):
            # print("B wins")
            break

print(f"win probability: {num_win} / {num_iter}")

import numpy as np
import fractions

np.set_printoptions(
    formatter={"all": lambda x: str(fractions.Fraction(x).limit_denominator())}
)

# Transition matrix P
P = np.array(
    [
        [0, 0, 1 / 3, 2 / 3, 0, 0],
        [0, 0, 1 / 6, 2 / 3, 0, 1 / 6],
        [1 / 12, 1 / 6, 1 / 6, 1 / 3, 1 / 4, 0],
        [1 / 24, 1 / 6, 1 / 12, 1 / 3, 1 / 4, 1 / 8],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1],
    ]
)

# Q and R matrices
Q = P[:4, :4]  # Transitions between transient states
R = P[:4, 4:]  # Transitions from transient to absorbing states

# Compute (I - Q) inverse
I = np.eye(Q.shape[0])
N = np.linalg.inv(I - Q)

print(Q, N, R)
# Compute absorption probabilities
B = N @ R
print("Absorption probabilities:\n", B)
