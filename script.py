# Лаба 1: Змінні, типи, оператори

name = "Влад"
age = 17
height = 1.82
is_student = True
grades = [12, 10, 11, 9]
average = sum(grades) / len(grades)
info = {"ім'я": name, "вік": age}
unique = set(grades)
hobby = ("футбол", "ігри")
none_val = None

for var_name, var in {"name": name, "age": age, "height": height, "is_student": is_student,
                      "grades": grades, "average": average, "info": info,
                      "unique": unique, "hobby": hobby, "none_val": none_val}.items():
    print(f"{var_name} ({type(var).__name__}) : {var}")

a, b = 10, 3
print("\nОператори:")
print("a + b =", a + b)       # додавання
print("a - b =", a - b)       # віднімання
print("a * b =", a * b)       # множення
print("a / b =", a / b)       # ділення
print("a % b =", a % b)       # залишок
print("a ** b =", a ** b)     # степінь
print("a > b ->", a > b)      # порівняння
print("a == b ->", a == b)
print("a != b ->", a != b)
print("True and False ->", True and False)
print("True or False ->", True or False)
print("not True ->", not True)
print("'футбол' in hobby ->", "футбол" in hobby)
