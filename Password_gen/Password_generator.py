"""
Author : Bharat Kshirsagar
Date : 13/01/2024
Goal : A password generator is a useful tool that generates strong and
random passwords for users. This project aims to create a
password generator application using Python, allowing users to
specify the length and complexity of the password.
User Input: Prompt the user to specify the desired length of the
password.
Generate Password: Use a combination of random characters to
generate a password of the specified length.
Display the Password: Print the generated password on the screen.

"""
import sys
import random
import string

def generate_password(len : int)->str:
    """
    These function is going to generate a password 
    from lowercase uppercase digit and special characters
    
    """
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_char = string.punctuation

    all_char = lower_case + upper_case + digits + special_char #concatinate all the characters

    #ensure the length of the password 
    #it should be greater than 8 
    if len < 8: 
        print("The length of password should be greater than or equal to 8 characters!")
        sys.exit(-1)

    password =  "".join((random.choice(all_char) for a in range(len)))
     
    return password

def main()->None:

    length = int(input("enter the desired length of the password: "))
    password = generate_password(length)

    print("Generated Password: ", password)

    sys.exit(0)


main()