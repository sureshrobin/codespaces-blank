def user_info (**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

user_info(name = "Robin", age = 23, Location = "Chennai")
