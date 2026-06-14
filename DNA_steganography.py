# DNA Steganography: hide and recover text inside DNA-like sequences

code = {
    "00": "A",
    "01": "C",
    "10": "G",
    "11": "T"
}

decode_code = {v: k for k, v in code.items()}


def text_to_dna(message):
    dna = ""

    for char in message:
        binary = format(ord(char), "08b") #alphabet to ASCII to 8-bit binary

        for i in range(0, 8, 2):
            pair = binary[i:i+2]
            dna += code[pair]

    return dna


def dna_to_text(dna):
    binary = ""

    for base in dna:
        binary += decode_code[base]

    message = ""

    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        message += chr(int(byte, 2))

    return message


message = input("Enter message to hide: ")

encoded_dna = text_to_dna(message)
decoded_message = dna_to_text(encoded_dna)

print("\nEncoded DNA sequence:")
print(encoded_dna)

print("\nDecoded message:")
print(decoded_message)