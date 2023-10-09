#!/usr/bin/env python3

#Import section
import random   #Generate random values
import readchar #Read keys

from time import time, ctime            #Time related functions
from colorama import Fore, Back, Style  #Color for the mainstyle
from readchar import readkey, key       #read keys

#main program function
def runProgram(timeMode, maxValue, useWords):

    #Get a list of words
    wordFile = "palavras.txt"
    WORDS = open(wordFile).read().splitlines()

    #main vars of completetion reseted
    startTime = time()
    wordWritten = 0
    spacePressed = False

    #Check if its time mode or words mode
    if timeMode:
        conditionEnd='Time'
    else:
        conditionEnd='Words'
    
    #Main logic of the program
    if useWords:
        while True: #Mode of words

            randomWord = random.choice(WORDS)   #Generate the word
            size=len(randomWord)                #Get the lenght of the word
            print(randomWord)                   #Show the word
            print('')                           #Just a visual element
            
            #Cicle to wait for the whole word be typed
            keys=''
            for i in range(0,size):
                k = readkey()
                keys += k
                
                if k == " ":                    #Note: Spacebar has to interrupt the for cicle before the while cicle
                    spacePressed = True
                    break
            
            #Cicle to verify if the word its correct or not
            for i in range(0,size):
                if keys[i] != randomWord[i]:
                    print('Wrong')
                else:
                    print('Correct')
            print('')

            #Increase in the completition vars
            nowTime = time()
            wordWritten += 1

            #Verify if the completition conditions were satisfied
            if conditionEnd == 'Time' and nowTime - startTime >= maxValue:
                break
            if conditionEnd == 'Words' and wordWritten >= maxValue:
                break
            if spacePressed:
                break

    else:
        while True: #Mode of chars

            randomChar = random.choice('abcdefghijklmnopqrstuvwxyz')    #Generate the char
            print(randomChar)                                           #Show the char
            print('')                                                   #Just a visual element
            k = readkey()                                               #Wait for the typing

            #Verification process
            if k == randomChar:
                print('Correct')
            else:
                print('Wrong')

            #Increase in the completition vars            
            nowTime = time()
            wordWritten += 1

            #Verify if the completition conditions were satisfied
            if conditionEnd == 'Time' and nowTime - startTime >= maxValue:
                break
            if conditionEnd == 'Words' and wordWritten >= maxValue:
                break
            if k == " ":
                break

    print('Programa terminado')
    return