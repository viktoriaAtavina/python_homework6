'''
    Пользователь вводит число N. 
    Затем он вводит личные данные (имя и возраст) своих N друзей. 
    Создайте список friends и добавьте в него N словарей с ключами name и age.
    Выведите средний возраст всех друзей и самое длинное имя.
'''

N = int(input("Введите количество друзей: "))
friends = []

for index in range(N):

    friend = dict()

    key = input("Введите имя друга: ")
    value = input("Введите возраст друга: ")

    friend[key] = value
    friends.append(friend)

print(friends)

Main_name = ' '
Sum = 0

for friend in friends: 
    for name in friend.keys():
        Sum += int(friend[name])
        if len(Main_name) < len(name):
            Main_name = name

print("Средний возраст %.2f:" %(Sum / len(friends)))
print("Самое длинное имя:", Main_name)