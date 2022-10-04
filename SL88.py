import random as r


def instructions():
    print('Welcome to Python Slots!\nYour starting balance is $500\nYou can bet any amount up to your current balance.\nThe program will end when you reach zero balance, or if you enter a negative bet amount')
STARTING_BALANCE = 500


def choose_shapes():
    num1= r.randint(0,2)
    num2 =r.randint(0,2)
    num3=r.randint(0,2)
    if num1 == 1:
        shape1 = 'XXX'
    if num1 == 2:
        shape1 = ' X '
    if num1 == 0:
        shape1 = 'X X'
    if num2 == 1:
        shape2 = 'XXX'
    if num2 == 2:
        shape2 = ' X '
    if num2 == 0:
        shape2 = 'X X'
    if num3 == 1:
        shape3 = 'XXX'
    if num3 == 2:
        shape3 = ' X '
    if num3 == 0:
        shape3 = 'X X'
    LIST1 =[shape1,shape2,shape3]
    slot1 = r.choice(LIST1)
    slot2 = r.choice(LIST1)
    slot3 = r.choice(LIST1)
    slot7 = r.choice(LIST1)
    slot8 = r.choice(LIST1)
    slot9 = r.choice(LIST1)
    print('',slot1,slot2,slot3,'\n',shape1,shape2,shape3,'\n',slot7,slot8,slot9,sep='  ')
    return shape1,shape2,shape3
           
        
    
def calculate_winnings(Bet,shape1,shape2,shape3):
    Bet = float(Bet)
    if shape1 == 'XXX' and shape2 == 'XXX' and shape3 == 'XXX':
        WINNINGS = Bet + Bet
        print('JACKPOT')
    if shape1 == ' X ' and shape2 == ' X ' and shape3 == ' X ':
        WINNINGS = Bet + Bet
        print('JACKPOT')  
    if shape1 == 'X X' and shape2 == 'X X' and shape3 == 'X X':
        WINNINGS = Bet + Bet
        print('JACKPOT')          
    if (shape1 == 'XXX' and shape2 == 'XXX') or (shape1 == "XXX" and shape3 == 'XXX') or (shape2 == 'XXX' and shape3=='XXX'):
        INCOME = Bet/2
        INCOME = float(INCOME)
        WINNINGS = Bet + INCOME
    if (shape1 == ' X ' and shape2 ==' X ') or (shape1 == ' X ' and shape3 == ' X ') or (shape2 == ' X ' and shape3 == ' X '):
        INCOME = Bet/2
        INCOME = float(INCOME)
        WINNINGS = Bet + INCOME
    if (shape1 == 'X X' and shape2 == 'X X') or (shape1 == 'X X' and shape3 == 'X X') or (shape2 == 'X X' and shape3 == 'X X'):
        INCOME = Bet/2
        INCOME = float(INCOME)
        WINNINGS = Bet + INCOME
    if shape1 != shape2 and shape1 != shape3 and shape2 != shape3:
        WINNINGS = 0
    return WINNINGS    

def main():
    instructions()
    BALANCE = STARTING_BALANCE
    while BALANCE > 0:
        print('Your current balance is $',BALANCE,sep='')
        BET = float(input('ENTER your bet: $'))
        if BET > BALANCE:
            print('INSUFFICIENT FUNDS')
            print('GAME OVER!')
            main()
        if BET <= 0:
            print('GAME OVER')
            exit()
        BALANCE = BALANCE - BET
        shape1,shape2,shape3 = choose_shapes()
        Winnings=calculate_winnings(BET,shape1,shape2,shape3)
        Winnings = Winnings
        BALANCE = BALANCE + Winnings
        BALANCE = round(BALANCE, 2)
    print('GAME OVER')
main()
       