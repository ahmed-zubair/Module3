def welcome():
    '''Prints out the welcome message for the user right in the beginning of
    the program.'''
    print '\n\n\n', '*' * 62, '\n', '*' * 10, 'Welcome to the MAKE-BELIEVE Banking System', '*' * 10, '\n', '*' * 62
    print '\n\nPlease select the function you want to perfrom (1 ~ 3)\n\n\t1. ' \
          'Login for user services. \n\t2. Create New account. \n\t3. Exit!\n\n'


class Account(object):

    #Account_Info = {'Title':'Manager','Acc_No':'0000','acc_type':'current','balance':1000000}
    global Account_holders
    Account_holders = []

    def __init__(self):
        self.acc_title = None
        self.acc_no = None
        self.acc_type = None
        self.balance = None

    def get_balance(self,title):
        '''Gets the current account balance of a particular account'''
        return 'ALERT: Your Current Balance is: ', self.balance

    def deposit(self, amount):
        self.balance = amount + self.balance
        return 'ALERT: Your balance after a deposit of ', amount, ' is: ' \
                                                           '', self.balance

    def withdraw(self,amount):
        if self.balance == 0:
            return 'ALERT: Your account is empty...'
        else:
            self.balance = self.balance - amount
            return 'ALERT: Your balance after a withdrawl of'. amount, 'is: ' \
                                                                '',self.balance

    def transfer(self,amount,to_acc_no):
        '''Transfers funds from the logged in account to the account no.
        provided in the parameters'''
        if self.balance == 0:
            return 'ALERT: Sorry! you don\'t have enough money in your account ' \
                   'to make the transaction!'
        elif((self.balance - amount) <= 0):
            return 'ALERT: You are trying to make an invalid transfer! ' \
                   'Maximum transcation of ',self.balance,' could be made!'
        else:
            self.balance = self.balance - amount
            to_acc_no.balance = to_acc_no.balance + amount
            return self.balance

        def search_title(title2):
            i = 0
            while i < len(Account_holders):
                if title2 == Account_holders[i].acc_title:
                    return Account_holders[i]
                    break
                else:
                    i += i
            return 'No such account exists!'



        def compare(self):
            balance1 = int(self.bank_balance)
            print "Enter the title of Second Account to be compared"
            account2 = raw_input()
        # Call the search_by_name method to find the CUSTOMER in database
            account2 = search_title(account2)
            balance2 = int(account2.balance)
        # Comparing Balances
            if balance1 > balance2:
                print self.acc_title, "\'s account is greater than", account2.acc_title,'\'s'
            elif balance2 > balance1:
                print account2.acc_title, "\'s account is greater than", self.acc_title,'\'s'
            else:
                print self.acc_title, "and", account2.acc_title, " have equal account balances. "


    def add_acc_holder(self):
        '''Adds a new account holder to the database'''
        self.acc_title(raw_input('Enter new account holder\'s Name: '))
        self.acc_no(raw_input('Enter new account holder\'s account number: '))
        self.acc_type(raw_input('Enter new account holder\'s account type (current/savings): '))
        self.balance(raw_input('Enter the amount you want to deposit initially: '))
        return 'New account holder added to the database!'