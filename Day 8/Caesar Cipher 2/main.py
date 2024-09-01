alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
def caesar(direction, original_text, shift_amount):
    output_text = ""
    if direction == "decode":
        for c in original_text:
            if c in alphabet:
                index = (alphabet.index(c) - shift_amount) % 26
                print(index)
                output_text += alphabet[index]
            else:
                output_text += c
        print(f"Here is the encoded result: {output_text}")

    else:
        for letter in original_text:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {output_text}")
caesar(direction, text, shift)



