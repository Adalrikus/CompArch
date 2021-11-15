import re
import sys

fb = []
with open("decryptor.bin", "rb") as f:
    while (byte := f.read(1)):
        fb.append(int.from_bytes(byte, byteorder=sys.byteorder))

asmd = ["INC", "DEC", "MOV", "MOVC", "LSL", "LSR", "JMP", "JZ", "JNZ", "JFE", "RET", "ADD", "SUB", "XOR", "OR", "IN", "OUT"]
for i in range(len(fb)):
    if fb[i] >= 1 and fb[i] <= 17:
        print(fb[i])
        fb[i] = asmd[fb[i]-1]


print(fb)

#casm_file = open("decrypted.txt", 'w')
#casm = ""
#for i in range(len(fb)):
#    if type(fb[i]) == type(1):
#        casm += str(fb[i]) + '\n'
#    elif type(fb[i]) == type(fb[i+1]):
#        casm += fb[i] + "\n"
#    else:
#        casm += fb[i] + " "

class ASM:
    def __init__(code):
        self.code = code
        self.regs = range(0, 16)
        self.flag = False
        self.fEnd = False
        self.indx = 0
        while not (self.flag and self.fEnd):
            if type(self.code[self.indx]) == type(1):
                self.regs.append(self.code[self.indx])
            elif type(self.code[self.indx]) == type(self.code[self.indx+1]):
                getattr(self, self.code[self.indx])
            self.indx += 1

    def ADD(self):
        self.code[self.indx+1] =


    def INC(self):


    def DEC(self):

        
    def MOV(self):


    def MOVC(self):


    def LSL(self):


    def LSR(self):


    def JMP(self):


    def JZ(self):


    def JNZ(self):


    def JFE(self):


    def RET(self):


    def SUB(self):


    def XOR(self):


    def OR(self):


    def IN(self):

    
    def OUT(self):
