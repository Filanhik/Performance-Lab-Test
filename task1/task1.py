import sys

def get_path(n, m):
    current = 1
    path = ""

    while True:
        path += str(current)
        next_num = (current + m - 2) % n + 1

        if next_num == 1:
            break

        current = next_num

    return path


if len(sys.argv) != 5:
    print("Нужно 4 аргумента: n1 m1 n2 m2")
    sys.exit()

n1, m1, n2, m2 = map(int, sys.argv[1:5])

path1 = get_path(n1, m1)
path2 = get_path(n2, m2)

print(path1 + path2)