
message = input('Enter a message to work on: ')
message = message.lower()
key = 2
counter = 0
SYMBOLS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%/.'
translated = ''
mode = input('Encrypt or Decrypt: ') # Set to either 'encrypt' or 'decrypt'.
mode = mode.lower()

while mode[0] is not 'e' and mode[0] is not 'd':
    mode = input('Mode not recognized, please enter either Encrypt or Decrypt: ')
    mode = mode.lower()


for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        if mode[0] is  'e':
            if counter % 2 is not 0:
                translatedIndex = symbolIndex + key + 1
                counter += 1
            else:
                translatedIndex = symbolIndex + key
                counter += 1
        elif mode[0] is 'd':
            if counter % 2 is not 0:
                translatedIndex = symbolIndex - key - 1
                counter += 1
            else:
                translatedIndex = symbolIndex - key
                counter += 1

        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        translated = translated + SYMBOLS[translatedIndex]
    else:
        translated = translated + symbol
        
print(translated)
