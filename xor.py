import sys

def xor():
    return ''.join(list('\\x' + hex(ord(x) ^ 0x2A)[2:] for x in sys.argv[1]))

xor()
