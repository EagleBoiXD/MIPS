opcodes = {
    "add": "000000", "sub": "000000", "and": "000000", "or": "000000", "xor": "000000",
    "addi": "001000", "beq": "000100", "j": "000010", "lw": "100011", "sw": "101011"
}
fn = {
    "add": "100000", "sub": "100010", "and": "100100", "or": "100101", "xor": "100110"
}

regs = {
    "00000": ["$0", "$zero"], "00001": ["$1", "$at"], "00010": ["$2", "$v0"], "00011": ["$3", "$v1"],
    "00100": ["$4", "$a0"], "00101": ["$5", "$a1"], "00110": ["$6", "$a2"], "00111": ["$7", "$a3"],
    "01000": ["$8", "$t0"], "01001": ["$9", "$t1"], "01010": ["$10", "$t2"], "01011": ["$11", "$t3"],
    "01100": ["$12", "$t4"], "01101": ["$13", "$t5"], "01110": ["$14", "$t6"], "01111": ["$15", "$t7"],
    "10000": ["$16", "$s0"], "10001": ["$17", "$s1"], "10010": ["$18", "$s2"], "10011": ["$19", "$s3"],
    "10100": ["$20", "$s4"], "10101": ["$21", "$s5"], "10110": ["$22", "$s6"], "10111": ["$23", "$s7"],
    "11000": ["$24", "$t8"], "11001": ["$25", "$t9"], "11010": ["$26", "$k0"], "11011": ["$27", "$k1"],
    "11100": ["$28", "$gp"], "11101": ["$29", "$sp"], "11110": ["$30", "$fp"], "11111": ["$31", "$ra"],
}
etichete = {0: "balls"}

def get_register_binary(register):
    for key, components in regs.items():
        if register in components:
            return key
    return "0"

def instr(line,nrinstr):  # line = the entire instruction
    components = line.strip().split()

    opcode = components[0]
    if opcode not in opcodes:
        print("Instruction not found")
        return

    binary_instruction = opcodes[opcode]

    binary_codification = [binary_instruction]

    if opcode == "j":
        address = components[1]
        binary_codification.append(format(int(etichete[address]), f"0{26}b"))
    elif opcode == "beq":
        rt = get_register_binary(components[1].split(',')[0])
        rs = get_register_binary(components[2].split(',')[0])
        address = int(etichete[components[3]])-nrinstr-1
        binary_codification.append(rs)
        binary_codification.append(rt)
        binary_codification.append(format(address, f"0{16}b"))
    elif opcode == "addi":
        rt = get_register_binary(components[1].split(',')[0])
        rs = get_register_binary(components[2].split(',')[0])
        offset = components[3]
        binary_codification.append(rs)
        binary_codification.append(rt)
        binary_codification.append(format(int(offset), f"0{16}b"))

    elif opcode == "lw" or opcode == "sw":
        rt = get_register_binary(components[1].split(',')[0])
        offset = components[2].split('(')[0]
        rs = get_register_binary(components[2].split('(')[1].strip(')'))
        binary_codification.append(rs)
        binary_codification.append(rt)
        binary_codification.append(format(int(offset), f"0{16}b"))
    elif opcode in ["add","sub","and","or","xor"]:
        rd = get_register_binary(components[1].split(',')[0])
        rs = get_register_binary(components[2].split(',')[0])
        rt = get_register_binary(components[3])
        binary_codification.append(rs)
        binary_codification.append(rt)
        binary_codification.append(rd)
        binary_codification.append("00000")
        binary_codification.append(fn[opcode])
    else:
        for component in components[1:]:
            if component.startswith("$"):
                register_binary = get_register_binary(component)
                binary_codification.append(register_binary)
    return ''.join(binary_codification)


def main():
    fileR = open("assembly.txt", "r")
    fileW = open("binar.txt", "w")
    lines = fileR.readlines()
    count = 0
    for line in lines:
        x = line.split(' ', 1)
        if x[0].find(':') != -1:  # eticheta
            x[0]=x[0].split(":")[0]
            etichete.update({x[0]: count})
            lines.remove(line)
        count = count+1
    count = 0
    for line in lines:
        fileW.write(str(instr(line,count)+"\n"))
        count = count+1
    fileR.close()
    fileW.close()

if __name__ == "__main__":
    main()
