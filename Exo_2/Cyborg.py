from Robot import *
from Humane import *
import time
import random

class Cyborg(Robot, Humane):
    
  # Constructeur
    def __init__(self, name, sex = "M"):
        Robot.__init__(self, name)
        Humane.__init__(self, name, sex)
  

  #Méthode qui va retourner toutes les info d'un robot sous format string
    def __str__(self):
        return "Nom du cyborg : {} / Sexe: {}".format(self.name, self.sexe)
    
    def status(self):
        return (Robot.__str__(self)+ " // "+Humane.__str__(self))
    
    def truc_fun():
        turns = 10
        print ("Hello, Let's play hangman! You will have " + str(turns) + " turns!")
        print("")
        # delay
        time.sleep(0.5)
        # set of words to guess from
        wordList = ["geekflare", "awesome", "python", "magic"]
        word = random.choice(wordList)
        guesses = ''
        # loop till no turns are remaining
        while turns > 0:         
            wrong = 0             
            for char in word:      
                if char in guesses:    
                    print(char),    
                else:
                    print("_"),     
                    wrong += 1    
            print("\n")
            if wrong == 0:        
                print ("You won :)")  
                break             
            guess = ''
            if len(guess) < 1:
                guess = raw_input("Guess a character or enter the correct word: ")[0]
            guesses += guess                    
            if guess not in word:  
                turns -= 1        
                print("Wrong")    
                print("You have", + turns, ' turns left!') 
                if turns == 0:           
                    print("You Lose :(")