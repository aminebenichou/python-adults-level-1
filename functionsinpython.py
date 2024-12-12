def authentication(email, password):
    if email=="example@gmail.com" and password=="123456789":
        print("welcome...")
    else:
        print("Your credentials are wrong")
        qst = input("Did you forget your password? (answer with yes/no) : \n")
        if qst == "yes" :
            new_password = input("enter your new password : \n")
            confirm_password = input("Confirm your password : \n")
            if new_password == confirm_password and new_password!="123456789":
                authentication(email, new_password)


email = input("enter your email : \n")
password = input("enter your password : \n")

authentication(email, password)


# def sum_multiple_numbers(numbers):
#     result = 0
#     for number in numbers:
#         result = result + number

#     print(result)


# sum_multiple_numbers([1, 5, 8, 10, 12])













def somme(a, b):
    c = a + b 
    print(c)


somme(5, 7)
somme(1258, 59887)






