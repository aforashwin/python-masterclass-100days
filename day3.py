# a = int(input("enter a number:"))
# if a%2==0:
#     print("even number")
# else:
#     print("odd number")

# print(10 % 3)
# enter_pizza = input("enter the size of the the pizza?")
# pepper = input("do you need pepper?")
# cheese = input("do you need extra cheese?")
# che = 5
# if enter_pizza == "S":
#     bill=15
#     pep = 2
#     if pepper == "yes" and cheese == "yes":
#         bill = bill + pep + che
#     elif pepper == "no" and cheese == "yes":
#         bill = bill + che
#     elif pepper == "yes" and cheese == "no":
#         bill += pep
#     print("total bill: ", bill)
# elif enter_pizza == "M":
#     bill = 25
#     pep = 3
#     if pepper == "yes" and cheese == "yes":
#         bill = bill + pep + che
#     elif pepper == "no" and cheese == "yes":
#         bill = bill + che
#     elif pepper == "yes" and cheese == "no":
#         bill += pep
#     print("total bill: ", bill)
# elif enter_pizza == "L":
#     bill = 30
#     pep = 3
#     if pepper == "yes" and cheese == "yes":
#         bill = bill + pep + che
#     elif pepper == "no" and cheese == "yes":
#         bill = bill + che
#     elif pepper == "yes" and cheese == "no":
#         bill += pep
#     print("total bill: ", bill)


print("welcome to this game you need to find the treasure")
a = input("enter right or left?")
if a == "right":
    print("game over")
else:
    b = input("enter swim or wait?")
    if b == "swim":
        print("game over")
    else:
        door =input("enter black or red or yellow?")
        if door == "red" or door == "black":
            print("game over")
        else:
            print("you won")
