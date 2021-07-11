#!/opt/homebrew/bin/python3.9

from pprint import pprint as pp

with open('pong/Pong.asm', 'rt') as f:
    commands = {counter : command.strip().partition(' ')[0] 
                    for counter, command in enumerate(f.read().splitlines(), start=1) 
                        if (not command.startswith("//") and command)}

pp(commands)
