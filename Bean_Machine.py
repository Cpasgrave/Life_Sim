# https://www.sololearn.com/Discuss/1065685/assignment-bean-machine
'''
[ASSIGNMENT] BEAN MACHINE - wolfsan
task in this challenge is to create simulation of bean machine or quincunx,which is consists of an upright board with evenly spaced nails in triangular form.
balls are dropped from the opening of the board. every time a ball hit a nail, it goes left or right. balls are accumulated in the slots.
write a problem which takes as input number of balls and slots and then guess the numbers of balls in each slots.
Good luck. 
'''
from random import choice
h = 7 # height of the bean machine
n = 753 # number of beans introduced

machine = [[0 for i in range(j)] for j in range(1,h+1)]
machine[0][0] = n

for raw in range(len(machine)-1):
    for nail in range(len(machine[raw])):
        for bean in range(machine[raw][nail]):
            machine[raw + 1][nail + choice([0,1])] += 1
machine = [' '.join(['.']*(h-len(i))+[' '*(len(str(n))-len(str(j)))+str(j) for j in i]+['.']*(h-len(i))) for i in machine]
print('\n'.join(machine))
