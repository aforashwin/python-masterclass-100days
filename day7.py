import random

lives = 6
stages = [
# 0 lives
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",

# 1 life
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",

# 2 lives
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",

# 3 lives
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",

# 4 lives
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",

# 5 lives
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",

# 6 lives
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]

random_list = ["ashwin","balaji","baraa"]
choosen_word  = random.choice(random_list)
print("chossen_word:",choosen_word)


a = len(choosen_word)
place_holder = ""
for i in range(a):
    place_holder += "_"
print(place_holder)

game_over = False
correct_letter = []

while not game_over:
    guess = input("Enter your guess: ").lower()
    display = ""

    if guess in correct_letter:
        print("you guessed correctly")

    if guess not in choosen_word:
        print(f"you guessed incorrectly {guess}")

    for letter in choosen_word:
        if guess == letter:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in correct_letter:
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"the correct answer is {choosen_word}: You Lose!")
    # optional
    # if "_" not in display:
    #     game_over = True
    #     print("You win!")

    print(stages[lives])
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # i=0
# # while i < a:
# #     if guess == choosen_word[i]:
# #             i = i + 1
# #             print("right")
# #     elif guess != choosen_word[i]:
# #             i = i + 1
# #             print("Wrong")

































# import random
#
# # lives = 6
# # stages = [
# # # 0 lives
# # """
# #   +---+
# #   |   |
# #       |
# #       |
# #       |
# #       |
# # =========
# # """,
# #
# # # 1 life
# # """
# #   +---+
# #   |   |
# #   O   |
# #       |
# #       |
# #       |
# # =========
# # """,
# #
# # # 2 lives
# # """
# #   +---+
# #   |   |
# #   O   |
# #   |   |
# #       |
# #       |
# # =========
# # """,
# #
# # # 3 lives
# # """
# #   +---+
# #   |   |
# #   O   |
# #  /|   |
# #       |
# #       |
# # =========
# # """,
# #
# # # 4 lives
# # """
# #   +---+
# #   |   |
# #   O   |
# #  /|\\  |
# #       |
# #       |
# # =========
# # """,
# #
# # # 5 lives
# # """
# #   +---+
# #   |   |
# #   O   |
# #  /|\\  |
# #  /    |
# #       |
# # =========
# # """,
# #
# # # 6 lives
# # """
# #   +---+
# #   |   |
# #   O   |
# #  /|\\  |
# #  / \\  |
# #       |
# # =========
# # """
# # ]
#
# random_list = ["ashwin","balaji","baraa"]
# choosen_word  = random.choice(random_list)
# print("chossen_word:",choosen_word)
#
#
# a = len(choosen_word)
# place_holder = ""
# for i in range(a):
#     place_holder += "_"
# print(place_holder)
#
# game_over = False
# correct_letter = []
#
# while not game_over:
#     guess = input("Enter your guess: ").lower()
#     display = ""
#     for letter in choosen_word:
#         if guess == letter:
#             display += letter
#             correct_letter.append(letter)
#         elif letter in correct_letter:
#             display += letter
#         else:
#             display += "_"
#     print(display)
#
#     # if guess not in correct_letter:
#     #     lives -= 1
#     #     if lives == 0:
#     #         game_over = True
#     #         print("You Lose!")
#
#     if "_" not in display:
#         game_over = True
#         print("You win!")
#
#     # print(stages[lives])
















# i=0
# while i < a:
#     if guess == choosen_word[i]:
#             i = i + 1
#             print("right")
#     elif guess != choosen_word[i]:
#             i = i + 1
#             print("Wrong")
