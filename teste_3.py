def string_encode(string: str) -> str:

    string = string + ' '

    previous_letter = None
    current_letter = None
    sum_letters = 1

    response = ''

    count = 0
    while count < len(string):
        
        if count > 0 and count < len(string):

            current_letter = string[count]
            previous_letter = string[count - 1]

            if current_letter == previous_letter:

                sum_letters += 1

                if sum_letters == 9:
                    current_encoded_letter = str(sum_letters) + previous_letter
                    response += current_encoded_letter
                    sum_letters = 0
            else:
                current_encoded_letter = str(sum_letters) + previous_letter
                response += current_encoded_letter
                sum_letters = 1

        count += 1
        
    return response

result = string_encode(string = "BBBBBBBBBBBBBAACCCDD")
print(result)
