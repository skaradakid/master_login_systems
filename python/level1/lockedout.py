allowed_characters = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z']

def main():
    print("welome to lockedout!\ninput 1 for loging in\ninput 2 for registering")
    while True:
        try:
            choice = input("=> ")
            if not choice.isdigit():
                print("your answer has to be a number")
            elif choice != "1" and choice != "2":
                print("please chose from the given options \n1(login)\n2(register)")
            else:
                break
                
        except:
            print("something went wrong\n it's not you it's us")
    if choice == "1":
            login()
    elif choice =="2":
        signup()
    else:
        print("goodbye")

def login():
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
        if name not in list_of_names:
            print("username does not exist")
            ans = input("try again? y/n")
            if ans == "n":
                print("good bye!")
                break
            else:
                continue
        else:
            chances = 3
            while chances > 1:
                entered = input("Enter password: ")
                index = list_of_names.index(name)
                hashed = decrypt(new_list[index][1])
                if entered == hashed:
                    print("Access granted!")
                    break
                elif chances < 1:
                    print("login failed!")
                    break
                else:
                    print("Access denied.")
                    chances-=1
                    print(f"you have {chances} remaining")
        break
            
        
    

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
        file2.write(f"\n{name} {encrypt(password)}")
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

def encrypt(password):
    new_string = ""
    for x in password:
        print(x)
        if x in allowed_characters:
            new_string+= allowed_characters[(allowed_characters.index(x) + 13) % len(allowed_characters)]
        else:
            new_string+="@"
    return new_string



def decrypt(password):
    new_string = ""
    for x in password:
        if x in allowed_characters:
            new_string+= allowed_characters[(allowed_characters.index(x) - 13) % len(allowed_characters)]
        else:
            new_string+="@"
    return new_string

main()
