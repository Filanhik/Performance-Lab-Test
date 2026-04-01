import sys
import json

if len(sys.argv) != 4:
    print("Нужно 3 аргумента: values.json tests.json report.json")
    sys.exit()

file_values = sys.argv[1]
file_tests = sys.argv[2]
file_report = sys.argv[3]

# Читаем values
with open(file_values) as f:
    data = json.load(f)

values = {item["id"]: item["value"] for item in data["values"]}

# Читаем tests
with open(file_tests) as f:
    tests = json.load(f)

# Рекурсия
def fill(test):
    if test["id"] in values:
        test["value"] = values[test["id"]]

    if "values" in test:
        for internal_test in test["values"]:
            fill(internal_test)

# Обработка
for test in tests["tests"]:
    fill(test)

# Запись
with open(file_report, "w") as f:
    json.dump(tests, f, indent=2)