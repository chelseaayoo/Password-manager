#!/usr/bin/env python3.8
#!/usr/bin/env python3.6
from credential import Credential
from user import User
def create_credential(login_username,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(login_username,password)
    return new_credential
def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()
def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()
def find_credential(login_username):
    '''
    Function that finds a credential by email and returns the credential
    '''
    return Credential.find_by_login_username(login_username)
def check_existing_credentials(login_username):
    '''
    Function that check if a credential exists with that login_username and return a Boolean
    '''
    return Credential.credential_exist(login_username)
def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()
def create_user(email,first_name,last_name):
    '''
    Function to create a new user
    '''
    new_user = User(email,first_name,last_name)
    return new_user
def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
def find_user(email):
    '''
    Function that finds a user by email and returns the user
    '''
    return User.find_by_email(email)
def check_existing_users(email):
    '''
    Function that check if a user exists with email and return a Boolean
    '''
    return User.user_exist(email)
def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def main():
    print("Hello Welcome to your credential list. What is your name?")
    login_username = input()

    print(f"Hello {login_username}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential,  delc -delete credential, ex -exit the credential list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Credential")
                            print("-"*10)

                            print ("First name ....")
                            first_name = input()

                            print("Last name ...")
                            last_name = input()

                            print("Login username ...")
                            login_username = input()

                            print("Password ...")
                            password = input()

                            print("Email address for account login ...")
                            email = input()


                            save_credentials(create_credential(login_username,password)) # create and save new credential.
                            print ('\n')
                            print(f"New Credential with login username:  {login_username}  with password: {password} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your credentials")
                                    print('\n')

                                    for credential in display_credentials():
                                            print(f"Login Username : {credential.login_username} Password: {credential.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the login username you used while creating your credential")

                            search_login_username = input()
                            if check_existing_credentials(search_login_username):
                                    search_credential = find_credential(search_login_username)
                                    print(f"{search_credential.login_username} Your password is  {search_credential.password}")
                                    print('-' * 20)

                                    # print(f"Phone number.......{search_contact.phone_number}")
                                    # print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That credential does not exist")
                    elif short_code == 'delc':
                        if del_credential(create_credential):
                            print("choose credentials to delete")
                            print('\n')
                            for credential in del_credential():
                                print("{credential}")
                        else:
                            print('\n')
                            print("no credential deleted")
                            print('\n')


                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':

      main()                                