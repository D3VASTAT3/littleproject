def convert_to_position(input_sentence, reference_array):
    output_sentence = ""
    
    for char in input_sentence:
        if char.isalpha():
            char = char.lower()  # Convert char to lowercase
            if char in reference_array:
                char_position = reference_array.index(char) + 1
                if char_position > 9:
                    char_position %= 26  # Handle wrap around from 'z' to 'a'
                    if char_position == 0:
                        char_position = 26
                    output_sentence += chr(char_position + 64 - 9)  # Convert to uppercase alphabet
                else:
                    output_sentence += str(char_position)
            else:
                output_sentence += char
        else:
            output_sentence += char
    
    return output_sentence

# Reference array representing a sentence-like sequence of characters
reference_array = ['t', 'h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'o', 'x', 'j', 'u', 'm', 'p', 's', 'o', 'v', 'e', 'r', 't', 'h', 'e', 'l', 'a', 'z', 'y', 'd', 'o', 'g']

# User input
user_input = input("Enter a sentence: ")

# Convert input to position
output = convert_to_position(user_input, reference_array)

print("Converted sentence:", output)
