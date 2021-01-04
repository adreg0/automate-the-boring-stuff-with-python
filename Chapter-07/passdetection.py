import re

def strongPassword(password):
    passlen = re.compile(r'(.{8,})')
    passnum = re.compile(r'[0-9]+')
    passlower = re.compile(r'[a-z]')
    passupper = re.compile(r'[A-Z]')
    if passlen.search(password)==None:
        print('Password must be atleast 8 characters long')
    elif passnum.search(password)==None:
        print('Password must contain atleast one number')
    elif passlower.search(password)==None:
        print('Password must contain atleast one lower case letter')
    elif passupper.search(password)==None:
        print('Password must contain atleast one upper case later')
    else:
        print('Strong password')



password=input()
strongPassword(password) 
