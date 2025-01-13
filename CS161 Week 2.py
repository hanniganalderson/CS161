#Week 2 Assignment CS161

x = 31
#x = 1.825
#float cannot be interpreted as an integer
x = 18
#Print value, binary value, hex value
print (x, bin(x), hex(x))

#Customized for different output
y = 0b101
z = 0xC9
print(z, y)
w = x + y + z
print('The sum is', w)

#Compression variables
original_size = 90
dictionary_size = 40
compressed_text_size = 15

#Caculating total compressed size and compression percent
total_compressed_size = compressed_text_size + dictionary_size
compression_percent = (1 - ((compressed_text_size + dictionary_size) / original_size)) * 100 #*100 to make percentage accurate

#Printing values
print(' 	Original size:', str(original_size), 'characters')
print(' 	Dictionary size:', str(dictionary_size), 'characters')
print(' 	Compressed text size:', str(compressed_text_size), 'characters')
print(' 	Total:', str(total_compressed_size), 'characters')
#f string with .2f to allow 2 decimal points
print(' 	Compression percent:', f"{compression_percent:.2f}%", '')

#Extra credit
# Input from user between -127 and 127
decimal = int(input("Enter a number between -127 and 127: "))

#If input is valid
if -127 <= decimal <= 127:
    #If input is positive
    if decimal >= 0:
        #Slices removing the 0b
        binary = bin(decimal)[2:]
        #Add zero(s) to get the binary to length of 8
        while len(binary) < 8:
            binary = "0" + binary
    else:
        #Add 256 to negative decimal
        positive = 256 + decimal
        #Change decimal to binary and remove 0b
        binary = bin(positive)[2:]
    twos_complement = bin(decimal & 0xFF) [2:].zfill(8)
    #Print two's complement
    print(f"The two's complement is: {binary}")
else:
    #Invalid input, give error
    print ("Error, invalid input")