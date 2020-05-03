'''
Created on Mar 27, 2018

@author: lindsaymagg
'''

import random 

def beginGame():
    """Welcomes user to the game, and allows the user to set the difficulty. Then,
    begins the game by calling stateGuesses."""
    print("Hey, thanks for playing Hangman! \nYou get 12 misses on easy mode and 8 on hard mode.")
    mode = input("Which difficulty do you prefer? Enter 'e' or 'h' > ")
    if mode == "e":
        misses = 12
    if mode == "h":
        misses = 8
    else:
        print("Please restart the game and enter either e or h.")
    print("\nOkay, you have", misses, "misses to guess my word. Let's begin.\n")
    word = chooseWord()
    #print("..."+word)
    stateGuesses(0,word,"",misses,"_ " *len(word),misses)

def chooseWord():
    """randomly selects a word from list of words lowerwords"""
    f = open("lowerwords.txt")
    lowerwords = f.read().split()
    wordsatgoodlength = []
    necessarylength = random.randint(5,10)
    #print(necessarylength)
    for w in lowerwords:
        if len(w) == necessarylength:
            wordsatgoodlength.append(w)
    #print(wordsatgoodlength)
    word = wordsatgoodlength[random.randint(0,len(wordsatgoodlength)+1)]
    return word

def stateGuesses(numofguessessofar,word,ltrsguessed,missesleft,currenttemplate,missesallowed):
    """If the user has run out of misses, this function ends the game. If the user guesses the word,
    they win the game. If neither of those happen, it tells the user which letters they have guessed,
    how many misses they have left, and it shows them the word with its unknown letters as "_"
    and known letters filled in."""
    if currenttemplate == (" ").join(list(word))+" ":
        print("You guessed my word! It was '"+word+".'")
        print("You won in",str(numofguessessofar),"guesses with",str(missesallowed-missesleft),"misses.\nThanks for playing!")
    else:
        #print("...numofguessessofar =",numofguessessofar)
        if missesleft == 0:
            print("You're hung!")
            print("My word was '"+word+".'")
            print("You made",str(numofguessessofar+1),"guesses with",str(missesallowed),"misses.")
        else:
            print("Letters you've guessed so far:"," ".join(sorted(ltrsguessed)))
            print("Misses remaining = ",missesleft)
            print(currenttemplate)
            ltr = input("Guess a letter > ")
            if ltr in ltrsguessed:
                print("\nYou already guessed "+ltr+". Try a different letter.")
                ltr = input("Guess your next letter. > ")
                while ltr in ltrsguessed:
                    print("\nYou already guessed "+ltr+". Try a different letter.")
                    ltr = input("Guess your next letter. > ")
            print(".")
            print(".")
            print(".")
            getTemplate(numofguessessofar,word,ltrsguessed,missesleft,currenttemplate,missesallowed,ltr)

def getTemplate(numofguessessofar,word,ltrsguessed,missesleft,currenttemplate,missesallowed,ltrtoadd):
    """Checks to see if the guessed letter is in the word, and updates the template.
        Informs user of results."""
    if ltrtoadd in word:
        listytemplate = currenttemplate.split(" ")
        #print(listytemplate)
        indexer = -1
        for l in word:
            #print("l is",l)
            indexer += 1
            if l == ltrtoadd:
                listytemplate[indexer] = ltrtoadd
                newtemplate = " ".join(listytemplate)
        #print(newtemplate)
        print("Nice!",ltrtoadd,"is in my word.\n")
        stateGuesses(numofguessessofar+1,word,ltrsguessed+ltrtoadd,missesleft,newtemplate,missesallowed)
    else:
        print("\nYou missed.",ltrtoadd,"is not in my word.\n")
        stateGuesses(numofguessessofar+1,word,ltrsguessed+ltrtoadd,missesleft-1,currenttemplate,missesallowed)
                
if __name__ == '__main__':
    pass
beginGame()