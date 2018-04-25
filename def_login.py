#Program to sign_up and login using funtion,
#Here user will be asked whether to sign up or login 
#If user choses to sign up all the details will be stored in different shell
#of the excell sheet
#And during the logging in username and password will be matched with the
#stored details in the sheet ,if matched login successfull else it will show
#the error message as 'username or password is incorrect'


import time
import re
import datetime
import openpyxl,xlwt
import smtplib, time
wb = xlwt.Workbook()
ws = wb.add_sheet("Def_login ")
def sign_up():
        print("Enter your detail to sign up ")


        x = 'y'
        while(x == 'y'):
            first_name = input('Enter your first name ')
            last_name = input('Enter your last name ')
            date_of_birth = input('Enter DOB ')
            #dob_time = datetime.strptime(date_of_birth, '%b %d %Y')
            mob_no = input('Enter your mob. no. ')
            mo=1

            while mo:
                if len(mob_no) != 10:
                    print("please enter 10 digit mob no")
                    mob_no = input('Enter your mob. no. again: ')
                else:
                    mo=0
            address = input('Enter your address ')
            UserName = input("Enter the username to login into your accout ")
            

            print('Enter your username and password to log in ')
            p = True
            while p:
                PassWord = input("Now please create a password. ")
                PassWordCheck = input("Please Re Enter the password \n ")
                if PassWord.lower() == PassWordCheck.lower():
                    if (len(PassWord)<6 or len(PassWord)>12):
                        continue
                    elif not re.search("[a-z]",PassWord):
                        continue
                    elif not re.search("[0-9]",PassWord):
                        continue
                    elif not re.search("[A-Z]",PassWord):
                        continue
                    elif not re.search("[$#@]",PassWord):
                        continue
                    elif re.search("\s",PassWord):
                        continue
                    else:
                        print("Valid Password")
                        print('Password succesfully saved')
                        p=False
                        break
                else:
                    print ("Passwords Do Not Match!\nPlease Re Try.")
                

            file = open("Def_Login.xls","a+")
            '''file.write ('A1', columnfirst_name)
            file.write('B1', last_name)
            file.write('C1', date_of_birth)
            file.write('D1', mob_no)
            file.write('E1', address)'''
            file.write ( UserName +","+PassWord + "\n")
            #file.write (",")
            #file.write (PassWord)
            #file.write("\n")
            file.close()

            print ("Your login details have been saved. ")
            x = input('Do you want to enter another detail: ')
            x = x.lower()



def login():
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("Username can't be blank")
        else:
            break
    while True:
        password = input("Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
        else:
            break

    if username == username:
        print('login successfull')
    else:
        print("Invalid username or password")
            
def exit():
    print ('Wrong input, try again')



print("Welcome to the system. Please register or login.")
print("Options: sign_up | login | exit")
while True:
    option = input("> ")
    if option == "login":
        login()
    elif option == "sign_up":
        sign_up()
    elif option == "exit":
        break
    else:
        print(option + " is not an option")

    
    
