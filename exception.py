try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print(age)
except ValueError:
    print("Wrongly taken input")
except ZeroDivisionError:
    print("Cannot divide a number by zero")