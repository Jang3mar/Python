import json as js
from pprint import pprint
import readchar
from random import randint
import enum

tom_yum = []
global sum
global thais_leg
global id

# users = {}
# users = {'User' : [{'ID' : 0, 'name' : 'Admin', 'login' : 'admin1', 'password' : 'p@SSw0rd', 'money' : 0.00, 'role' : 'admin'}, {'ID' : 1, 'name' : 'User1', 'login' : 'user1', 'password' : 'p@SSw0rd', 'money' : 1500.00, 'role' : 'client'}]}
# ['users.json'].append(users)
# with open('users.json', 'w', encoding='utf8') as f:
#     js.dump(users, f, ensure_ascii=False, indent=2)

def Add_MoneyAdm():
    money = float(input("Введите сумму: "))
    if money > 0.0:
        with open('users.json') as f:
            data = js.load(f)
            data['User'][0]['money'] += money
            print(data['User'][0]['money'])
            with open ('users.json', 'w') as f:
                js.dump(data,f,  ensure_ascii=False, indent=2)
                print(f"На вашем счету теперь {data['User'][0]['money']} рублей")
                Admin_Menu()
    else:
        print("Сумма должна быть неотрицательной")
        Admin_Menu()

def Add_MoneyCl():
    money = float(input("Введите сумму: "))
    if money > 0.0:
        with open('users.json', encoding='utf8') as f:
            data = js.load(f)
            for i in range(len(data['User'])):
                if id == int(data['User'][i]['ID']):
                    data['User'][i]['money'] += money
            with open('users.json', 'w') as f:
                js.dump(data, f, ensure_ascii=False, indent=2)
                print("Счет пополнен!")
                Client_Menu()
    else:
        print("Сумма должна быть неотрицательной!")
        Client_Menu()

def History_Order():
    print("История всех заказов")
    with open('history.json', encoding='utf8') as f:
        data = js.load(f)
        pprint(data)
    print("Нажмите 1, чтобы вернуться в меню")
    key = readchar.readkey()
    if key == '1':
        Admin_Menu()

def History_OrderClient():
    print(id)
    print("История ваших заказов")
    with open('history.json', encoding='utf8') as f:
        data = js.load(f)
        for i in range(len(data['Orders'])):
            if data['Orders'][i]['user_id'] == id:
                pprint(data['Orders'][i])
    print("Нажмите 1, чтобы вернуться в меню")
    key = readchar.readkey()
    if key == '1':
        Client_Menu()
    else:
        print("Не туда нажали")

def Admin_Menu():
    print("Выберите действие: \n1.Заказать продукты\n2.Посмотреть историю заказов\n3.Пополнить счет\n4.Выйти из аккаунта")
    key = readchar.readkey()
    if key == '1':
        Ordering_Groceries()
    if key == '2':
        History_Order()
    if key == '3':
        Add_MoneyAdm()
    if key == '4':
        Main_Menu()
    else:
        print("Не туда нажали")

def Ordering_Groceries():
    cycle = True
    with open('products.json', encoding='utf8') as f:
        prod = js.load(f)
    with open ('users.json', encoding='utf8') as f:
        user = js.load(f)
    while cycle:
        print("Выберите продукт: 1.Вода 2.Куриный бульон 3.Овощной бульон 4.Томаты черри 5.Кабачок 6.Лук 7.Креветки 8.Кальмар 9.Курица 10.Оливковое масло 11.Подсолнечное масло 12.Соевое масло 13.Шампиньоны 14.Эноки 15.Шиитаке 16.Соевый соус 17.Рыбный соус 18.Устричный соус 19.Лемонграсс 20.Галангал(имбирь) 21.Кокосовое молоко 22.Кинза 23.Лайм 24.Кунжутный соус\nИли нажмите 0, чтобы выйти")
        key = int(input())
        match(key):
            case '1':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][0]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][0]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '2':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][1]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][1]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '3':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][2]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][2]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '4':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][3]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][3]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '5':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][4]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][4]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '6':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][5]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][5]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '7':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][6]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][6]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '8':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][7]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][7]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '9':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][8]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][8]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '10':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][9]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][9]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '11':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][10]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][10]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '12':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][11]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][11]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '13':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][12]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][12]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '14':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][13]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][13]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '15':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][14]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][14]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '16':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][15]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][15]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '17':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][16]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][16]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '18':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][17]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][17]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '19':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][18]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][18]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '20':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][19]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][19]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '21':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][20]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][20]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '22':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][21]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][21]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '23':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][22]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][22]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '24':
                print("Введите количество")
                count = int(input())
                print("Нажмите 1, чтобы оплатить, либо 2, чтобы выйти")
                key = readchar.readkey()
                if key == '1':
                    prod['Product'][23]['count'] += count
                    user['User'][0]['money'] -= count * prod['Product'][23]['cost']
                    with open('products.json', 'w', encoding='utf8') as f:
                        js.dump(prod, f, ensure_ascii=False, indent=2)
                    with open ('users.json', 'w', encoding='utf8') as f:
                        js.dump(user, f, ensure_ascii=False, indent=2)
                if key == '2':
                    cycle = False
                    Admin_Menu()
                else :
                    print("Не туда нажали")
            case '0':
                cycle = False
                Admin_Menu()
            case _:
                print("Не туда нажали")

def Client_Menu():
    print("Выберите действие \n1.Собрать свой том ям\n2.Пополнить счет\n3.История заказов\n4.Выйти из аккаунта")
    key = readchar.readkey()
    if key == '1':
        Build_TomYum()
    if key == '2':
        Add_MoneyCl()
    if key == '3':
        History_OrderClient()
    if key == '4':
        Main_Menu()

def Build_TomYum():
    сount = 1
    tom_yum = []
    summ = 0
    cycle = True
    try:
        with open('products.json', encoding='utf8') as f:
            prod = js.load(f)
        with open('users.json', encoding='utf8') as f:
            user = js.load(f)
        with open('history.json', encoding='utf8') as f:
            his_order = js.load(f)
        while cycle:
            print("Что будем делать?\n1.Собрать том ям\n2.Выйти\n3.Оплатить заказ\n4.Убрать ингридиенты")
            key = readchar.readkey()
            if key == '1':
                print("Выберите суповую основу\n1.Просто вода\n2.Куриный\n3.Овощной")
                key = int(input())
                match(key):
                    case 1:
                        if prod['Product'][0]['count'] > 0:
                            tom_yum.append(prod['Product'][0]['name'])
                            prod['Product'][0]['count'] -= сount
                            summ += prod['Product'][0]['cost']
                        else:
                            print("Продукт закончился")
                    case 2:
                        if prod['Product'][1]['count'] > 0:
                            tom_yum.append(prod['Product'][1]['name'])
                            prod['Product'][1]['count'] -= сount
                            summ += prod['Product'][1]['cost']
                        else:
                            print("Продукт закончился")
                    case 3:
                        if prod['Product'][2]['count'] > 0:
                            tom_yum.append(prod['Product'][2]['name'])
                            prod['Product'][2]['count'] -= сount
                            summ += prod['Product'][2]['cost']
                        else:
                            print("Продукт закончился")
                    case _:
                        print("Не туда нажали")
                print("Выберите овощи\n4.Томаты черри\n5.Кабачки\n6.Лук")
                key = int(input())
                match(key):
                    case 4:
                        if prod['Product'][3]['count'] > 0:
                            tom_yum.append(prod['Product'][3]['name'])
                            prod['Product'][3]['count'] -= сount
                            summ += prod['Product'][3]['cost']
                        else:
                            print("Продукт закончился")
                    case 5:
                        if prod['Product'][4]['count'] > 0:
                            tom_yum.append(prod['Product'][4]['name'])
                            prod['Product'][4]['count'] -= сount
                            summ += prod['Product'][4]['cost']
                        else:
                            print("Продукт закончился")
                    case 6:
                        if prod['Product'][5]['count'] > 0:
                            tom_yum.append(prod['Product'][5]['name'])
                            prod['Product'][5]['count'] -= сount
                            summ += prod['Product'][5]['cost']
                        else:
                            print("Продукт закончился")
                    case _:
                        print("Не туда нажали")
                print("Выберите рыбную или мясную основу\n7.Креветки\n8.Кальмар\n9.Курица")
                key = int(input())
                match(key):
                    case 7:
                        if prod['Product'][6]['count'] > 0:
                            tom_yum.append(prod['Product'][6]['name'])
                            prod['Product'][6]['count'] -= сount
                            summ += prod['Product'][6]['cost']
                        else:
                            print("Продукт закончился")
                    case 8:
                        if prod['Product'][7]['count'] > 0:
                            tom_yum.append(prod['Product'][7]['name'])
                            prod['Product'][7]['count'] -= сount
                            summ += prod['Product'][7]['cost']
                        else:
                            print("Продукт закончился")
                    case 9:
                        if prod['Product'][8]['count'] > 0:
                            tom_yum.append(prod['Product'][8]['name'])
                            prod['Product'][8]['count'] -= сount
                            summ += prod['Product'][8]['cost']
                        else:
                            print("Продукт закончился")
                    case _:
                        print("Не туда нажали")
                print("Выберите масло\n10.Оливковое\n11.Подсолнечное\n12.Соевое")
                key = int(input())
                match(key):
                    case 10:
                        if prod['Product'][9]['count'] > 0:
                            tom_yum.append(prod['Product'][9]['name'])
                            prod['Product'][9]['count'] -= сount
                            summ += prod['Product'][9]['cost']
                        else:
                            print("Продукт закончился")
                    case 11:
                        if prod['Product'][10]['count'] > 0:
                            tom_yum.append(prod['Product'][10]['name'])
                            prod['Product'][10]['count'] -= сount
                            summ += prod['Product'][10]['cost']
                        else:
                            print("Продукт закончился")
                    case 12:
                        if prod['Product'][11]['count'] > 0:
                            tom_yum.append(prod['Product'][11]['name'])
                            prod['Product'][11]['count'] -= сount
                            summ += prod['Product'][11]['cost']
                        else:
                            print("Продукт закончился")
                    case _:
                        print("Не туда нажали")
                print("Выберите грибы\n13.Шампиньоны\n14.Эноки\n15.Шиитаке")
                key = int(input())
                match(key):
                    case 13:
                        if prod['Product'][12]['count'] > 0:
                            tom_yum.append(prod['Product'][12]['name'])
                            prod['Product'][12]['count'] -= сount
                            summ += prod['Product'][12]['cost']
                        else:
                            print("Продукт закончился")
                    case 14:
                        if prod['Product'][13]['count'] > 0:
                            tom_yum.append(prod['Product'][13]['name'])
                            prod['Product'][13]['count'] -= сount
                            summ += prod['Product'][13]['cost']
                        else:
                            print("Продукт закончился")
                    case 15:
                        if prod['Product'][14]['count'] > 0:
                            tom_yum.append(prod['Product'][14]['name'])
                            prod['Product'][14]['count'] -= сount
                            summ += prod['Product'][14]['cost']
                        else:
                            print("Продукт закончился")
                    case _:
                        print("Не туда нажали")
                print("Выберите соус\n16.Соевый\n17.Рыбный\n18.Устричный")
                key = int(input())
                match(key):
                    case 16:
                        if prod['Product'][15]['count'] > 0:
                            tom_yum.append(prod['Product'][15]['name'])
                            prod['Product'][15]['count'] -= сount
                            summ += prod['Product'][15]['cost']
                        else:
                            print("Продукт закончился")
                    case 17:
                        if prod['Product'][16]['count'] > 0:
                            tom_yum.append(prod['Product'][16]['name'])
                            prod['Product'][16]['count'] -= сount
                            summ += prod['Product'][16]['cost']
                        else:
                            print("Продукт закончился")
                    case 18:
                        if prod['Product'][17]['count'] > 0:
                            tom_yum.append(prod['Product'][17]['name'])
                            prod['Product'][17]['count'] -= сount
                            summ += prod['Product'][17]['cost']
                        else:
                            print("Продукт закончился")
                    case _:
                        print("Не туда нажали")
                print("Выберите особый ингридиент\n19.Лемонграсс\n20.Имбирь\n21.Кокосовое молоко")
                key = int(input())
                match(key):
                    case 19:
                        if prod['Product'][18]['count'] > 0:
                            tom_yum.append(prod['Product'][18]['name'])
                            prod['Product'][18]['count'] -= сount
                            summ += prod['Product'][18]['cost']
                        else:
                            print("Продукт закончился")
                    case 20:
                        if prod['Product'][19]['count'] > 0:
                            tom_yum.append(prod['Product'][19]['name'])
                            prod['Product'][19]['count'] -= сount
                            summ += prod['Product'][19]['cost']
                        else:
                            print("Продукт закончился")
                    case 21:
                        if prod['Product'][20]['count'] > 0:
                            tom_yum.append(prod['Product'][20]['name'])
                            prod['Product'][20]['count'] -= сount
                            summ += prod['Product'][20]['cost']
                        else:
                            print("Продукт закончился")
                    case _:
                        print("Не туда нажали")
                print("Выберите топпинг\n22.Кинза\n23.Лайм\n24.Кунжутное масло")
                key = int(input())
                match(key):
                    case 22:
                        if prod['Product'][21]['count'] > 0:
                            tom_yum.append(prod['Product'][21]['name'])
                            prod['Product'][21]['count'] -= сount
                            summ += prod['Product'][21]['cost']
                        else:
                            print("Продукт закончился")
                    case 23:
                        if prod['Product'][22]['count'] > 0:
                            tom_yum.append(prod['Product'][22]['name'])
                            prod['Product'][22]['count'] -= сount
                            summ += prod['Product'][22]['cost']
                        else:
                            print("Продукт закончился")
                    case 24:
                        if prod['Product'][23]['count'] > 0:
                            tom_yum.append(prod['Product'][23]['name'])
                            prod['Product'][23]['count'] -= сount
                            summ += prod['Product'][23]['cost']
                        else:
                            print("Продукт закончился")
                    case _:
                        print("Не туда нажали")
                print(tom_yum)
                print(summ)
                input("Нажмите enter, чтобы продолжить")
            if key == '2':
                cycle = False
                Client_Menu()
            if key == '3':
                print(tom_yum)
                print(summ)
                print("Хотите сыграть в игру и получить скидку 30%?\n1.Да\n2.Нет")
                key = readchar.readkey()
                if key == '1':
                    if "thaisleg" in tom_yum:
                        print("Вы уже получили скидку!")
                    else:
                        print("Введите число от 1 до 10")
                        num = int(input())
                        ran = randint(1, 10)
                        if num == ran:
                            tom_yum.append(prod['Product'][24]['name'])
                            summ = summ - (summ / 100 * 30)
                            print(f"Сумма вашего заказа составляет: {summ}. Нажмите 1, чтобы оплатить")
                            key = readchar.readkey()
                            if key == '1':
                                try:
                                    user['User'][id]['money'] -= summ
                                    user['User'][0]['money'] += summ
                                    history = {'user_id' : id, 'summ' : summ, 'compound' : f"{tom_yum}"}
                                    his_order['Orders'].append(history)
                                    with open('products.json', 'w', encoding='utf8') as f:
                                        js.dump(prod, f, ensure_ascii=False, indent=2)
                                    with open('users.json', 'w', encoding='utf8') as f:
                                        js.dump(user, f, ensure_ascii=False, indent=2)
                                    with open('history.json', 'w', encoding='utf8') as f:
                                        js.dump(his_order, f, ensure_ascii=False, indent=2)
                                    print("Нужен чек?\n1.Да\n2.Нет")
                                    key = readchar.readkey()
                                    if key == '1':
                                        check = open(f"Check{id}.txt", 'w+')
                                        check.write(history)
                                        check.close()
                                        print("Чек в папке")
                                        cycle = False
                                        Client_Menu()
                                    if key == '2':
                                        cycle = False
                                        Client_Menu()
                                except Exception as e:
                                    print(e)
                            else:
                                print("Не туда нажали")
                        else:
                            print("На этот раз не повезло")
                if key == '2':
                    print(f"Сумма вашего заказа составляет: {summ}. Нажмите 1, чтобы оплатить")
                    key = readchar.readkey()
                    if key == '1':
                        user['User'][id]['money'] -= summ
                        user['User'][0]['money'] += summ
                        history = {'user_id' : id, 'summ' : summ, 'compound' : f"{tom_yum}"}
                        his_order['Orders'].append(history)
                        with open('products.json', 'w', encoding='utf8') as f:
                            js.dump(prod, f, ensure_ascii=False, indent=2)
                        with open('users.json', 'w', encoding='utf8') as f:
                            js.dump(user, f, ensure_ascii=False, indent=2)
                        with open('history', 'w', encoding='utf8') as f:
                            js.dump(his_order, f, ensure_ascii=False, indent=2)
                        print("Нужен чек?\n1.Да\n2.Нет")
                        key = readchar.readkey()
                        if key == '1':
                            print("Чек в папке")
                            cycle = False
                            Client_Menu()
                        if key == '2':
                            cycle = False
                            Client_Menu()
                        else:
                            print("Не туда нажали")
                else:
                    print("Не туда нажали")
            if key == '4':
                compound = str(tom_yum)
                print(f"Состав {compound}. Введите число ингридиента, который хотите удалить")
                ind = int(input())
                tom_yum.pop(ind - 1)
            else:
                print("Не туда нажали")
    except Exception as e:
        print("Компиляция умерла, python дурак")
        print(e)

#Build_TomYum()

def Main_Menu():
    print("Добро пожаловать в ресторан том яма!\n1.Авторизироваться\n2.Зарегистрироваться")
    key = readchar.readkey()
    if key == '1':
        print("Введите логин:")
        login = input()
        print("Введите пароль:")
        password = input()
        with open('users.json', encoding='utf8') as f:
            data = js.load(f)
            for i in range(len(data['User'])):
                if login == data['User'][i]['login'] and password == data['User'][i]['password']:
                    global id 
                    id = data['User'][i]['ID']
            print(id)
            if id == 0:
                Admin_Menu()
            if id > 0:
                Client_Menu()
    if key == '2':
        print("Введите имя")
        name = input()
        print("Придумайте логин:")
        login = input()
        print("Придумайте пароль:")
        password = input()
        id = 0
        with open('users.json', encoding='utf8') as f:
            data = js.load(f)
            for i in range(len(data['User'])):
                id = data['User'][i]['ID'] + 1
            print(id)
            user = {'ID' : id, 'name' : f'{name}', 'login' : f'{login}', 'password' : f'{password}', 'money' : 1500.00, 'role' : 'client'}
            data['User'].append(user)
            with open('users.json', 'w', encoding='utf8') as f:
                js.dump(data, f, ensure_ascii=False, indent=2)
                Main_Menu()
    else:
        print("Не туда нажали")

Main_Menu()