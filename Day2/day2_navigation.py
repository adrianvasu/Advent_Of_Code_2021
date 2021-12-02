#!/usr/bin/env python3

def p1():
    depth = 0
    x = 0
    f = open('day2_input.txt')
    #f = open('day2_example_input.txt')
    lines = f.readlines()
    for l in lines:
        ins,val = l.split(' ')
        ins = ins.rstrip()
        val = val.rstrip()
        if ins == 'forward':
            x = x + int(val)
        elif ins == 'down':
            depth = depth + int(val)
        elif ins == 'up':
            depth = depth - int(val)
        else:
            print('Error unknown input: ', ins)
    print('Depth: ', depth)
    print('x: ', x)
    print('Answer: ', x*depth)

def p2():
    depth = 0
    x = 0
    aim = 0
    f = open('day2_input.txt')
    #f = open('day2_example_input.txt')
    lines = f.readlines()
    for l in lines:
        ins,val = l.split(' ')
        ins = ins.rstrip()
        val = val.rstrip()
        if ins == 'forward':
            x = x + int(val)
            depth = depth + (aim * int(val))
        elif ins == 'down':
            aim = aim + int(val)
        elif ins == 'up':
            aim = aim - int(val)
        else:
            print('Error unknown input: ', ins)
    print('Depth: ', depth)
    print('x: ', x)
    print('Answer: ', x*depth)

if __name__=='__main__':
    p2()
