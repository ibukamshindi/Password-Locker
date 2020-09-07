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

def create_new_credentials(account_name, account_password):
    """
    Function to create new account and password
    """
    new_credentials = Credentials(account_name,account_password)
    return new_credentials




