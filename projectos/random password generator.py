import string
import random

characters = list(string.ascii_letters + string.digits + "!@$#/&%")


def generate_password():
    password_length = int(
        input("Input the lenght you want your password to be: "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)


option = input("Do you want to generate a password? (Yes/No): ")

if option == "Yes":
    generate_password()
    quit()
elif option == "No":
    print("Program ended")
    quit()
else:
    print("invalid input")
    quit()


generate_password()
