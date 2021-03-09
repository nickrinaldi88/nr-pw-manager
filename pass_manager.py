import time
import db_manager
import hash_script
import pyperclip


def first_time():
    master = input(
        "Please create your master password. (Store in a safe place!): ")
    with open('master.txt', 'w+') as f:
        f.write(master)

    print(
        f"Your master password is {master}. It has been saved to master.txt in your current directory.")
    print("-"*30)
    time.sleep(1)
    print("NOTE: You will be prompted to confirm your password in the next menu!")
    time.sleep(1)
    print("-"*30)


def check_master():

    mast = input("Please enter your master password: ")
    with open('master.txt', "r") as f:
        for line in f:
            if mast == line:
                return True
        return False


def add_password():
    print("---------ADD A PASSWORD--------")
    # take inputs
    svc = input("Enter service: ")
    user = input("Enter your username: ")
    manual = input("Would you like to manually enter your own password(y/n): ")
    if manual == "y":
        personal = input("Please enter your own password: ")
        print("Your password for " + svc + " is: " + personal)
        time.sleep(0.5)
        print("-"*30)
        time.sleep(0.5)
        pyperclip.copy(personal)
        print("Password for " + svc + " has been copied to the clipboard!")
        print("-"*30)
        db_manager.db_add(svc, user, personal)
        time.sleep(1)
        print("The password for " + svc + " has been added to the database!")
        print("-"*30)
        print("\n")
        time.sleep(1)
    else:

        length = int(
            input("Enter the desire length of your encrypted password: "))
        custom = input(
            "Would you like a password with special characters, or without special characters?(1-with/2-without): ")
        if custom == '2':
            cust_pwd = hash_script.custom_pwd(length)
            print("Your generated password for " + svc + " is: " + cust_pwd)
            time.sleep(0.5)
            print("-"*30)
            time.sleep(0.5)
            pyperclip.copy(cust_pwd)
            print("Password for " + svc + " has been copied to the clipboard!")
            print("-"*30)
            db_manager.db_add(svc, user, cust_pwd)
            time.sleep(1)

            print("The password for " + svc +
                  " has been added to the database!")
            print("-"*30)
            print("\n")
            time.sleep(1)
        else:
            # generate password
            final = hash_script.final_pwd(length)
            print("Your generated password for " + svc + " is: " + final)
            time.sleep(0.5)
            print("-"*30)
            time.sleep(0.5)
            pyperclip.copy(final)
            print("Password for " + svc + " has been copied to the clipboard!")
            print("-"*30)

        # Save password to clipboard

            db_manager.db_add(svc, user, final)
            time.sleep(1)

            print("The password for " + svc +
                  " has been added to the database!")
            print("-"*30)
            print("\n")
            time.sleep(1)


def update_password():

    while True:
        svc = input("Enter the service would you like to update:  ")

        time.sleep(1)
        # check if svc exists in db
        if db_manager.db_chek(svc) == False:
            break

        # except:
        #     print("there's an error")
        #     break
        print("-"*30)
        option = input(
            "Would you like to update or remove the password from this service? (1/Update, 2/Remove): ")

        if option == "1":

            print("-"*30)

            print("You would like to update the password for " + svc + "."
                  )

            # update :

            print("-"*30)

            length = int(input(
                "Enter the desired length for your new encrypted password: "))
            print("-"*30)

            new_pwd = hash_script.final_pwd(length)
            db_manager.db_update(svc, new_pwd)
            time.sleep(1)
            print("The password for " + svc +
                  " has been updated to: " + str(new_pwd))
            print("\n")
            time.sleep(2)

            break

        elif option == "2":
            # remove
            print("-"*30)
            print("You would like to remove this service from the database..")
            print("-"*30)
            time.sleep(1)
            ru_sure = input(
                "Are you sure you want to remove this password? (y/n): ")
            if ru_sure == 'y':
                time.sleep(1)
                db_manager.db_remove(svc)
                print("-"*30)
                print(svc + " has been successfully removed!")
                print("\n")
                time.sleep(2)
            elif ru_sure == 'n':
                print("-"*30)
                print("Returning to menu...")
                print("\n")
                time.sleep(2)

            break


def retrieve_password():

    while True:
        svc = input(
            "Enter the service you want to retrieve the password from: ")
        print("-"*30)
        time.sleep(1)
        try:
            db_manager.db_chek(svc)

            time.sleep(1)
        except:

            print("There's an error!")

        db_manager.db_grab(svc)
        exit = input("Would you like to exit? (y/n) ")

        if exit == "y":
            break


def display_all():

    while True:

        time.sleep(1)

        db_manager.display_db()
        time.sleep(1)

        exit = input("Would you like to exit?(y/n) ")

        if exit == "y":
            print("\n")
            break

    # closing functionality
