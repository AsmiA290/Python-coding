#Encoder
def messageEncoder(sent, shift):
    ''' we take an input ex. meet me in the living room and the user wants to move the entire sentace by 2'''
    ''
    letters = [ord(a) for a in sent]
    shifted_list = [chr(a+shift) for a in letters]
    encoded = ''.join(shifted_list)
    return encoded


def main():
    message = "This is a test."
    shift = 5
    encoded = messageEncoder(message, shift)
    print(encoded)
    decode=messageDecoder(encoded, shift)
    print (decode)

    
# Decoder
def messageDecoder(mix, value):
    letters = [ord(a) for a in mix]
    shifted_list = [chr(a-value) for a in letters]
    encoded = ''.join(shifted_list)
    return encoded
if __name__ == "__main__":
    main()
