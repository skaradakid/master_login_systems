def main():
    print("welome to lockedout!\ninput 1 for loging in\ninput 2 for registering")
    while True:
        try:
            choice = input("=> ")
            if not choice.isdigit():
                print("your answer has to be a number")
            elif choice != "1" and choice != "2":
                print("please chose from the given options 1 or 2")
            else:
                break
                
        except:
            print("something went wrong\n it's not you it's us")
    if choice == "1":
            login()
    else:
            signup()

def login():
    print("coming soon!")

def signup():
    while True:
        name = input("name: ")
        with open("python/level1/users.txt", "r") as file:
            open_file = file.readlines()
            new_list = []
            for x in open_file:
                new_list.append(x.strip().split(" "))
            list_of_names= []
            for x in new_list:
                list_of_names.append(x[0])
        if name in list_of_names:
            print("username already exist")
        else:
            break
                
    with open("python/level1/users.txt", "a") as file2:
        while True:
            password = input("password: ")
            password2 = input("confirm password: ")
            if password != password2:
                print("passwords do not match")
            else:
                print("passwords matched!")
                break
        file2.write(f"\n{name} {password}")
        print("signup complete")
    
    print("would you like to login? y/n")
    while True:
        answer = input("=> ")
        if answer != "y" and answer != "n":
            print("choose from the given options y/n")
        elif answer == "y":
            login()
        elif answer == "n":
            print("good bye!")
        break    
signup()