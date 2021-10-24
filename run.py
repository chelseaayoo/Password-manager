#!/usr/bin/env python3.8
from credential import Credential
def create_credential(email,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(email,password)
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