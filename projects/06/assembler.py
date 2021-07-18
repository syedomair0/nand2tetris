#!/usr/bin/python3

import sys
from pprint import pprint as pp

dest_table = {None  :"000",
              "M"   :"001",
              "D"   :"010",
              "MD"  :"011",
              "A"   :"100",
              "AM"  :"101",
              "AD"  :"110",
              "AMD" :"111"}

comp_table = {0:     {"0"  : "101010",
                      "1"  : "111111",
                      "-1" : "111010",
                      "D"  : "001100",
                      "A"  : "110000",
                      "!D" : "001101",
                      "!A" : "110001",
                      "-D" : "001111",
                      "-A" : "110011",
                      "D+1": "011111",
                      "A+1": "110111",
                      "D-1": "001110",
                      "A-1": "110010",
                      "D+A": "000010",
                      "D-A": "010011",
                      "A-D": "000111",
                      "D&A": "000000",
                      "D|A": "010101"},
                1:    {"M" : "110000",
                       "!M": "110001",
                       "-M": "110011",
                      "M+1": "110111",
                      "M-1": "110010",
                      "D+M": "000010",
                      "D-M": "010011",
                      "M-D": "000111",
                      "D&M": "000000",
                      "D|M": "010101",}
                }

jump_table = {None  :"000",
              "JGT" :"001",
              "JEQ" :"010",
              "JGE" :"011",
              "JLT" :"100",
              "JNE" :"101",
              "JLE" :"110",
              "JMP" :"111"}



symbol_table = {f'R{num}' : f'0{num:015b}' for num in range(16)}
symbol_table.update({'SCREEN': f'0{0x4000:015b}',
                     'KBD'   : f'0{0x6000:015b}',
                     'SP': f'0{0:015b}',
                     'LCL': f'0{1:015b}',
                     'ARG': f'0{2:015b}',
                     'THIS': f'0{3:015b}',
                     'THAT': f'0{4:015b}',
                     })

counter = 16
def build_symbol_table(cmd):
    global counter
    dest, comp, jmp = None, None, None

    if(cmd.startswith('(') and cmd.endswith(')')):
        return
    else:
        if(cmd.startswith('@')):                                    # if it is an A-instruction
            var = cmd[1:]
            if(var.isnumeric() and (int(var) < 2**15)):             # if it is an A-instruction and is entirely a number
                return(f'0{int(cmd[1:]):015b}')
            elif(var not in symbol_table):                          # if A-instruction then look for it in the symbol_table first
                symbol_table[var] = f'0{counter:015b}'
                counter += 1
            return (symbol_table[var])
        elif("=" in cmd or ";" in cmd):                             # if it is a C-instruction
            if('=' in cmd):                                         # if it containes the dest and comp part
                dest,comp = cmd.split('=')
                if(';' in comp):                                    # if it contains the jump part along with the comp and dest part
                    comp, jmp = comp.split(';')
            if(';' in cmd):                                         # if it contains just the comp and jmp part
                comp,jmp = cmd.split(';')

    a_bit = 0
    if(comp is not None and ('M' in comp)):                         # decide the a-bit of the final binary and for the comp_table
            a_bit = 1

    dest_binary = dest_table[dest]
    jmp_binary = jump_table[jmp]
    comp_binary = comp_table[a_bit][comp]
    final_binary = f'111{a_bit}{comp_binary}{dest_binary}{jmp_binary}'

    return(f'{final_binary}')

def get_labels(commands):
    for line, cmd in commands.items():
        if(cmd.startswith('(')):
            label = cmd[1:len(cmd)-1]
            symbol_table[label] = f'0{line:015b}'

with open(sys.argv[1], 'rt') as f:
    commands = {counter : command.strip().partition(' ')[0]# parser(command.strip().partition(' ' )[0])]
                    for counter, command in enumerate(f.read().splitlines(), start=1)
                        if (command and not command.startswith("//") ) }


if __name__ == "__main__":
    get_labels(commands)
    pp(commands)
    filename = sys.argv[1]
    hack_filename = filename.replace('asm', 'hack')
    f = open(hack_filename, 'wt')
    for cmd in commands.values():
        f.write(build_symbol_table(cmd))
        f.write('\n')
