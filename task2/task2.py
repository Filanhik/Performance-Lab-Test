import sys

# Аргументы
if len(sys.argv) != 3:
    print("Нужно 2 аргумента: файл эллипса и файл точек")
    sys.exit()

file_circle = sys.argv[1]
file_dot = sys.argv[2]

# Читаем эллипс
with open(file_circle) as f:
    x0, y0 = map(float, f.readline().split())
    a, b = map(float, f.readline().split())

# Читаем точки
with open(file_dot) as f:
    for line in f:
        x, y = map(float, line.split())

        dx = x - x0
        dy = y - y0

        value = (dx*dx)/(a*a) + (dy*dy)/(b*b)

        eps = 1e-9

        if abs(value - 1) < eps:
            print(0)
        elif value < 1:
            print(1)
        else:
            print(2)