num1 = float(input("Введіть перше число:"))
num2 = float(input("Введіть друге число:"))

act = input("Вибір дії з числами - +(сума), -(різниця), *(добуток), /(середньоарифметичне):")

if act == '+':
    result = num1 + num2
if act == '-':
    result = num1 - num2
if act =='*':
    result = num1 * num2
if act =='/':
    result = (num1 + num2)/2

print(f"Результат - {result}")