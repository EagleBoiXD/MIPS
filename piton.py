import re

def instr(line): #line = toata instr
    x = line.split(' ',1)
    rd = line.split(' ',1)[1].split(', ')
    rs = line.split(', ')
    
    
    if x[0] == 'addi':
        print(x[0])
    print(x)
    print(rd)
    print(rs)
    print(x)
    print("aaaaaaaaa")
    
    

def main():
    fisier=open('assembly.txt','r')
    lines=fisier.readlines()
    for line in lines:
        x = line.split(' ',1)
        if x[0].find(':') !=-1:  # eticheta
            print("blee") 
        else:  # instructiune adevarata
            instr(line)
            print("awa awa") 
 
if __name__=="__main__":
    main()
