""""
estimate: 30 mins
actual: 40 mins
"""
email_name = {}

while True:
    email = input("Email: ")
    if not email:
        break
    username = email.split('@')[0]
    name = input(f"Is your name {username.title()}? (Y/n) ")
    if not name or name.lower() == "y":
        email_name[email] = username
    elif name.lower() == "n":
        name = input("Name: ")
        email_name[email] = name

for email, name in email_name.items():
    print(f"{name.title()} ({email})")


