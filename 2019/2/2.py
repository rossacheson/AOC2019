from typing import List

initial_memory: List[int]
DESIRED_OUTPUT = 19690720

with open('2019/2/input.txt', mode='r') as file:
    input = file.read()
    initial_memory = [int(s) for s in input.split(',')]


def intcode_compute(noun:int, verb:int):
    program = initial_memory.copy()
    program[1] = noun
    program[2] = verb

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

        try:
            program[program[i + 3]] = result
        except IndexError as e:
            print(e)

        i += 4

    return program[0]


def find_noun_verb_pair():
    for i in range(100):
        for j in range(100):
            result = intcode_compute(i, j)
            if(result == DESIRED_OUTPUT):
                return { 'noun': i, 'verb': j }


noun_verb_dict = find_noun_verb_pair()

if(noun_verb_dict == None):
    raise Exception('Error: no combination resulted in the desired output of ' + DESIRED_OUTPUT)

noun = noun_verb_dict.get('noun', -1)
verb = noun_verb_dict.get('verb', -1)
print('noun: ' + str(noun))
print('verb: ' + str(verb))
final_answer = 100 * noun + verb
print('final answer: ' + str(final_answer))