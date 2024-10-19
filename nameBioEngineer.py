import random

vowels = "euioay"
consonants = "qwrtpsdfghjklzxcvbnm"

VOWEL = 0
CONSONANT = 1

sylabStructures = [[VOWEL],[CONSONANT,VOWEL,CONSONANT],[CONSONANT,VOWEL],[VOWEL,CONSONANT]]

def renderName(name):
    out = ""
    for sylab in name:
        out += sylab
    return out

def randomSylab():
    sylabStructure = sylabStructures[random.randrange(0,len(sylabStructures))]
    sylab = ""
    for x in sylabStructure:
        if(x == VOWEL):
            sylab += vowels[random.randrange(0,len(vowels))]
        if(x == CONSONANT):
            sylab += consonants[random.randrange(0,len(consonants))]
    return sylab

def randomName():
    numberOfSylabs = random.randrange(2,5)
    name = []
    for i in range(numberOfSylabs):
        name.append(randomSylab())
    return name

def randModifyName(name):
    newName = name.copy()

    actionsToMake = random.randrange(1,3)
    done = 0
    while done < actionsToMake:
        randAction = random.randrange(0,2)
        if(randAction == 0): #modify sylab
            randomSylabToChange = random.randrange(0,len(newName))
            newName[randomSylabToChange] = randomSylab()
            done = done + 1
        if(randAction == 1): #add sylab
            if(len(name) < 5):
                newName.append(randomSylab())
                done = done + 1
        if(randAction == 2): #remove sylab
            if len(newName) > 2:
                randIndex = random.randrange(0,len(newName))
                newName.pop(randIndex)
                done = done + 1

    return newName

NAMES_COUNT = 10

def getRandomNames():
    return [randomName() for _ in range(10)]

def modifyNames(father,names):
    return [randModifyName(father) for x in range(len(names))]

def help():
    print("[WRITE]: `help` to get this")
    print("[WRITE]: `R` to completely reset state")
    print("[WRITE]: from 0-9 to pick name to genetically modify")
    print("[WRITE]: `r` to re roll")
    print("[NOTE]: note writing nothing will do the same effect as `r`")
    print("[WRITE]: `back` or `ret` to get previous names")
    print("[NOTE]: you can only go back once")
    print("[WRITE]: `input` to manually set name family")
    print("[NOTE]: you need to seprate sylabs by spaces")


def main():
    print("Welcome to NameBioEngineer!")
    print("made by:")
    print("""_______________.____    ______________       ________  
\\_   _____/_   |    |  /_   \\______   \___  _\\_____  \\ 
 |    __)  |   |    |   |   ||     ___/\  \/ //  ____/ 
 |     \   |   |    |___|   ||    |     \   //       \\ 
 \___  /   |___|_______ \___||____|      \_/ \_______ \\
     \\/                \\/                            \/""")
    help()

    lastGeneticPicker = ""
    names = getRandomNames()
    lastNames = []
    while True:
        print("names: ")
        for x in range(len(names)):
            print(str(x)+". "+renderName(names[x]))
        if(renderName(lastGeneticPicker) != ""):
            print(renderName(lastGeneticPicker)+" ",end="")
        userAction = input("> ")
        if(userAction == "help"):
            help()
            continue
        if(userAction == "input"):
            lastNames = names.copy()
            namer = input("> ")
            lastGeneticPicker = namer.split(" ")
            names = modifyNames(lastGeneticPicker, names)
            continue
        if(userAction == "back" or userAction == "ret"):
            names = lastNames.copy()
            continue
        if(userAction == "R"):
            lastNames = names.copy()
            lastGeneticPicker = ""
            names = getRandomNames()
            continue
        if(userAction == "r" or userAction == ""):
            lastNames = names.copy()
            if(lastGeneticPicker == ""):
                names = getRandomNames()
                continue
            names = modifyNames(lastGeneticPicker, names)
            continue
        if(userAction[0] >= '0' and userAction[0] <= '9'):
            lastNames = names.copy()
            pickedName = names[int(userAction)]
            lastGeneticPicker = pickedName
            names = modifyNames(lastGeneticPicker, names)
            continue
        print("Unknown command")
    return;

if __name__ == "__main__":
    main()