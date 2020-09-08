#!/usr/bin/env python3.6
import random
from user import User
from credentials import Credentials
import string 


def create_user(username,password):
    """
    Function to create a new user
    """
    new_user = User(username, password)
    return new_user

def save_user(user):
    """
    function to save user 
    """
    user.save_user()

def create_new_credential(account_name, account_password):
    """
    Function to create new account and password
    """
    new_credential = Credentials(account_name,account_password)
    return new_credential

def save_credential(credentials):
    """
    Function to save newly created account and password
    """
    credentials.save_credentials()

def display_credentials():
    """
    Function that displays all saved credentials
    """
    return Credentials.display_credentials()    

def del_credential(credentials):
    """
    Function to delete a credentials
    """
    credentials.delete_credential()

def find_credential(account_name):
    """Function that finds credentials based on account_name given"""
    return Credentials.find_by_name(account_name)


def check_existing_credentials(name):
    """Method that checks whether a particular account and its credentials exist based on searched account_name"""
    return Credentials.find_by_name(name)


def main ():
    while True:

        print("Karibu to Password Locker")
        print('\n')
        print('''
             Use these short codes to select an option: 
             'cu' to create a new user:
             'lg' to login into account
             'ex' to exit application''')
        short_code = input('Enter a choice').lower()
        print('\n')
        if short_code == 'cu':
            print("Create a UserName")
            created_user_name = input()

            print("Select a Password")
            created_user_password = input()

            print("Confirm Your Password")
            confirm_password = input()

            while confirm_password != created_user_password:
                print("Sorry your passwords did not match!")
                print("Enter a password")
                created_user_password = input()
                print("Confirm Your Password")
                confirm_password = input()
            else:
                print(f"Congratulations {created_user_name}! You have created your new account.")
                print('\n')
                print("Proceed to Log In to your Account")
                print("Username")
                entered_userName = input()
                print("Your Password")
                entered_password = input()

                while entered_userName != created_user_name or entered_password != created_user_password:
                    print("You entered a wrong username or password")
                    print("Username")
                    entered_userName = input()
                    print("Your Password")
                    entered_password = input()
                else:
                    print(f"Welcome: {entered_userName} to your Account")
                    print('\n')

                    print("Select an option below to continue: Enter 1, 2, 3,or 4")
                    print('\n')

                while True:
                    print("1: View Your saved credentials")
                    print("2: Add new credentials")
                    print("3: Remove credentials")
                    print("4: Log Out")
                    option = input()

                    if option == '2':
                        while True:
                            print("Continue to add? y/n")

                            choice = input().lower()
                            if choice == 'y':
                                print("Enter The Account Name")
                                account_name = input()
                                print("Enter a password")
                                print(
                                    "To generate random password enter keyword 'gp' or 'c' to create your own password")
                                keyword = input().lower()
                                if keyword == 'gp':
                                    account_password = random.randint(111111, 1111111)
                                    print(f"Account: {account_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')
                                elif keyword == 'c':
                                    print("Create your password")
                                    account_password = input()
                                    print(f"Account: {account_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')

                                else:
                                    print("Please enter a valid Code")

                                save_credential(create_new_credential(
                                    account_name, account_password))
                            elif choice == 'n':
                                break
                            else:
                                print("Please use 'y' for yes or 'n' for no!")
                    elif option == '1':
                        while True:
                            print("Below is a list of all your credentials")
                            if display_credentials():

                                for credential in display_credentials():
                                    print(f"ACCOUNT NAME:{credential.account_name}")
                                    print(f"PASSWORD:{credential.account_password}")

                            else:
                                print('\n')
                                print("You don't seem to have any credentials yet")
                                print('\n')

                            print("Back to Menu? y/n")

                            back = input().lower()
                            if back == 'y':
                                break
                            elif back == 'n':
                                continue
                            else:
                                print("Please Enter a valid code")
                                continue

                    elif option == '4':
                        print("WARNING!  Are you sure? y/n")
                        logout = input().lower()

                        if logout == 'y':
                            print("You have Successfully logged out")
                            break
                        elif logout == 'n':
                            continue
                    elif option == '3':
                        while True:
                            print("Search for credential to delete")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(search_name)
                                print(f"ACCOUNT NAME: {search_credential.account_name} \n PASSWORD: {search_credential.account_password}")
                                print("Delete? y/n")
                                sure = input().lower()
                                if sure == 'y':
                                    del_credential(search_credential)
                                    print("Account SUCCESSFULLY deleted")
                                    break
                                elif sure == 'n':
                                    continue
                            else:
                                print("That Contact Does not exist")
                                break

        elif short_code == 'lg':
            print("WELCOME")
            print("Enter UserName")
            default_user_name = input()

            print("Enter Your password")
            default_user_password = input()
            print('\n')

            while default_user_name != 'testuser' or default_user_password != '12345':
                print("Wrong userName or password. Username 'testuser' and password '12345'")
                print("Enter UserName")
                default_user_name = input()

                print("Enter Your password")
                default_user_password = input()

                print('\n')

            if default_user_name == 'testuser' and default_user_password == '12345':
                print("YOU HAVE SUCCESSFULLY LOGGED IN!")
                print('\n')
                print("Select an option below to continue: Enter 1, 2, 3, or 4")
                print('\n')

            while True:
                print("1: View Your saved credentials")
                print("2: Add new credentials")
                print("3: Remove credentials")
                print("4: Log Out")
                option = input()

                if option == '2':
                    while True:
                        print("Continue to add? y/n")

                        choice = input().lower()
                        if choice == 'y':
                            print("Enter The Account Name")
                            account_name = input()
                            print("Enter a password")
                            print(
                                "To generate random password enter keyword 'gp' or 'c' to create your own password")
                            keyword = input().lower()
                            if keyword == 'gp':
                                account_password = random.randint(111111, 1111111)
                                print(f"Account: {account_name}")
                                print(f"Password: {account_password}")
                                print('\n')
                            elif keyword == 'c':
                                print("Create your password")
                                account_password = input()
                                print(f"Account: {account_name}")
                                print(f"Password: {account_password}")
                                print('\n')

                            else:
                                print("Please enter a valid Code")

                            save_credential(create_new_credential(
                                account_name, account_password))
                        elif choice == 'n':
                            break
                        else:
                            print("Please use 'y' for yes or 'n' for no!")
                elif option == '1':
                    while True:
                        print("Below is a list of all your credentials")
                        if display_credentials():

                            for credential in display_credentials():
                                print(f"ACCOUNT NAME:{credential.account_name}")
                                print(f"PASSWORD:{credential.account_password}")

                        else:
                            print('\n')
                            print("You don't seem to have any contacts yet")
                            print('\n')

                        print("Back to Menu? y/n")

                        back = input().lower()
                        if back == 'y':
                            break
                        elif back == 'n':
                            continue
                        else:
                            print("Please Enter a valid code")

                elif option == '4':
                    print("WARNING! Are you sure? y/n")
                    logout = input().lower()

                    if logout == 'y':
                        print("You have Successfully logged out")
                        break
                    elif logout == 'n':
                        continue

                elif option == '3':
                    while True:
                        print("Search for credential to delete")

                        search_name = input()

                        if check_existing_credentials(search_name):
                            search_credential = find_credential(search_name)
                            print(f"ACCOUNT NAME: {search_credential.account_name} \n PASSWORD: {search_credential.account_password}")
                            print("Delete? y/n")
                            sure = input().lower()
                            if sure == 'y':
                                del_credential(search_credential)
                                print("Account SUCCESSFULLY deleted")
                                break
                            elif sure == 'n':
                                continue

                        else:
                            print("That Contact Does not exist")
                            break

if __name__ == '__main__':
    main()

#         if short_code == 'cu':
#             print("Create a username")
#             username = input()
#             print("Select a Password")
#             password = input()
#             save_user(create_user(username,password))
#             print(f'New account created for {username} using password:{password}')

#             while True:
#                 print(f'Karibu {username} please choose an option to continue.')
#                 print ( '''
#                 Use these short codes to select an option: 
#                 'cc' to create credentials:
#                 'dc' to display credentials
#                 'ex' to exit ''')
#                 short_code = input('Enter a choice').lower()
#                 if short_code =='cc':
#                   print('Enter your credential details:')
#                   account_name = input()
#                   while True:
#                          print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
#                          psw_choice = input('Enter an option: ').lower()
#                          if psw_choice == 'ep':
#                            password = input('Enter your password: ')
#                            break
#                          elif psw_choice == 'gp':
#                            password = random.randint(111111, 1111111)
#                            break
#                          elif psw_choice == 'ex':
#                            break
#                          else:
#                            print('Wrong option entered. Try again.')

#                          save_credentials(create_credentials(account_name,password)



# if __name__ == '__main__':
#     main()

        # if short_code == 'ex':
        #         break
        # elif short_code == 'cu':
        #     print("Create a username")
        #     username = input()
        #     print("Select a Password")
        #     password = input()
        #     save_user(create_user(username,password))
        #     print(f'New account created for {username} using password:{password}')
        # elif short_code == 'lg':
        #     print('To log in, enter your account details')
        #     print("Enter username")
        #     username = input ()
        #     print("Enter password")
        #     password = input ()
  
        #     while True:
        #         print(f'Karibu {username}.please choose an option to continue.')
        #         print ( '''
        #         Use these short codes to select an option: 
        #         'cc' to create credentials:
        #         'dc' to display credentials
        #         'ex' to exit ''')
        #         short_code = input('Enter a choice').lower()

        #         if short_code == 'ex':
        #                 print (f'Goodbye {username}')
        #                 break


            #     elif short_code =='cc':
            #       print('Enter your credential details:')
            #       account_name = input()
            #       while True:
            #              print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
            #              psw_choice = input('Enter an option: ').lower()
            #              if psw_choice == 'ep':
            #                password = input('Enter your password: ')
            #                break
            #              elif psw_choice == 'gp':
            #                password = random.randint(111111, 1111111)
            #                break
            #              elif psw_choice == 'ex':
            #                break
            #              else:
            #                print('Wrong option entered. Try again.')
            #       save_credentials(create_credentials(account_name,password))
            #       print(f'Credential Created: Account Name: {account_name} - Password: {password}')
                  
            #     elif short_code == 'dc':
            #       if display_credentials():
            #         print('Here is a list of all your credentials')
            #         for credential in display_credentials():
            #           print(f'Account Name: {credential.account_name} - Password: {credential.password}')
            #       else:
            #         print("You don't seem to have any credentials saved yet")
                    
            # else: 
            #   	print('Wrong details entered. Try again or Create an Account.')