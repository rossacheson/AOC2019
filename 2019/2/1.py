from typing import List

program: List[int]

with open('2019/2/input.txt', mode='r') as file:
    input = file.read()
    program = [int(s) for s in input.split(',')]

## restore the gravity assist program to the "1202 program alarm" state
program[1] = 12
program[2] = 2

## alternative test program
# program = [int(s) for s in [1,9,10,3,2,3,11,0,99,30,40,50]]

## run the program on the intcode computer
i = 0
while True:
    result = -1
    opcode = program[i]
    if(opcode == 99):
        break
    elif(opcode == 1):
        result = program[program[i + 1]] + program[program[i + 2]]
    elif(opcode == 2):
        result = program[program[i + 1]] * program[program[i + 2]]

    program[program[i + 3]] = result
    i += 4

print(program[0])