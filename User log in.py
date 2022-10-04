print('Welcome to the user interface.')
file1 = open('Text.txt', 'r+')
obj = file1.read()
def login():
    user_name = input('What is your Username:')
    password = input('What is your password:')
    FINAL = (user_name + ' ' + password)
    if FINAL in obj:
        print('Welcome back ', user_name, ', we really missed you!',sep='')
    if FINAL not in obj:
        print("We couldn't find you")
        login()
def new_user():
    print('What username would you like?')
    new_username = input()
    if new_username in obj:
        print('That name has already been taken, please choose another.')
        new_user()
    print('What password would you like?')
    new_pass = input()
    new_pass2 = input('Enter password again.\n')
    if new_pass != new_pass2:
        print('The two passwords do not match')
        new_user()
    file1.write(new_username)
    file1.write(' ')
    file1.write(new_pass)
    file1.write('\n')
    print('Welcome to the fam', new_username,sep=' ')
def change_pass():
    NAME= input('What is your username:')
    if NAME in obj:
        print('Hello',NAME, 'what was your previous password?')
        old=input()
        XD = NAME+' '+old
        if XD in obj:
            new=input('What would you like your new password to be?\n')
            NEWXD = NAME+' '+new
            z=obj
            z=z.replace(XD, NEWXD)
            file1.seek(0)
            file1.truncate(0)
            file1.write(z)
            print('No worries', NAME,'your password was changed!')
        if old not in obj:
            print("I couldn't find that password in the database")
            change_pass()
    if NAME not in obj:
        print("We couldn't find you, please make an account")
        new_user()
         

def main():
    you = input('Is this your first time here? (Enter yes or no)\n')
    if you.lower() == 'yes':
        new_user()
    elif you.lower() == 'no':
        Q=input('Would you like to sign in, or change your password?\n(Enter s to sign in or p to change password)\n')
        if Q.lower() == 's':
            login()
        if Q.lower() == 'p':
            change_pass()
        else:
            print('Invalid input')
            main()
main()   
file1.close()

        
