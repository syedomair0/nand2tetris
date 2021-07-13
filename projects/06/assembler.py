#!/usr/bin/python3

import sys
import re
from pprint import pprint as pp

"""Not efficient at all!!! Write better code"""

jump_table = {"null":"000",
              "JGT" :"001",
              "JEQ" :"010",
              "JGE" :"011",
              "JLT" :"100",
              "JNE" :"101",
              "JLE" :"110",
              "JMP" :"111"}


dest_table = {"null":"000",
              "M"   :"001",
              "D"   :"010",
              "MD"  :"011",
              "A"   :"100",
              "AM"  :"101",
              "AD"  :"110",
              "AMD" :"111"}

comp_table = {"0": {"0"  : "101010",
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
                "1": {"M" : "110000",
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

def parser(cmd):
    ret = ""
    dest, comp, jmp = None, None, None
    if(cmd.startswith('@')):
        """
        there needs to be a condition here for resolving symbols and integers
        """
        if(cmd[1:].isnumeric() and (int(cmd[1:]) < 2**15)):
            ret += f'{int(cmd[1:]):016b}'
            return ret
    elif("=" in cmd or ";" in cmd):
        if('=' in cmd):
            dest,comp = cmd.split('=')
            if(';' in comp):
                comp, jmp = comp.split(';')
        if(';' in cmd):
            comp,jmp = cmd.split(';')
        return(f'dest={dest}, comp={comp}, jump={jmp}')

def code():
    pass

def build_symbol_table():
    pass

with open(sys.argv[1], 'rt') as f:
    commands = {counter : [command.strip().partition(' ')[0], True if command.startswith("(") else False, parser(command.strip().partition(' ' )[0])]
                    for counter, command in enumerate(f.read().splitlines(), start=1)
                        if (not command.startswith("//") and command) }

if __name__ == "__main__":
    pp(commands)
