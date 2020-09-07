#!/usr/bin/env python3.6
import random
from user import User
from credentials import Credentials

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


def main ():
    while True:

        print("Karibu to Password Locker")
        print('\n')
        print("Use these short codes to select an option : cu - create a new user, lg - login into account, ex - exit application")

        short_code = input ().lower()

        if short_code == 'cu':
          print ("Create a UserName")
          User_Name = input()



          print 




