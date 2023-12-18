print("--------------------------Random passoword genrator----------------------")

# thinking about first the password is made of " char,symbol,number and special symbol"""


# user_input:

import random

char_len = int(input(  "How many charchater do yo want        :"))
number_len = int(input("How many number do you want           :"))
symbol_len = int(input("How many symbol do you want           :"))


char=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
      'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


number=[1,2,3,4,5,6,7,8,9,10]

symbol=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',
        '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']



#take a empty list for storing a number, symbol, char
password_list=[]


#geting a char_len
for i in range(0,(char_len)):
    password_list.append(random.choice(char))


#getting a number
for i in range(0,(number_len)):
    password_list.append(random.choice(number))
    
#getting a symbol
for i in range(0,(symbol_len)):
    password_list.append(random.choice(symbol))
    
print(f"Your password for intagram/twiter/snapchat/whatsapp:{password_list}")


#every time we need different passcode for different account :

random.shuffle(password_list)

#But our passcode formate is  list we need to convert it into a string becoz password look like-->"weclome002@""

password=''

#convert a list into string:
for i in password_list:
    password=password+str(i)
    
print(f"Your passcode :{password}")