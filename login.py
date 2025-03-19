user = input("INPUT USER NAME > ")
password = input("INPUT PASSWORD > ")

print("YOU LOGIN") # from master
def generate(info):
    return "".join(map(lambda char: f"+{char}+",info))

print(f"Your username: {generate(user)}", f"Your password: {generate(password)}", sep="\n")
