#!/usr/bin/python3

import sys
from pprint import pprint as pp


symbol_table = {f'R{num}' : num for num in range(16)}
symbol_table.update({'SCREEN': 0x4000, 'KBD': 0x6000, 'SP': 0, 'LCL': '1','ARG': '2', 'THIS': '3', 'THAT': '4'})

def parser(cmd):
    dest, comp, jmp = None, None, None

    if(not cmd.startswith('(')):                                    # if it is not a label (iiinal)

"""
        classifications (3 ifs, so to say)
            first: classify it into an A-instruction or a C-instruction
            second: if it is an A-instruction decide if it is just an integer or a symbol. Confused what to return if it is a symbol
            third: if C-instruction, the logic to deal with that is already there
"""          

        if(cmd.startswith('@')):                                    # if it is an A-instruction 
            if(cmd[1:].isnumeric() and (int(cmd[1:]) < 2**15)):     # if it is an A-instruction and is entirely a number 
                return f'{int(cmd[1:]):016b}'
            elif(cmd[1:] in symbol_table):                          # if it is an A-instruction then look for it in the symbol_table first
                return symbol_table[cmd[1:]]
        elif("=" in cmd or ";" in cmd):                             # if it is a C-instruction
            if('=' in cmd):                                         # if it containes the dest and comp part
                dest,comp = cmd.split('=')                  
                if(';' in comp):                                    # if it contains the jump part along with the comp and dest part
                    comp, jmp = comp.split(';')
            if(';' in cmd):                                         # if it contains just the comp and jmp part
                comp,jmp = cmd.split(';')

        a_bit = 0 

        if(comp is not None and ('M' in comp)):                     # decide the a-bit of the final binary and for the comp_table
            a_bit = 1
        
        dest_binary = dest_table[dest]
        jmp_binary = jump_table[jmp]
        comp_binary = comp_table[a_bit][comp]
        final_binary = f'111{a_bit}{comp_binary}{dest_binary}{jmp_binary}'

        pp(f'dest={dest}  comp={comp} jump={jmp} final_binary={final_binary}')
        return(final_binary)

def build_symbol_table(commands):
    counter, constant = 1, list(commands.keys())[-1]
    print(f'the constant is {constant}')
    for line, cmd in commands.items():                              # loop to get labels
        label = ""
        if(cmd.startswith('(')):
            label = cmd[1:len(cmd)-1]

        if label and label not in symbol_table:
            symbol_table[label] = line

    for line, cmd in commands.items():                              # loop to get variables
        variable=""
        if(cmd.startswith('@') and not cmd[1:].isnumeric()):
            variable = cmd[1:]

        if variable and variable not in symbol_table:               # if variable is not empty and variable is not in symbol_table then add it to symbol_table
            symbol_table[variable] = counter + constant
            counter += 1

    return(symbol_table)

with open(sys.argv[1], 'rt') as f:
    commands = {counter : command.strip().partition(' ')[0]
                    for counter, command in enumerate(f.read().splitlines(), start=1)
                        if (command and not command.startswith("//") ) }
    

if __name__ == "__main__":
    pp(commands)
    build_symbol_table(commands)
    pp(symbol_table)
    for cmd in commands.values():
        parser(cmd)
