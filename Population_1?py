import re
from random import choice
'''There is a population, with specific behaviour :
A, B, C, D, E, ... upper case characters are female.
a, b, c, d, e, ... lower case characters are male.
- When they are next to each other, one female and one male will mate and randomly bring to life 0 to 3 newborns.
- Incest, of course is allowed as it is in every biology lab. A male can mate with two females,
 but a female with one male only.
- Newborns can be male or female (randomly), and they will be situated bewtween their parents (including them) in the alphabetical order.
- Reproduction cycle length is one day.
- Everyday, 25 % of the population will move (random individuals).
  Moving involves jumping over the head of 1 or 2 neighbours, randomly to the left or to the right.
- Death happens in a way that's very specific to characters : When they happen to make a
consonant-vowel-consonant group, they are taken away to the words world.
- The life cycles will end if the population stabilises, crashes, or get to a max number you can set to 60.
- Last rule(suggestion) : use Regex

ex : 
day 1 : Az
day 2 : ArZz
__Nobody moved today (random individual from 25% of 4 --> 0)
day 3 : AberQZz (here, 'A' and 'r' had two newborns 'b' and 'e', 'r' and 'Z' gave birth to 'Q'
__death : 'ber' are taken away together.
day 3 : AQZz
__no movements again
day 4 : AQZzZZz (the only possible reproduction was between 'Z' and 'z' they had 3 newborns : 'zZZ'
_movement : population of 7 : 1 traveller. first Z came two places leftwards :
day 4 : ZAQzZZz
day 5 : ZAQrTzZZz
etc ...
'''

pop = 'aZ'

def rep(pop):
    patt= '(?=([a-z][A-Z])|([A-Z][a-z]))'
    mates= [([m[i] for i in range(1,3) if m[i]][0], m.end(0)+1) for m in re.finditer(patt,pop)]
    n = 0 ; b = 0
    while n<len(mates)-1:
        if mates[n+1][1]==mates[n][1]+1 and 64<ord(mates[n][0][1])<91:
            mates.remove(choice([mates[n],mates[n+1]]))
        n+=1
    p=0
    for parents in mates:
        limit = 1+int((201-len(pop))/(3*len(mates)))
        for j in range(choice([i for i in range(0,limit if limit<6 else 5)])):
            b +=1
            nb = chr(choice([i for i in range(97,123)]))
            nb = choice([nb,nb.upper()])
            pop = pop[:parents[1]+p]+nb+pop[parents[1]+p:]
            p+=1
    print('++++ ',b,'births')
    return pop

def kill(pop):
    #patt = '[^aeiou][aeiou][^aeiou]'
    #pop = re.sub(patt,'',pop,flags=re.IGNORECASE)
    #patt1 = r'([a-z])(\1)(\1*)'
    #pop = re.sub(patt1,choice([r'\1',r'\2']),pop,flags=re.IGNORECASE)
    patt2 = '([A-Z])([a-z])([a-z])+'
    pop = re.sub(patt2, choice([r'\1\2', r'\1\3']), pop)
    patt3 = '([a-z])+([a-z])([A-Z])'
    pop = re.sub(patt3, choice([r'\1\3', r'\2\3']), pop)
    patt4 = '([A-Z])([A-Z])([A-Z])'
    pop = re.sub(patt4, r'\1'+r'\3', pop)
    return pop

def move(pop):
    for i in range(len(pop)//2):
        pos = choice([i for i in range(len(pop))])
        t = pop[pos]
        mov = choice([pos+i if 0<=pos+i<=len(pop) else pos for i in[-3,-2,-1,1,2,3]])
        pop = pop[:pos]+pop[pos+1:]
        pop = pop[:mov]+t+pop[mov:]
    return pop

def life(pop):
    print(pop)
    gen=0
    while True:
        ancestor = pop
        gen += 1
        print('--------------------pop size :',len(pop),' - {} generations'.format(gen))
        pop = rep(pop)
        print('repr --->',pop)
        pop = move(pop)
        print('move --->',pop)
        pop = kill(pop)
        print('kill --->',pop)
        if pop == ancestor:
            print('---- no change')
            break
        if len(pop) > 300:
            print('---- overcrowding')
            break
            
pop = life(pop)
