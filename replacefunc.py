'''def replaceString(replace='nn'):
    return f'welcome A{replace}oited'
print(replaceString('nn'))'''





def replacestring(word,search,replaceWith):
  a=word,replaceWith(word,replaceWith)
  return a
pass
 



'''def changeCase(sentence,case):
 print(changeCase('ABDULHAMID','lower'))'''




'''def muti(*numebers):#passing a variable numbers of arguement
    total=1
    for a in numbers:
        total*a
    return total
print(muti(3,4,5,6))
pass'''


'''def Sum(*numbers):
    total=0
    for number in numbers:
        total+=number
    return total
pass'''









'''def withdrawalcash():
    withdraw_amount = float(input('please enter amount to be withdrawn:'))
    username = float(input('Please enter username:'))
    filename =username+'Gimba Halam:'
    transactionfilename =username+'_transactionhistory,txt'
    transactionfile =open(transactionfilename,'a')
    file =open(filename,'a')
    balance =0
    new_balance = 0

    with open(filename,'a') as file:
        for i in file:
            balance = float(i)
    with open(filename,'w') as file2:
        if withdrawn_amount > balance:
            print('You have insufficient balance.Your balance is low',balance)



        else:
            new_balance = balance - withdrawn_amount
            new_balance = str(new_balance)
            file2.write(new_balance)
            print('Your new balance is:',new_balance)
            with open (transactionfilename,'a') as file3:
                balance = str(balance)
                withdrawn_amount = str(withdrawn_amount)
                file3.write(str(datatime,datatime,now()))
                file3.write('\nPrevious balance:'+bvalance+'. Withdrawn amount is'+withdrawn_amount+'.New balance:'+new_balance+'\n')
    file,close()'''


'''def trimEdges(sentence):
    word = sentence
    return word.strip()
pass'''







'''def main():
    dict = startup('accounts.csv')#dict dictionary name in main()
    if dict == None:
        return
    pin, value = verifyPin(dict)
    if pin == None:
        msg = value
        print(msg)
        return 'Good bye'
    name = value

    while True:
        print()
        choice = verifyMenuChoice(name)
        if choice == 2:
            deposit(pin, dict)
        elif choice == 3:
            withdraw(pin, dict)
        elif choice == 1:
            b = balance(pin , dict)
            msg = 'Your current balance is $(200)'
            print (msg.format(b))
        elif choice == 4:
            fname, lname = quit(pin, dict)
            if fname== None and lname == None:
                pass
            else:
                str = '\n{} {}, thank you for using the keystone banking system'
                print(str.format(fname, lname))
                break
    return 'Goodbye' '''


'''def atm():
    inputlimit=0
    while inputlimit<3:
        pin=int(input('Enter your pin:'))
        if pin==2022:
            print('Logged in')
            break
        elif inputlimit ==1:
            print('Try again please')
        elif inputlimit ==2:
            print('invalid pin')
        else:
            print('Try Again')
        inputlimit+=1'''


'''def Maxnum(*number):
    return max(*number)'''
