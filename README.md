# Life_Sim

Life simulation for a String of Letters.

''' This code is my first attempt to make a life simulation. It's very basic.
- The population is made of letters. 
- CAPITAL characters ARE FEMALE
- small characters are males
- Newborns are 'a' or 'A', aging comes with getting higher in alphabet range
- reproduction happens randomly when a male and a FEMALE are next to each other
in the string. Reproduction goes down if the population grows too much.
- Dying happens when age grows over 'z' or 'Z'.
- There is also some random travelling (some chars will randomly be chosen to 
jump randomly 1 to 3 chars to the left or right)
- fight happens between two males when they are close to a female.
- females are aging faster when pregnant
- males are aging faster when far from females (in the middle of male groups)

Sometimes, extinction happens, often before the population didn't reach a big enough
size at start. Start it again.
Of course, the algorithm takes some processing and it easily reaches the time limit 
here in SL Code Playground (sometimes it shows nothing, sometimes it does print the first generations.
Try it in your IDE. It stayed quite stable for a long time on my PC with a population around 200.
'''
