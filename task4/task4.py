import sys

if len(sys.argv) != 2:
    print("Нужен 1 аргумент: файл с числами")
    sys.exit()

file_name = sys.argv[1]

# Читаем числа
with open(file_name) as f:
    nums = [int(line.strip()) for line in f]

# Находим медиану
nums.sort()
n = len(nums)
median = nums[n // 2]

# Считаем шаги
steps = sum(abs(x - median) for x in nums)

# Вывод
if steps <= 20:
    print(steps)
else:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")