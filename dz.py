num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

act = input("Вибір дії[+, *]: ")

if act == "+":
    result = num1+num2+num3
elif act == "*":
    result = num1*num2*num3

print(f"Результат - {result}")