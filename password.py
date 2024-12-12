import random
import string

def generate_password():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symboles = string.punctuation

    all_charaters = lowercase + uppercase + digits + symboles

    password = ''.join(random.sample(all_charaters, random.randint(10,20)))
    
    return password

randompassword = generate_password()
print(randompassword + " hello from outside the function")