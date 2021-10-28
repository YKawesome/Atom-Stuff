import re

fhandle = open("input.txt")
lol = list()

for line in fhandle:
    x = int(line)
    lol.append(x)

memes = lol
reee = memes

for thing in lol:
    for meme in memes:
        for ree in reee:
            if (int(thing)+int(meme)+int(ree)==2020):
                print(thing)
                print(meme)
                print(ree)
                break
