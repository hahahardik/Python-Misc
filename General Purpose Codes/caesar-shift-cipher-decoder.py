import string

def caesar_shift_cipher(sentence, shift=3):
    
    '''This is a caeser shift decoder, which decodes one sentence at a time.
    For the shift value, if shift = 3 (shift value used by Caesar himself),
    then A becomes D, B becomes E, W becomes Z and Z becomes C and so on,
    '''
    
    upper_l = []    # To store uppercase alphabets
    lower_l = []    # To store lowercase alphabets
    decoded = ''    # Empty string to store the decoded messeage (using concatenation)
    
    # The commands below extract every letter from the standard ASCII alphabets and store them in their resp. lists
    for i in string.ascii_uppercase:
        upper_l.append(i)
    
    for j in string.ascii_lowercase:
        lower_l.append(j)
    
    # Checks for every letter in the sentence
    for letter in sentence:

        # Adds 'SPACE' for 'SPACE'
        if letter == ' ':
            decoded += ' '

        # Adds 'PERIOD' for 'PERIOD' and stops 
        elif letter == '.':
            decoded += '.'
            break

        # Replaces the letter with the corresponding decoders considering their case
        else:

            if letter in lower_l:
                decoded += lower_l[lower_l.index(letter) - shift]
            else:
                decoded += upper_l[upper_l.index(letter) - shift]


    return decoded