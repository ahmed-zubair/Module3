import banking


while 1:
    banking.welcome()
    start_fn = int(raw_input('Enter your choice >> '))

    if start_fn==1:
        title1 = raw_input('Enter account title for existing account: ')


    elif start_fn==2:
        new1 = banking.Account.add_acc_holder()
        banking.Account.Account_holders.append(new1)

    elif start_fn==3:
        print 'If you are sure to exit (Y/N)?'
        if raw_input()=='Y':
            exit(0)
        else:
            banking.welcome()
    else:
        print 'INVALID CHOICE!'

    print 'Enter your account number and password to see the available services:'
    print 'Welcome user. \nAccount number '
