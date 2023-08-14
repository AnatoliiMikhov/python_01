# some function
def show_message(message):
    print(message)


name = input("Enter your name: ")

show_message(f"\nHello, {name.title()} what do you would like to drink?")
