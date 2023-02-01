def Eachmonth(month, y):
    for i in range(month + 1):
        if i // 10 >= 1:
            y += i % 10
            y += i // 10
        else:
            y += i
    return y
y = 0
print("какой год?")
year = input()
if year == "невисокосный":
    j = Eachmonth(31, y)
    print(f"Январь: {j} день")
    f = Eachmonth(28, y)
    print(f"Февраль: {f} дней")
    m = Eachmonth(31, y)
    print(f"Март: {m} дней")
    a = Eachmonth(30, y)
    print(f"Апрель: {a} дней")
    ma = Eachmonth(31, y)
    print(f"Май: {ma} день")
    jn = Eachmonth(30, y)
    print(f"Июнь: {jn} дней")
    jl = Eachmonth(31, y)
    print(f"Июль: {jl} день")
    ag = Eachmonth(31, y)
    print(f"Август: {ag} день")
    s = Eachmonth(30, y)
    print(f"Сентябрь: {s} дней")
    o = Eachmonth(31, y)
    print(f"Октябрь: {o} день")
    n = Eachmonth(30, y)
    print(f"Ноябрь: {n} ")
    d = Eachmonth(31, y)
    print(f"Декабрь: {d} день")
    summa = j + f + m + a + ma + jn + jl + ag + s + o + n + d
    print(f"Всего {summa} дней")
elif year == "високосный":
    j = Eachmonth(31, y)
    print(f"Январь: {j} день")
    f = Eachmonth(29, y)
    print(f"Февраль: {f} дней")
    m = Eachmonth(31, y)
    print(f"Март: {m} дней")
    a = Eachmonth(30, y)
    print(f"Апрель: {a} дней")
    ma = Eachmonth(31, y)
    print(f"Май: {ma} день")
    jn = Eachmonth(30, y)
    print(f"Июнь: {jn} дней")
    jl = Eachmonth(31, y)
    print(f"Июль: {jl} день")
    ag = Eachmonth(31, y)
    print(f"Август: {ag} день")
    s = Eachmonth(30, y)
    print(f"Сентябрь: {s} дней")
    o = Eachmonth(31, y)
    print(f"Октябрь: {o} день")
    n = Eachmonth(30, y)
    print(f"Ноябрь: {n} ")
    d = Eachmonth(31, y)
    print(f"Декабрь: {d} день")
    summa = j + f + m + a + ma + jn + jl + ag + s + o + n + d
    print(f"Всего {summa} дней")
else:
    print("Пишите нормально...")