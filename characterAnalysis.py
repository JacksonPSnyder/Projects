#Stringsum.py
#Jackson Snyder
#5/4/2022
#Calculates total of type of characters on the test.txt file
def main():
    file1 = open('test.txt', 'r')
    file= file1.readlines()
    cap= 0
    low= 0
    space = 0
    digits = 0
    for lines in file1:
        for ch in lines:
            if ch.isupper():
                cap+=1
            elif ch.islower():
                low+=1
            elif ch.isspace():
                space+=1
            elif ch.isdigit():
                digits +=1
    print('Uppercase letters:',cap,'\n','Lowercase letters:',low,'\n','Digits:',digits,'\n','Spaces:',space)
main()
                
        
       