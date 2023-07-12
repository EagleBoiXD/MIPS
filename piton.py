def instr(line): #line = toata instr
    opcode=rest=""
    line = line.split(' ',1)
    op = line[0]
    rest = line[1]
    
    
    if op == 'addi':
        opcode = '001000'
        print(opcode)
    if op == 'lw':
        opcode = '100011'
        print(opcode)
    if op == 'sw':
        opcode = '101011'
        print(opcode)
    if op == 'xor' or op == 'add' or op == 'sub':
        opcode = '000000'
        print(opcode)
    if op == 'beq':
        opcode = '000100'
        print(opcode)
    if op == 'j':
        opcode = '000010'
        print(opcode)
    
def eticheta():
    print("sunt eticheta")

def main():
    fisier=open('assembly.txt','r')
    lines=fisier.readlines()
    for line in lines:
        x = line.split(' ',1)
        if x[0].find(':') !=-1:  # eticheta
            eticheta() 
        else:  # instructiune adevarata
            instr(line)
            #print("awa awa") 
 
if __name__=="__main__":
    main()
