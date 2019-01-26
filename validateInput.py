while True:
    print("Enter your age")
    age = input()
    if age.isdecimal():
        break
    print("Please enter a numbeer for your age")

while True:
    print("Set a new Password (letters and numbers only)")

    pwd = input()
    if pwd.isalnum():
        break
    print("Password can only have letters and numbers")