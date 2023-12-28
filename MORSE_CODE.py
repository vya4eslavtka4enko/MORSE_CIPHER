
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def start_function():
    message = input('Please enter your message  ')
    return message

# First case

def encrypt(message):
    encrypted_message = [] 
    message = [item.upper() for item in message if item != " "]
    list_message = list(message)
    for key,value in MORSE_CODE_DICT.items():
        for item  in list_message:
            if key == item:
                encrypted_message.append(value)
    print(' '.join(encrypted_message))
    return encrypted_message
# Second case

def decrypted(message):
    # n = {k:MORSE_CODE_DICT[k] for k in message if k in MORSE_CODE_DICT}
    # print(n)
    dec_message = []
    for item in message:
        for key,value in MORSE_CODE_DICT.items():
            if item == value:
                dec_message.append(key)
    print(' '.join(dec_message))



# encrypt(start_function())
decrypted(encrypt(start_function()))