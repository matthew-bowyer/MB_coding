# Writing a programme to code a message and return the result
# Text will be encoded
# Punctuation to remain as per the original message

def encodedmessage(message: str) -> str:
    
    encoded = []
    shift = 15
    
    # Using a for loop to loop through the letters in the message
    for char in message:
        
        # Process lowercase letters
        if 'a' <= char <= 'z':
            # Shift within 0–25 range
            offset = ord(char) - ord('a')
            new_char = chr((offset + shift) % 26 + ord('a'))
            encoded.append(new_char)
        
        # Process uppercase letters
        elif 'A' <= char <= 'Z':
            offset = ord(char) - ord('A')
            new_char = chr((offset + shift) % 26 + ord('A'))
            encoded.append(new_char)

        # Checking for digits in message and leave unchanged
        elif '0' <= char <= '9':
            encoded.append(char)

        # Leave punctuation or other symbols unchanged
        else:
            encoded.append(char)
    
    return "".join(encoded)


# Print the encoded message
print(encodedmessage("Encode: Pl3aSe, eNCode. ME!"))
