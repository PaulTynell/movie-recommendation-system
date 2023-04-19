# File: users.py
# Author: 
# this class will 
# prompt the user to enter their information, 
# save it to the users.txt file, and print a list of all users in the file

class User:
    def __init__(self, name="", age=0, gender="", preferred_genre=""):
        self.name = name
        self.age = age
        self.gender = gender
        self.preferred_genre = preferred_genre

    def set_name(self):
        self.name = input("Enter your name: ")
    
    def get_name(self):
        return self.name
    
    def set_age(self):
        self.age = int(input("Enter your age: "))
    
    def get_age(self):
        return self.age

    def set_gender(self):
        self.gender = input("Enter your gender: ")

    def get_gender(self):
        return self.gender

    def set_preferred_genre(self):
        self.preferred_genre = input("Enter your preferred genre: ")
    
    def get_preferred_genre(self):
        return self.preferred_genre
        

    def save_user_info(self):
        with open("users.txt", "a") as f:
            f.write(f"{self.name},{self.age},{self.gender},{self.preferred_genre}\n")


    def load_users(self):
        with open("users.txt", "r") as f:
            lines = f.readlines()
        users = []
        for line in lines:
            name, age, gender, preferred_genre = line.strip().split(",")
            users.append(User(name, int(age), gender, preferred_genre))
        return users


def main():
    user = User()
    user.set_name()
    user.set_age()
    user.set_gender()
    user.set_preferred_genre()
    user.save_user_info()

    users = user.load_users()

    print("All users:")
    print()
    for user in users:
        print(f"Name: {user.get_name()}")
        print(f"Age: {user.get_age()}")
        print(f"Gender: {user.get_gender()}")
        print(f"Preferred Genre: {user.get_preferred_genre()}")
        print()


if __name__ == "__main__":
    main()






