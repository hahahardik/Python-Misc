import string

def caesar_shift_cipher(sentence, action='d', shift=3):
    
    '''This is a caeser shift decoder, which decodes one sentence at a time.
    
    For the shift value, if shift = 3 (shift value used by Caesar himself),
    then A becomes D, B becomes E, W becomes Z and Z becomes C and so on.
    
    This can also alternatively used as a ENCODER by changing the action to 'e'.
    'e' here means encode and 'd' means decode.
    '''
    
    upper_l = []    # To store uppercase alphabets
    lower_l = []    # To store lowercase alphabets
    message = ''    # Empty string to store the messeage depending on the action(using concatenation)
    
    # The commands below extract every letter from the standard ASCII alphabets and store them in their resp. lists
    for i in string.ascii_uppercase:
        upper_l.append(i)
    
    for j in string.ascii_lowercase:
        lower_l.append(j)
    
    # Checks for every letter in the sentence
    for letter in sentence:

        # Adds 'SPACE' for 'SPACE'
        if letter == ' ':
            message += ' '

        # Adds 'PERIOD' for 'PERIOD' and stops 
        elif letter == '.':
            message += '.'
            break

        # Replaces the letter with the corresponding decoders considering their case
        else:

            # For Decoding
            if action == 'd':

                if letter in lower_l:
                    message += lower_l[lower_l.index(letter) - shift]
                else:
                    message += upper_l[upper_l.index(letter) - shift]

            # For Encoding
            else:

                if letter in lower_l:
                    message += lower_l[(lower_l.index(letter) + shift) % 26]
                else:
                    message += upper_l[(upper_l.index(letter) + shift) % 26]


    return message
