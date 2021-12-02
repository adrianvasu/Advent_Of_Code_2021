#!/usr/bin/env python3

def p1():
    f = open("day1_input.txt")
    #f = open("day1_example_input.txt")
    lines = f.readlines()
    counter = 0
    for i in range(1,len(lines)):
        if lines[i].rstrip() > lines[i-1].rstrip():
            counter = counter + 1
    print(counter)

def p2():
    f = open("day1_input.txt")
    #f = open("day1_example_input.txt")
    lines = f.readlines()
    mod = 3
    numGroups = len(lines) - 2
    counter = 0
    for i in range(1, numGroups):
        num1 = 0
        for j in range(0, mod):
            num1 = num1 + int(lines[i + j])
        num2 = 0
        for j in range(0, mod):
            num2 = num2 + int(lines[i - 1 + j])
        if num1 > num2:
            counter = counter + 1
    print(counter)

if __name__=="__main__":
    #p1()
    p2()
