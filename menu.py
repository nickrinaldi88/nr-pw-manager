import time
import pass_manager
import db_manager
import os

# how to check if program is run for the first time
# have a function that checks to see if the DB exists. If it does, don't run that function. If it doesn't, run that function


def login_success():

    print("----------Welcome to the Menu!----------")
    time.sleep(1)
    print("What would you like to do?")
    time.sleep(0.5)
    print("1. Add a new password")
    time.sleep(0.5)
    print("2. Update/Remove a password")
    time.sleep(0.5)
    print("3. Retrieve a password")
    time.sleep(0.5)
    print("4. Display all passwords")
    time.sleep(0.5)
    print("5. Exit")
    print("\n")


if not os.path.exists('master.txt'):
    # the the master file doesn't exist
    # run the first time function, else, run
    pass_manager.first_time()
    db_manager.create_table()

if pass_manager.check_master():
    print("----------You're in!----------")
    time.sleep(0.5)
    print("-"*30)
    time.sleep(0.5)

    while True:

        login_success()
        choice = input("Please enter your choice: ")
        print("\n")
        if choice == "1":
            pass_manager.add_password()
        elif choice == "2":
            pass_manager.update_password()
        elif choice == "3":
            pass_manager.retrieve_password()
        elif choice == "4":
            pass_manager.display_all()
        elif choice == "5":
            db_manager.close_db()
            break  # break here
    # if passwords don't match, print prompt, return to top
else:
    print("Your master password is not correct. Try Again. ")
