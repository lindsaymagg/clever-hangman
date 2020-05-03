'''
Created on Mar 30, 2018

@author: lindsaymagg
'''

import random
DEBUG = False 

def beginGame():
    """Welcomes user to the game, and allows the user to set the difficulty and choose
    how many letters long the mystery word will be and if they want to play on 
    debugging mode or play mode. Then, chooses a word using chooseWord, and begins 
    the game by calling stateGuesses."""
    global DEBUG
    print("Hey, thanks for playing Hangman! \nYou get 12 misses on easy mode and 8 on hard mode.")
    mode = input("Which difficulty do you prefer? (e)asy or (h)ard > ")
    if mode == "e":
        misses = 12
    if mode == "h":
        misses = 8
    debugorna = input("Which mode do you want to use: (d)ebug or (p)lay > ")
    if debugorna == "d":
        DEBUG = True
    numofltrs = int(input("How many letters long would you like the word to be? > "))
    chooseWord(numofltrs,misses,misses)

def chooseWord(numofltrs,missesleft,missesallowed):
    """randomly selects a word from list words that are of desired length
    from list of words lowerwords"""
    f = open("lowerwords.txt")
    lowerwords = f.read().split()
    wordsatgoodlength = []
    for w in lowerwords:
        if len(w) == numofltrs:
            wordsatgoodlength.append(w)
    #print(wordsatgoodlength)
    word = wordsatgoodlength[random.randint(0,len(wordsatgoodlength)+1)]
    print("\nOkay, you have", missesleft, "misses to guess my word. Let's begin.\n")
    stateGuesses(0,word,missesleft,"_ " *len(word),missesallowed,wordsatgoodlength)

def stateGuesses(numofguessessofar,word,missesleft,currenttemplate,missesallowed,wordList):
    """If the user has run out of misses, this function ends the game. If the user guesses the word,
    they win the game. If neither of those happen, it tells the user which letters they have guessed,
    how many misses they have left, and it shows them the word with its unknown letters as "_"
    and known letters filled in. It then prompts them to guess another letter."""
    global DEBUG
    ltrsnotguessed = "abcdefghijklmnopqrstuvwxyz"
    #print(currenttemplate == ((" ").join(list(word)))+" " == False and (missesleft == 0) == False)
    while currenttemplate != ((" ").join(list(word)))+" " != False and (missesleft == 0) == False:
        if DEBUG == True:
            print("(word is",word+")")
            print("# of possible words:",len(wordList))
        print("Letters not yet guessed:",ltrsnotguessed)
        print("Misses remaining = ",missesleft)
        print(currenttemplate)
        ltr = input("Guess a letter > ")
        if ltr not in ltrsnotguessed:
            print("\nYou already guessed "+ltr+". Try a different letter.")
            ltr = input("Guess your next letter. > ")
            while ltr not in ltrsnotguessed:
                print("\nYou already guessed "+ltr+". Try a different letter.")
                ltr = input("Guess your next letter. > ")
        print(".")
        print(".")
        print(".")
        wordListTuple = getNewWordList(currenttemplate,ltr,wordList)
        maxnum = 0
        prevtemp = currenttemplate
        for potTemplate in wordListTuple:
            pottempcount = len(potTemplate[1])
            if DEBUG == True:
                print(potTemplate[0],pottempcount)
            if pottempcount > maxnum:
                maxnum = pottempcount
                #print("maxnum=",maxnum)
                currenttemplate = potTemplate[0]
                #print("currenttemplate=",currenttemplate)
                wordList = potTemplate[1]
                #print("wordList=",wordList)
        ltrsnotguessed = removeltr(ltrsnotguessed,ltr)
        numofguessessofar += 1
        #print(word)
        #print(wordList)
        #print(len(wordList))
        randnum = random.randrange(0,len(wordList))
        #print(randnum)
        word = wordList[randnum]
        if prevtemp == currenttemplate:
            print("\nYou missed.",ltr,"is not in my word.\n")
            missesleft -= 1
        else:
            print("Nice!",ltr,"is in my word.\n")
        
    if currenttemplate == (" ").join(list(word))+" ":
        print("You guessed my word! It was '"+word+".'")
        print("You won in",str(numofguessessofar),"guesses with",str(missesallowed-missesleft),"misses.\nThanks for playing!")
        quit()
    else:
        #print("...numofguessessofar =",numofguessessofar)
        if missesleft == 0:
            print("You're hung!")
            print("My word was '"+word+".'")
            print("You made",str(numofguessessofar+1),"guesses with",str(missesallowed),"misses.")
            quit()

def createTemplate(currenttemplate,word,letter):
    """produces a template for the word incorporating
    the new letter and the already-known letters."""
    if letter in word:
        listytemplate = currenttemplate.split(" ")
        #print(listytemplate)
        indexer = -1
        
        for l in word:
            print("l is",l)
            indexer += 1
            print("indexer is",indexer)
            if l == letter and indexer < len(listytemplate):
                listytemplate[indexer] = letter
                newtemplate = " ".join(listytemplate)
        print("newtemplate is",newtemplate)
        return newtemplate
    if letter not in word:
        print("currenttemplate is",currenttemplate)
        return currenttemplate
    else:
        print("somethingwentwrong")
        
def removeltr(ltrsnotguessed,ltr):
    """alters the string of letters not yet guessed to eliminate
    the letter that was just guessed"""
    ltrsnotguessedlist = list(ltrsnotguessed)
    for letr in ltrsnotguessedlist:
        if letr == ltr:
            ltrsnotguessedlist[ltrsnotguessedlist.index(letr)] = " "
    ltrsnotguessed = "".join(ltrsnotguessedlist)
    return ltrsnotguessed

def getNewWordList(current,letter,wordList):
    """Calls createTemplate to produce a new template for all words in
    list of words that fits the current template. Each unique template becomes
    a dictionary key, and every word that corresponds to a different
    template gets added to the list of words that is the value for 
    that key. Returns a list of 2-tuple with the template with the 
    highest number of words that fit it."""
    #print(wordList)
    d = {}
    for wd in wordList:
        temp = createTemplate(current,wd,letter)
        #print(wd)
        #print(temp)
        if temp in d:
            d[temp].append(wd)
        if temp not in d:
            d[temp] = [wd]
    tupley = []
    for key in d:
        tupley.append((key,d[key]))
    #print(tupley)
    return tupley
      
      
        
if __name__ == '__main__':
    pass
beginGame()
# current = "p _ _ _ _"
# letter = "u"
# wordsatgoodlength = ["pizza","pissn","punny","purpy"]
# getNewWordList(current,letter,wordsatgoodlength)