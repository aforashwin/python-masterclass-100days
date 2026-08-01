# a = [30,10,20]
# sum = 0
# for i in a:
#     if i > sum:
#         sum = i
# print(sum)
#
# j = 0
# for i in range(1,101):
#     j +=i
# print(j)
from random import shuffle
from traceback import print_list

# for i in range(1,10):
#     if i % 2 == 0:
#         print("divisible by 2")
#     elif i % 3 == 0:
#         print("divisible by 3")
#     else:
#         print(i)



letters = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

# Numbers
numbers = [
    '0','1','2','3','4','5','6','7','8','9'
]

# Symbols
symbols = [
    '!','@','#','$','%','^','&','*','(',')',
    '-','_','=','+',
    '[',']','{','}',
    '\\','|',
    ';',':',
    "'",'"',
    ',','.','<','>','/','?'
]
import random
a  = int(input("enter a total alphabet to be entered in the password:"))
b = int(input("enter a total number to be entered in the password:"))
c = int(input("enter a total symbol to be entered in the password:"))
password_list = []
for i in range(a):
    password_list.append(random.choice(letters))
for j in range(b):
    password_list.append(random.choice(symbols))
for k in range(c):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char # password = password + char
print(password)





