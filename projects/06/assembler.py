#!/usr/bin/python3

#parser = argparse.ArgumentParser(prog="Hack Assembler", description="Assemble the Hack assembly to binary")
import sys

with open(sys.argv[1], 'r') as f:
    for i in f.read().splitlines():
        if (i and not i.startswith("//")):
            print(i.strip())

