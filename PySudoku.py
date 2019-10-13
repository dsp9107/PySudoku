import json

def new():
    return [[0 for i in range(9)] for j in range(9)]

def load(mode='easy'):
    global sdk
    with open("puzzle_" + mode + ".txt", "r") as p:
        sdk = json.loads(p.read())

def show(sudoku):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end = ' ')
            if not ((j+1) % 3) and (j < 8) :
                print("|", end = ' ')
        print()
        if not ((i+1) % 3) and (i < 8) :
            for k in range(9 + 2):
                print("-", end = ' ')
            print()

sdk = new()
load('easy')
show(sdk)
