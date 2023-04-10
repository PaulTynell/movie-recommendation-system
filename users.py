# File: users.py
# Author: 
# class to handle all user information and actions

class User:
    def __init__(self, name, age, gender, preferred_genre):
        self.name = name
        self.age = age
        self.gender = gender
        self.preferred_genre = preferred_genre


def get_user_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    preferred_genre = input("Enter your preferred genre: ")
    return User(name, age, gender, preferred_genre)


def save_user_info(user):
    with open("users.txt", "a") as f:
        f.write(f"{user.name},{user.age},{user.gender},{user.preferred_genre}\n")


def load_users():
    with open("users.txt", "r") as f:
        lines = f.readlines()
    users = []
    for line in lines:
        name, age, gender, preferred_genre = line.strip().split(",")
        users.append(User(name, age, gender, preferred_genre))
    return users


def main():
    user = get_user_info()
    save_user_info(user)
    users = load_users()
    print("All users:")
    print()
    for user in users:
        print(f"Name: {user.name}")
        print(f"Age: {user.age}")
        print(f"Gender: {user.gender}")
        print(f"Preferred Genre: {user.preferred_genre}")
        print()


if __name__ == "__main__":
    main()






