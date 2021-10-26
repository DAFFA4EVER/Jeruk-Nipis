user_list = []
id = 0

class user:
    def __init__(self, uid, name, age, film, food, address):
        self.uid = uid
        self.name = name
        self.age = age
        self.film = film
        self.food = food
        self.address = address


def save_list():
    global user_list
    data_list = open(r'1.0\user_data_list', 'w')
    for i in user_list:
        data = {
            "uid": f'{i.uid}',
            "name": f'{i.name}',
            "age": f'{i.age}',
            "film": f'{i.film}',
            "food": f'{i.food}',
            "address": f'{i.address}'
        }
        data_list.write(str(data))
    data_list.close()


def create():
    global user_list, id
    uid = ""
    name = input("Please insert your name : ")
    age = int(input("Please insert your age : "))
    flag = input("Do you have favorite movies/film? ")
    film = ""
    food = ""
    address = ""
    if flag == "yes" or flag == "y":
        film = input("Please insert your favorite film : ")

    flag = input("Do you have favorite food? ")
    if flag == "yes" or flag == "y":
        food = input("Please insert your favorite food : ")

    uid = f'{id + 1}'
    user_list.append(user(uid, name, age, film, food, address))
    save_list()
    return user_list

def see_user():
    global user_list
    n=0
    for i in user_list:
        print(f"{n+1} : {i.name}")
        n = n + 1