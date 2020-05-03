# hangman
Spring 2018 CS101 (Introduction to CS) Assignments #4 and #5

This was an assignment for my intro to programming class.
Hangman instructions: https://docs.google.com/document/d/1e79vggjLc389Y9AW6_qAAo2FyhjjQaW_Ofnrdp-QxI0/edit#heading=h.dfbkxtalt81v
Clever hangman instructions: https://docs.google.com/document/d/1Gd9GeS4YqyIV8JYwQrmlcOr__y3FLLeKhC-y_CrWl8g/edit

Hangman:
"The user must be given a choice of (e)asy or (h)ard which are 12 and 8 misses until hung, respectively. You do not need to check for bad user-input. For example, you can assume the user will enter an 'h' or an 'e'. See the runs below where the default is 12 for easy and the user can enter 'h' for hard.
A secret word must be chosen at random from the file lowerwords.txt. First a length between 5 and 10 (inclusive) must be chosen at random and then a word from all words of that length must be chosen at random from these words as the secret word.
The user must be shown all the letters already guessed, these letters must appear in sorted order (see the runs below). These include letters in the word as well as missed letters.
The user must be told how many misses are left on each turn when the user enters a letter. When a letter in the word is correctly guessed the number of misses doesn't change, but an incorrectly-guessed letter changes the number of misses.
A letter already guessed should not count as a miss and should not count as a guess when reporting summary game statistics.
When the user has guessed the word, or the number of misses allowed is reached, the game should be over and summary statistics about the number of guesses and misses should be printed. See the sample runs below.
On each turn the secret "word" should be printed with underscores for unknown letters and correctly-guessed letters in place as warranted. A single space should appear between each underscore and letter."

Clever hangman:
"The user must be asked how many letters in the word to be guessed and then a word from all words of that length must be chosen at random from these words as the secret word. This is different from the Hangman program where the number of letters in the secret word was chosen at random. You do not need to guard against bad user input.
The user must be shown all the letters that have not yet been guessed, these letters must appear in sorted order (see the runs below). These include letters in the word as well as missed letters. This is different from the Hangman program where the user was shown letters already guessed, rather than letters not yet guessed.
You must make the program "clever" in that after each letter guessed the list of possible secret words is as large as possible. This is described in detail below. As part of making the program clever you must write and call two functions described below.
You must include a global DEBUG variable that when set to True provides information about the list of possible secret words and how dictionary keys/values are used in creating a new list of possible secret words after each letter guessed. The user should be prompted as to whether the DEBUG value is True (for debug mode) or False (for play mode)."

