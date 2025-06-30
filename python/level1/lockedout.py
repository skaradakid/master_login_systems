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
    print("coming soon!")
main()