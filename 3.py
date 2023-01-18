''' 
 Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
 Создайте список friends и добавьте в него N словарей с ключами name и age.
 Найдите самого младшего из друзей и выведите его имя
'''

N = int(input("Введите количество друзей: "))
= = []

for index in range(N):

    friend = dict()

    key = input("Введите имя друга: ")
    value = input("Введите возраст друга: ")

    friend[key] = value
    friends.append(friend)

print(friends)

Main_name = 'none'
Min_age = 1000

for friend in friends: 
    for name in friend.keys(): 
        if Min_age > int(friend[name]):
            Main_name = name
            Min_age = int(friend[name])

print("Самый младший друг:", Main_name)