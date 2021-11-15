#var = str(input("Enter a character: "))
#dec = ord(var)
#print("In decimal: ", dec)
#uni = "U+" + '0'*(5-len(str(hex(dec)))) + str(hex(dec))
#print('Unicode: ', uni)
#print('UTF-8: ', var.encode('utf-8'))

num = int(input("Enter a number: "))
cha = chr(num)
print("Unicode: U+" + '0'*(5-len(str(hex(num)))) + str(hex(num)))
print("UTF-8: ", cha.encode('utf-8'))
print('Char: ' + cha)

with open('/home/adalrikus/Downloads/386intel.txt', 'rb') as f:
    contents = f.read()

output = open('output.txt', 'w')
output.write(contents.decode('cp437'))
output.close()
f.close()
