#!/usr/bin/env python3
#Tower of hanoi solver

def showStacks(S1, S2, S3):
    '''Visualises tower of hanoi using ascii art'''
    height = len(S1)+len(S2)+len(S3) + 1
    width = height
    for step in range(height):
        #S1
        idx1 = height - step - 1
        if idx1 < len(S1):
            c1 = S1[idx1]
        else:
            c1 = 0

        #S2
        idx2 = height - step - 1
        if idx2 < len(S2):
            c2 = S2[idx2]
        else:
            c2 = 0

        #S3
        idx3 = height - step - 1
        if idx3 < len(S3):
            c3 = S3[idx3]
        else:
            c3 = 0
        print(' '*(width-c1)+'*'*c1+'| '  +  ' '*(width-c2)+'*'*c2+'| '  +  ' '*(width-c3)+'*'*c3+'|')
    print('-'*width + '| ' +'-'*width + '| ' +'-'*width + '| ')
    


def initStack(diskCount = 3):
    S1 = []
    for c in range(diskCount, 0, -1):
        S1.append(c)
    return S1, [], []

def hanoiSolve(S, dest = 2, source = 0, height = 3, steps=[0]):
    '''There are 3 poles, a left pole, a middle pole and a right pole.
    The stacks on these poles correspond to the values at indices 0,1,2 of S
    S[0] is the leftmost stack, S[1] is the middle one, S[2] is the rightmost.
    At any move one of this stack will be source, another will be destination
    and the third will be the intermediate'''
    #Find the index of the stack that is neither source nor dest
    intermediate = 0
    for idx in range(3):
        if idx != dest and idx != source:
            intermediate = idx

    '''Height indicates the number of disks to move.
    Algorithm:
    Move all(height -1) disks on top to intermediate pole
    Then move the disk from source pole to dest.
    Move all(height -1) disk that were moved to intermediate again to dest.
    If we have more than 1 disk, we need to recursively call hanoisolve, to move them'''
    if height > 1:
        hanoiSolve(S, dest = intermediate, source = source, height = height-1, steps=steps)
    S[dest].append(S[source].pop())
    steps[0] += 1
    print("Step", steps[0] , ':')
    showStacks(S[0], S[1], S[2])
    if height > 1:
        hanoiSolve(S, dest = dest, source = intermediate, height = height -1, steps=steps)


height = int(input("Height:"))
steps = [0]
S1, S2, S3 = initStack(height)
hanoiSolve([S1, S2, S3], dest = 2, source = 0, height = height, steps=steps)
print("Total Steps:", steps[0])
