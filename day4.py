# import random
#
# # a = random.choice(["true","false"])
# # print(a)
#
# a = random.randint(1,2)
# if a == 1:
#     print("true")
# else:
#     print("false")


import random
a = int(input("enter any number press 1 for stone,2 for paper and 3 for sessior:"))
print("=====================================================")
print(f"you chossed:{a}")
print("=====================================================")
if a == 1:
    print('''STONE
                   _______
              ---'   ____)
                    (_____)
                    (_____)
                    (____)
              ---.__(___)''')
elif a == 2:
    print('''PAPER
                  _______
             ---'    ____)____
                        ______)
                       _______)
                      _______)
             ---.__________)
''')
elif a == 3:
    print('''SCISSORS
                  _______
             ---'   ____)____
                       ______)
                    __________)
                   (____)
             ---.__(___)''')

b = random.randint(1,3)
print("=====================================================")
print(f"machine choosed:{b}")
print("=====================================================")
if b == 1:
    print('''STONE
                   _______
              ---'   ____)
                    (_____)
                    (_____)
                    (____)
              ---.__(___)''')
elif b == 2:
    print('''PAPER
                  _______
             ---'    ____)____
                        ______)
                       _______)
                      _______)
             ---.__________)
''')
elif b == 3:
    print('''SCISSORS
                  _______
             ---'   ____)____
                       ______)
                    __________)
                   (____)
             ---.__(___)''')

if a == 1 and b == 2:
    print("you lost")
elif a == 1 and b == 3:
    print("you won")
elif a == 1 and b == 1:
    print("match tied")
elif a == 2 and b == 1:
    print("you won")
elif a == 2 and b == 3:
    print("you lost")
elif a == 2 and b == 2:
    print("match tied")
elif a == 3 and b == 1:
    print("you lost")
elif a == 3 and b == 2:
    print("you won")
elif a == 3 and b == 3:
    print("match tied")
else:
    print("invalid input")

