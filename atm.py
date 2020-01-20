def verify_pin(pin):
    pins='1234'
    if pin == pins:
        return True
    else:
        return False

def log_in():
    tries = 0
    while tries < 3:
        pin = input('Please Enter Your 4 Digit Pin: ')
        if verify_pin(pin):
            print("Pin accepted!")
            return True
        else:
            print("Invalid pin")
            tries += 1
    print("No more tries. Could not log in")
    return False
def reg():
    name=input('Please enter your account name:')
    accountnum=input('Please enter your account number:')
    print('account register successful')
    print('your account name is :',name)
    print('your account number is:',accountnum)

def start_menu():
    print("Welcome to python ATM machine")
    restart=('Y')
    # chances = 3
    balance = 260.14
    reg()
        
        # print('your account number is:',accountnum)
        # print('your balance is:',balance)
    if log_in():
        while restart not in ('n','NO','no','N'):
            print('Please Press 1 For Your Balance\n')
            print('Please Press 2 To Make a Withdraw\n')
            print('Please Press 3 To Pay in\n')
            # print('Please Press 4 To Return Card\n')
            print('Please Press 4 To recharge\n')
            print('Please Press 5 To change pin\n')
            option= int(input('What Would you like to choose?'))
            if option ==1:
                print('Your Balance is #',balance,'\n')
                restart= input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You for Banking with us')
                    break
            if option ==2:
                # print('How Much Would u like Withdraw?')
                option2 = ('y')
                withdraw = float(input('How Much Would u like Withdraw? \n#10/#20/#40/#60/#80/#100  for other enter 1:'))
                if balance <=withdraw:
                    print('Insufficient balance')
                elif withdraw in [10,20,40,60,80,100]:
                    balance=balance - withdraw
                    print('Your balance is #',balance)
                    restart==input('Would You you like to go back? ')
                    if restart in ('n','no','No','N'):
                        print('Thank You for Banking with us')
                        break   
                
                    
                elif withdraw != [10,20,40,60,80,100]:
                    print('Invalid Amount, Please Re-try')
                    restart=('y')
                    if withdraw == 1:
                        withdraw=float(input('Please Enter Desired amount:'))
                        if balance <= withdraw:  
                            print('Insufficient balance')
                        else:   

                            balance=balance - withdraw
                            print('Your balance is #',balance)
            if option == 3: 
                payin=float(input('How Much Would You like To pay In?'))
                balance=balance + payin
                print('Your new Balance is #',balance)
                restart=input('Would You you like to go back? ')
                if restart in ('n','no','No','N'):
                    print('Thank You for Banking with u')
                    break

            if option == 4:
                number=float(input('Please enter Your number:'))
                amount=float(input('Please enter the amount :'))
                if balance <=amount:
                    print('Insufficient balance')
                else:   
                    balance=balance - amount
                    print('Your balance is #',balance)
                    print(amount,'Successful recharge to your number',number )
                    restart=input('Would You you like to go back? ')
                    if restart in ('n','no','No','N'):
                        print('Thank You for Banking with u')
                        break
                        
        # you will need to make this one yourself!
        # main_menu()
    print("Exiting Program")

start_menu()
# print('Welcome to motee Bank ATM')
# restart=('Y')
# chances = 3
# balance = 67.14
# # pins=
# while chances >= 0:
#     pin = int(input('Please Enter You 4 Digit Pin: '))
#     if pin == (1234):
#         print('You entered you pin Correctly\n')
#         while restart not in ('n','NO','no','N'):
#             print('Please Press 1 For Your Balance\n')
#             print('Please Press 2 To Make a Withdrawl\n')
#             print('Please Press 3 To Pay in\n')
#             print('Please Press 4 To Return Card\n')
#             option = int(input('What Would you like to choose?'))
#             if option == 1:
#                 print('Your Balance is #',balance,'\n')
#                 restart = input('Would You you like to go back? ')
#                 if restart in ('n','NO','no','N'):
#                     print('Thank You')
#                     break
#             elif option == 2:
#                 option2 = ('y')
#                 withdrawl = float(input('How Much Would you like to withdraw? \n#10/#20/#40/#60/#80/#100 for other enter 1: '))
#                 if withdrawl in [10, 20, 40, 60, 80, 100]:
#                     balance = balance - withdrawl
#                     print ('\nYour Balance is now #',balance)
#                     restart = input('Would You you like to go back? ')
#                     if restart in ('n','NO','no','N'):
#                         print('Thank You')
#                         break
#                 elif withdrawl != [10, 20, 40, 60, 80, 100]:
#                     print('Invalid Amount, Please Re-try\n')
#                     restart = ('y')
#                 elif withdrawl == 1:
#                     withdrawl = float(input('Please Enter Desired amount:'))    

#             elif option == 3:
#                 Pay_in = float(input('How Much Would You Like To Pay In? '))
#                 balance = balance + Pay_in
#                 print ('\nYour Balance is now #',balance)
#                 restart = input('Would You you like to go back? ')
#                 if restart in ('n','NO','no','N'):
#                     print('Thank You')
#                     break
#             elif option == 4:
#                 print('Please wait whilst your card is Returned...\n')
#                 print('Thank you for you service')
#                 break
#             else:
#                 print('Please Enter a correct number. \n')
#                 restart = ('y')
#     elif pin != ('1234'):
#         print('Incorrect Password')
#         chances = chances - 1
#         if chances == 0:
#             print('\nNo more tries')
#             break