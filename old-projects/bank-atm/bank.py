balance = 200
action = ''

def visit_bank():
    global action
    global balance
    while action.upper() != 'Q':
        action = input('''Please select from the following menu options:
        (B)alance
        (D)eposit
        (W)ithdraw
        (Q)uit
        ''')

        if action.upper() == 'B':
            check_balance()
        elif action.upper() == 'D':
            deposit()
        elif action.upper() == 'W':
            withdraw()
        elif action.upper() == 'Q':
            print('Goodbye. Please come again.')

def check_balance():
    print(f'Your current balance is ${balance:.2f}')

def deposit():
    deposit = ''
    while not isinstance(deposit,float):
        try:
            deposit = float(input('How much would you like to deposit? '))
        except ValueError:
            print('You gotta gimme a number! ')
    global balance
    balance += deposit
    print(f'You have deposited ${deposit:.2f} and your balance is ${balance:.2f}')

def withdraw():
    withdrawal = ''
    while not isinstance(withdrawal,float):
        try:
            withdrawal = float(input('How much would you like to withdraw? '))
        except ValueError:
            print('You gotta gimme a number! ')
    global balance
    if withdrawal <= balance:
        balance -= withdrawal
        print(f'You have withdrawn ${withdrawal:.2f} and your balance is ${balance:.2f}')
    else:
        print('Insufficient funds.')

visit_bank()