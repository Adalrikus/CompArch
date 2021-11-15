#import il
#import sys
#import ctypes

#fb = []
#with open("decryptor.bin", "rb") as f:
#    while (byte := f.read(1)):
#        fb.append(int.from_bytes(byte, byteorder=sys.byteorder))

#asmd = ["INC", "DEC", "MOV", "MOVC", "LSL", "LSR", "JMP", "JZ", "JNZ", "JFE", "RET", "ADD", "SUB", "XOR", "OR", "IN", "OUT"]
#for i in range(len(fb)):
#    if fb[i] >= 1 and fb[i] <= 17:
#        print(fb[i])
#        fb[i] = asmd[fb[i]-1]

#print(fb)
#casm = ""
#for i in range(len(fb)):
#    if type(fb[i]) == type(1):
#        casm += str(fb[i]) + "\n"
#    elif type(fb[i]) == type(fb[i+1]):
#        casm += fb[i] + "\n"
#    else:
#        casm += fb[i] + " "

#casm = '.intel_syntax noprefix\n' + casm
#print(casm)
#xasm = il.def_asm(name="xasm", prototype=ctypes.CFUNCTYPE(ctypes.c_int32), code=casm)
#with open ("q1_encr.txt", 'r') as myfile:
#    data=myfile.readlines()
#    print(data)
#    print(xasm(data))

import re
import sys
import numpy as np

fb = []
with open("decryptor.bin", "rb") as f:
    while (byte := f.read(1)):
        fb.append(int.from_bytes(byte, byteorder=sys.byteorder))

fbline = []
for i in range(0, len(fb), 2):
    fbline.append([fb[i], fb[i+1]])


asmd = ["INC", "DEC", "MOV", "MOVC", "LSL", "LSR", "JMP", "JZ", "JNZ", "JFE", "RET", "ADD", "SUB", "XOR", "OR", "IN", "OUT"]
mnemonics = {}
variables = {}
for i in range(len(fbline)):
    mnemonics[i] = asmd[fbline[i][0]-1]
    temp = format(fbline[i][1], 'x')
    if len(temp) > 1:
        variables[i] = [format(fbline[i][1], 'x')[0], format(fbline[i][1], 'x')[1]]
    else:
        variables[i] = ['0', format(fbline[i][1], 'x')]
    print(mnemonics[i], ' ', variables[i][0], ', ', variables[i][1])


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
    def __init__(self, mnem, vari):
        self.mnem = mnem
        print(mnem)
        print(vari)
        self.vari = vari
        self.encr = open("q1_encr.txt", 'r').read()
        self.regs = np.zeros(16, dtype=np.uint64)
        self.flag = False
        self.fEnd = False
        self.indx = 0
        while not self.flag:
            getattr(self, self.mnem[self.indx])()
            self.indx += 1
            #print(self.regs)
            #for ele in self.regs:
            #    with open("logs.txt", 'w') as log:
            #        log.write(chr(ele))


    def ADD(self):
        x = int(self.vari[self.indx][1])
        y = int(self.vari[self.indx][0])

        self.regs[x] = self.regs[x] + self.regs[y]
        #print(self.regs)


    def SUB(self):
        x = int(self.vari[self.indx][1])
        y = int(self.vari[self.indx][0])

        self.regs[x] = self.regs[x] - self.regs[y]
        #print(self.regs)


    def XOR(self):
        x = int(self.vari[self.indx][1])
        y = int(self.vari[self.indx][0])

        self.regs[x] = self.regs[x] ^ self.regs[y]
        #print(self.regs)


    def OR(self):
        x = int(self.vari[self.indx][1])
        y = int(self.vari[self.indx][0])

        self.regs[x] = self.regs[x] | self.regs[y]
        #print(self.regs)


    def IN(self):
        x = int(self.vari[self.indx][1])
        if len(self.encr) == 0:
            self.fEnd = True
        else:
            self.regs[x] = ord(self.encr[0])
            self.encr = self.encr[1:]
        #print(self.regs)


    def OUT(self):
        x = int(self.vari[self.indx][1])
        decr = open("decrypted.txt", 'a')
        decr.write(chr(self.regs[x]))
        #print(chr(self.regs[x]))
        #print(self.regs)


    def INC(self):
        regInd = int(self.vari[self.indx][1])
        self.regs[regInd] += 1
        #print(self.regs)


    def DEC(self):
        regInd = int(self.vari[self.indx][1])
        self.regs[regInd] -= 1
        #print(self.regs)


    def MOV(self):
        regInd = int(self.vari[self.indx][1])
        regNum = int(self.vari[self.indx][0])
        self.regs[regInd] = regNum
        #print(self.regs)


    def MOVC(self):
        regNum = int(str(self.vari[self.indx][0] + self.vari[self.indx][1]), 16)
        self.regs[0] = regNum
        #print(self.regs)


    def LSL(self):
        regInd = int(self.vari[self.indx][1])
        self.regs[regInd] = int(self.regs[regInd]) << 1
        #print(self.regs)


    def LSR(self):
        regInd = int(self.vari[self.indx][1])
        self.regs[regInd] = int(self.regs[regInd]) >> 1
        #print(self.regs)


    def JMP(self):
        self.indx = -1
        #print(self.indx)


    def JZ(self):
        if(self.flag):
            self.indx = self.indx + int(str(self.vari[self.indx][0] + self.vari[self.indx][1]), 16)/2 - 1
        #print(self.indx)


    def JNZ(self):
        if not self.flag:
            self.indx = self.indx + int(str(self.vari[self.indx][0] + self.vari[self.indx][1]), 16)/2 - 1
        #print(self.indx)


    def JFE(self):
        if self.fEnd:
            self.indx = self.indx + int(str(self.vari[self.indx][0] + self.vari[self.indx][1]), 16)/2 - 1
        #print(self.indx)


    def RET(self):
        self.flag = True
        #print(self.flag)



ASM(mnemonics, variables)
