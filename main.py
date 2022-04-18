#The code below is provided to you, you should not need to modify it!
from termcolor import colored
import random
import urllib.request as request
import json

#present_results is provided to you, you should not alter it!
#This function takes a word to print, and an array containing the colours each letter should be printed input
#The first character in the word will be printed in the first colour in the array and so forth
def present_results(word, colours):
  if(len(word)==5 and len(colours) == 5):
    print(colored(word[0],colours[0]), 
      colored(word[1], colours[1]),
      colored(word[2], colours[2]),
      colored(word[3], colours[3]),
      colored(word[4], colours[4]))
  else:
    print('Invalid input to present_results, word or array incorrect length, both should be length 5')
    print('[DEBUG] word length:',len(word),'colour array length:',len(colours))

#The following are tests for the present_results and randint functions
#you can feel free to uncomment and modify them to get a feel for how the functions work

word = "PRINT"
colors = ['green','white','yellow','white','yellow']
present_results(word, colors)
#print(random.randint(2,5))


#Start writing your code for assignment 2 below:

#Check if w is length 5
def Check(w):
    if len(w) == 5:
        return False
    return True
#Code for generate_word (don't forget to add comments):
#this function will generate the word we will be trying to guess
def generate_word():
    print("Getting random word...")
    with request.urlopen('https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json') as response: 
        source = response.read()
        data = json.loads(source) #get json file containing all english words
    
    w, _ = random.choice(list(data.items())) #extract random word
    while Check(w): #get new word until it matches our requirements (length 5 and non-duplicate)
        w, _ = random.choice(list(data.items()))
    print("Found a word!")
    return w    
    
#Code for letter_in_word (don't forget to add comments):
#check if the letter is in the word.
#Parameters: w is the word, l is the letter, and wc is the boolean array that checks if we already guessed the word in the correct place
def letter_in_word(w,l,wc):
    for i in range(len(w)):
        if l == w[i] and wc[i] == False:
            wc[i] = True
            return True #the letter is in the word, return True
    return False

#Code for letter_in_place  (don't forget to add comments):
#checks if the corresponding letter is in place
#w is the word, l is the letter, i is the index of the letter it should match, and
#wc is the boolean array that checks if we already guessed the word in the correct place
def letter_in_place(w,l,i, wc):
    if w[i] == l:
        wc[i] = True
        return True #returns true if the word is matching
    return False

#Code for guess_word (don't forget to add comments):
#This function will deal with the word guessing and the array of colors that will be returned
#wa is the word answer, wg is the word guessed
def guess_word(wa, wg):
    guessed = True
    wc = [False]*len(wa) #check if the letter has already been guessed
    present = ["grey"]*len(wa)
    for i in range(len(wg)):
        if letter_in_place(wa, wg[i], i, wc): #the letter is in the correct position
            present[i] = "green"
        else:
            guessed = False #this means we haven't guessed the word on this turn

    for i in range(len(wg)):
        if letter_in_word(wa, wg[i], wc): #this means the letter is in the word but not the correct position
            present[i] = "yellow"
            
    return present, guessed

#Code for run_game()  (don't forget to add comments):
#will execute the functions in order so the game is playable
def run_game():
    guessed = False
    attempts = 0
    wa = generate_word() 
    print("____________________________________________________________")
    print("Welcome to Pyrdle! Start by trying to guess a 5-letter word:")
    while True: #this loop will run a maximum of 6 times allowing us a maximum of 6 attempts
        wg = input()
        while len(wg) != 5:
            wg = input("Please enter a 5-letter word:")
        colors, guessed = guess_word(wa,wg)
        present_results(wg,colors)
        if guessed:
            print("Congratulations!")
            break
        attempts += 1
        if attempts == 6:
            print("The correct word was:", wa)
            print("Better luck next time!")
            break
run_game()
    
        


#Once everything is complete, run the game using the function call below
#run_game()