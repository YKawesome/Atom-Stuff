import random
#Syntax: random.choice(*list*) will pick a random thingie from a list
#more Synthx: random.choices(*list*, k=*howmany*) will pick k random thingies from a list
print("Copyright Yousef Khan, LLC (not really) :D\n")

def mergeList(list1, list2, list3):
    list4 = list1 + list2 + list3
    return list4

who = ["Green", "White", "Scarlet", "Peacock", "Plum", "Mustard"]
what = ["Rope", "Candlestick", "Dagger", "Wrench", "Lead Pipe", "Revolver"]
where = ["Bathroom", "Office", "Dining Room", "Game Room", "Garage", "Bedroom", "Living Room", "Kitchen", "Courtyard"]
playerCount = 0


while (1):
    try:
        playerCount = int(input("How many players? "))
        if (playerCount <= 6 and playerCount >= 3):
            print("Player Count: " + str(playerCount))
            break
        else:
            print("Not a valid amount of players silly!")
            continue
    except:
        print("U are mistake.")
        continue

playernames = list()

for i in range(playerCount):
    pname = input("Player name? ")
    playernames.append(pname)


#picking the thingies
whodunnit = random.choice(who)
who.remove(whodunnit)

whatdunnit = random.choice(what)
what.remove(whatdunnit)

wheredunnit = random.choice(where)
where.remove(wheredunnit)

numfaceup = 0
cardsperplayer = 0

if (playerCount == 6):
    numfaceup = 6
    cardsperplayer = 2

if (playerCount == 5):
    numfaceup = 3
    cardsperplayer = 3

if (playerCount == 4):
    numfaceup = 6
    cardsperplayer = 3

if (playerCount == 3):
    numfaceup = 6
    cardsperplayer = 4

cards = mergeList(who, what, where)

faceups = random.sample(cards, numfaceup)

for x in faceups:
    cards.remove(x)
    print(x)

playerdata = list()

playerone = dict()
playerone["name"] = playernames[0]
playerdata.append(playerone)

playertwo = dict()
playertwo["name"] = playernames[1]
playerdata.append(playertwo)

playerthree = dict()
playerthree["name"] = playernames[2]
playerdata.append(playerthree)

playerfour = dict()
try:
    playerfour["name"] = playernames[3]
except:
    playerfour["name"] = None
playerdata.append(playerfour)

playerfive = dict()
try:
    playerfive["name"] = playernames[4]
except:
    playerfive["name"] = None
playerdata.append(playerfive)

playersix = dict()
try:
    playersix["name"] = playernames[5]
except:
    playersix["name"] = None
playerdata.append(playersix)



for dicti in playerdata:
    try:
        pcards = random.sample(cards, cardsperplayer)
        for card in pcards:
            cards.remove(card)
        dicti["Cards"] = pcards
    except:
        dicti["Cards"] = None


print(playerdata)











#for i in playernames:



#look at your history to send messages to ppl abt there stuff, you found it :D
