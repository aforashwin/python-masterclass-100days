alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def cesar(original_text,shift_amount,encode_or_decode):
    cyper_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            cyper_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cyper_text += alphabet[shifted_position]
    print(f"{encode_or_decode}d text: {cyper_text}")
check = True
while check:

    direction = input("type encode for encoding or decode for decoding:")
    text = input(f"enter the text to {direction}: ")
    shift = int(input("enter the number to shift:"))


    cesar(original_text = text,shift_amount = shift,encode_or_decode = direction)

    restart = input("type yes to restart or no to exit:").lower()
    if restart == "no":
        check = False
        print("goodbye")







