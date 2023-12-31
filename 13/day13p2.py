input = open('input2.txt').read().splitlines()

ids = input[1].split(',')

def gcdExtended(a, b):
    v1 = [1, 0]
    v2 = [0, 1]

    while b != 0:
        s = a // b
        new_v0, new_v1 = v1[0] - s * v2[0], v1[1] - s * v2[1]
        v1 = v2 
        v2 = [new_v0, new_v1] 
        a, b = b, a % b
    return a, *v1

def solve(a1, m1, a2, m2):
    gcd, x, y = gcdExtended(m1, m2)
    lcm = m1 * m2 // gcd
    a3 = (x * m1 *a2 + y * m2 * a1) % lcm

    return a3, lcm

equations = []
for idx, id in enumerate(ids):
    if id != 'x':
        equations.append((int(id) - idx, int(id)))

current_equation = equations[0]
for equation in equations[1:]:
    current_equation = [*solve(current_equation[0], current_equation[1], equation[0], equation[1])]

print(current_equation[0])