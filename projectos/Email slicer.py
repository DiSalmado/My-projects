def main():
    print(" Welcome to my email silcer. ")
    print(" ")


while True:
    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username : ", username)
    print("Domaim", domain)
    print("Extension", extension)

main()
