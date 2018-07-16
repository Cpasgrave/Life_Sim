from re import finditer, sub
from random import choice, getrandbits

pop = 'poPuLaTIOn'
def F_m_split(pop):
    # this function separates males and females in a list to make it easy to work on them separately
    n=0
    for i in range(len(pop)-1):
        for j,k in [(1,0),(0,1)]:
            if pop[i+n+j] == pop[i+n+j].upper() and pop[i+n+k] != pop[i+n+k].upper():
                pop = pop[:i+n+1]+'.'+pop[i+n+1:]
                n+=1
    pop = pop.split('.')
    return pop
def repro(pop):
    pop = F_m_split(pop)
    # working on female groups
    for r in range(0 if pop[0] == pop[0].upper() else 1,len(pop),2):
        # The females next to males are pregnant, they are aging faster (+5 gen)
        mid = pop[r][1:-1] if len(pop[r])>2 else ''
        right = chr(ord(pop[r][-1])+5) if len(pop[r])>1 else ''
        pop[r]=chr(ord(pop[r][0])+5)+mid+right
        # On the left and right side of each female group,
        # random female or male newborns (0 or 1 per female)
        # take their place as 'a' or 'A'
        rate = -1 if len(pop)>200 else (0 if len(pop)>100 else 1)
        for s in range(choice([i for i in range(1+rate if len(pop[r])==1 else 2+rate)])):
                a,b=getrandbits(1),getrandbits(1)
                pop[r] = [['a','A'][a]+pop[r],pop[r]+['a','A'][a]][b]
    return ''.join(pop)
def age(pop):
    pop=list(pop)
    for i in range(len(pop)):
        pop[i]=chr(ord(pop[i])+1)
    return ''.join(pop)
def die(pop):
    pop = list(pop)
    for i in range(len(pop)):
        if 97>ord(pop[i])>90 or ord(pop[i])>122:
            pop[i]=''
    return ''.join(pop)
def fight(pop):
    pop = F_m_split(pop)
    for r in range(0 if pop[0] == pop[0].lower() else 1, len(pop), 2):
        # Here the males are fighting and randomly dying when they are two, close to a female
        if len(pop[r])<3:
            pass
        if len(pop[r])==3:
            pop[r]=pop[r][0]+choice([pop[r][1],''])+pop[r][1]
        if len(pop[r])>3:
            mid = ''.join([chr(ord(i)+3) for i in pop[r][2:-2]])
            pop[r]=pop[r][0]+choice([chr(ord(pop[r][1])+3),''])+ mid +choice([chr(ord(pop[r][-2])+3),''])+pop[r][-1]

    return ''.join(pop)
def move(pop):
    for i in range(len(pop)//2):
        pos = choice([i for i in range(len(pop))])
        t = pop[pos]
        mov = choice([pos+i if 0<=pos+i<=len(pop) else pos for i in[-3,-2,-1,1,2,3]])
        pop = pop[:pos]+pop[pos+1:]
        pop = pop[:mov]+t+pop[mov:]
    return pop
def detailed_life(pop, gen):
    print(pop)
    for i in range(gen):
        pop = repro(pop)
        print(pop, ' - after repro')
        pop = age(pop)
        print(pop, ' - after age')
        pop = die(pop)
        print(pop, ' - after die')
        pop = fight(pop)
        print(pop, ' - after fight')
        pop = move(pop)
        print(pop, ' - after move')
def life(pop,gen):
    print(pop)
    for i in range(gen):
        pop = repro(pop)
        pop = die(pop)
        print(len(pop),'-',pop)
        pop = age(pop)
        pop = die(pop)
        if pop=='':
            print('extinction')
            break
        pop = fight(pop)
        pop = move(pop)
life(pop,1000)
