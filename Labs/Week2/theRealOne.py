# This will import set_file() and read_byte() functions
# To read a file you must first call set_file("name_of_file"),
# Then you can call read_byte() to get the bytes of the file 1 by 1
from readfile import *

### The Protocol ###
# The first 4 bytes should be (in hex) 31 41 FA CE
# The next 2 bytes say how many operations will be in the file
# the next 1 byte contains the operations to perform

### Operations ###
# 0000 0001 - Addition
# The first operand is the first 2 bytes after the op code
# The second operand is the second 2 bytes after the op code
### 0000 0010 - Subtraction
# The first operand is the first 2 bytes after the op code
# The second operand is the second 2 bytes after the op code
# 0000 0011 - Multiplication
# The first operand is the first 2 bytes after the op code
# The second operand is the second 2 bytes after the op code
### 0000 0100 - Division
# The first operand is the first 2 bytes after the op code
# The second operand is the second 2 bytes after the op code
### 0000 0101 - Print
# The string starts immediately after the operation byte
# It ends when the the byte that codes for an ASCII newline is found (e.g. ‘\n’, ‘\x0a’)

### Result ###
# Create a list with the results from the operations in the order they are run
# For all math ops, push a number into the list
# For the "Print" op, push the ASCII string coded by the bytes into the list
# Write a function to open and then execute a program file formatted for "The Machine"
# program_file will be a string of the file to open
# As the program executes you should store a list of numbers of the results
# At the end return the list of numbers
from readfile import *

def execute(program_file):
    result = []
    # Your code here
    file = set_file(program_file)
    header = b''
    for i in range(4):
        header += read_byte()
    if header != b'\x31\x41\xfa\xce':
        print('This file is invalid.')

    numOperationsByte = b''
    for i in range(2):
        numOperationsByte += read_byte()
    numOperations = int.from_bytes(numOperationsByte, "big")

    if type(numOperations) is not int:
        print('This file has an invalid number of operations')

    #each operation has two bytes for each number and 2 bytes for the operation
    bytesFromOp = 6 * numOperations
    bytesRead = 0
    for operations in range(numOperations):
        operandByte = b''
        firstNumByte = b''
        secondNumByte = b''
        for i in range(2):
            operandByte += read_byte()
            bytesRead += 1
            
        operand = int.from_bytes(operandByte, "big")
        
        for i in range(2):
            firstNumByte += read_byte()
            bytesRead += 1
            
        firstNum = int.from_bytes(firstNumByte, "big")
        
        for i in range(2):
            secondNumByte += read_byte()
            bytesRead += 1
            
        secondNum = int.from_bytes(secondNumByte, "big")
        
        print('number of bytes read: %' % bytesRead)

        if operand == 1:
            ans = firstNum + secondNum
            result.append(ans)

        elif operand == 2:
            ans = firstNum - secondNum
            result.append(ans)

        elif operand == 3:
            ans = firstNum * secondNum
            result.append(ans)

        elif operand == 4:
            ans = firstNum / secondNum
            result.append(ans)

        elif operand == 5:
            pass

        else:
            pass

        
    return result
        
    testbank = [
    [3],
    ['1 + 2 =\n', 3],
    ['Hello World!\n'],
    ['10 + 100 =\n', 110],
    [85, 8, 3.0, 720, 'ALL DONE!\n'],
    [5, 3, 24, 3.0, 'ABCDEFG\n'],
    ['4 + 1 =\n', 5, '\n', '10 * 100 =\n', 1000, '\n', '100 / 10 =\n', 10.0, '\n', '5 / 3 =\n', 1.6666666666666667],
    ['H   H EEEEE L     L      OOO       W   W  OOO  RRRR  L     DDDD  !!\n', 'H   H E     L     L     O   O      W W W O   O R   R L     D   D !!\n', 'HHHHH EEEEE L     L     O   O      W W W O   O RRRR  L     D   D !!\n', 'H   H E     L     L     O   O       W W  O   O R   R L     D   D !!\n', 'H   H EEEEE LLLLL LLLLL  OOO        W W   OOO  R   R LLLLL DDDD  !!\n']
]

for i in range(8):
    file = 'program' + str(i+1)
    assert(testbank[i] == execute(file))