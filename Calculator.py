def summa(a, b):
    return a + b

def minus(a, b):
    return a - b

def div(a, b):
    return a / b

def multiply(a, b):
    return a * b

def degree(a, b):
    return a ** b

print("Введите количество операций")
count = float(input())
print("Введите первое число")
a = float(input())
while (0 < count):
    print("Введите второе число")
    b = float(input())
    print("Выберите оператор")
    oper = input()
    match oper:
        case "+":
            a = summa(a, b)
            print(a)
        case "-":
            a = minus(a, b)
            print(a)
        case "/":
            if (b == 0):
                print("на ноль делить нельзя!")
            else:
                a = div(a, b)
                print(a)
        case "*":
            a = multiply(a, b)
            print(a)
        case "**":
            a = degree(a, b)
            print(a)
    count -= 1
