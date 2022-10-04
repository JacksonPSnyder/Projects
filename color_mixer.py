#February_Days.py
#Jackson Snyder
#02.07.2021
#This program mixes color based on the mixing technique, additive or subtractive
method = input('Is the color your mixing additive or subtractive? \n (Enter A or S):')          #set the method variable to the input of the user, ensuring that method will be A or S
method = method.upper()
if method == 'A':
    first_color = input('Enter the first color (red, blue, green)\n')                           #set the first_color variable to the input of the user
    second_color = input('Enter the second color (red, blue, green)\n')                         #set the second_color variable to the input of the user
elif method.upper() == 'S':
    first_color = input('Enter the first color (yellow, magenta, cyan)\n')                      #set the first_color variable to the input of the user
    second_color = input('Enter the second color (yellow, magenta, cyan)\n')                    #set the second_color variable to the input of the user
else:
    print('Invalid input')                                                                      #If the user does not meet the inputs requirements, end the program
    quit()
first_color = first_color.lower()
second_color = second_color.lower()
if first_color == 'red' and second_color == 'red':                                              #lines 14-33 are if statements that produce an output that reflects the colors that they have blended i.e red, blue makes magenta
    mixed_color = 'red'
elif first_color == 'red' and second_color == 'blue':
    mixed_color ='magenta'
elif first_color == 'red' and second_color == 'green':
    mixed_color = 'yellow'
    
elif first_color == 'blue' and second_color == 'blue':
    mixed_color = 'blue'
elif first_color == 'blue' and second_color == 'red':
    mixed_color = 'magenta'
elif first_color == 'blue' and second_color == 'green':
    mixed_color = 'cyan'
    
elif first_color == 'green' and second_color == 'green':
    mixed_color = 'green'
elif first_color == 'green' and second_color == 'red':
    mixed_color = 'yellow'
elif first_color == 'green' and second_color == 'blue':
    mixed_color = 'cyan'
    
elif first_color == 'yellow' and second_color == 'yellow':                                      #lines 35-54 are if statements that produce an output that reflects the colors that they have blended i.e yellow, magenta makes red
    mixed_color = 'yellow'
elif first_color == 'yellow' and second_color == 'magenta':
    mixed_color = 'red'
elif first_color == ' yellow' and second_color == 'cyan':
    mixed_color = 'green'
    
elif first_color == 'magenta' and second_color == 'magenta':
    mixed_color = 'magenta' 
elif first_color == 'magenta' and second_color == 'yellow':
    mixed_color = 'red' 
elif first_color == 'magenta' and second_color == 'cyan':
    mixed_color = 'blue'
    
elif first_color == 'cyan' and second_color == 'cyan':
    mixed_color = 'cyan'
elif first_color == 'cyan' and second_color == 'yellow':
    mixed_color = 'green'
elif first_color == 'cyan' and second_color == 'magenta':
    mixed_color == 'blue'
else:
    print('You chose the wrong color!')
    quit()
print('Result of color mixing:',mixed_color)                                                    #print the result of the color mixing
    
    
