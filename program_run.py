#!/usr/bin/env python3

#Import section
import random   #Generate random values
import readchar #Read keys

from time import time, ctime            #Time related functions
from colorama import Fore, Back, Style  #Color for the mainstyle
from readchar import readkey, key       #read keys
from collections import namedtuple      #Use namedtuples

Input = namedtuple('Input', ['requested', 'received', 'duration']) #tupple to store the variables

#main program function
def runProgram(timeMode, maxValue, useWords):

    #Get a list of words
    wordFile = "palavras.txt"
    WORDS = open(wordFile).read().splitlines()

    #main vars for stats and for stoping reseted
    startTime = time()
    startDate = ctime()
    wordWritten = 0
    spacePressed = False
    numberInputs = 0
    numberHits = 0

    #Check if its time mode or words mode
    if timeMode:
        conditionEnd = 'Time'
    else:
        conditionEnd = 'Words'
    
    #Main logic of the program
    if useWords:
        while True: #Mode of words

            inputStartTime = time()             #Getting the time the input started

            randomWord = random.choice(WORDS)   #Generate the word
            size = len(randomWord)                #Get the lenght of the word
            print(randomWord)                   #Show the word
            
            #Cicle to wait for the whole word be typed
            isWrong = False
            keys = ''
            for i in range(0,size):
                k = readkey()
                keys += k

                if k != randomWord[i]:          #this verifies if there is any lether wrong
                    isWrong = True
                else:
                    numberHits += 1

                if k == " ":                    #Note: Spacebar has to interrupt the for cicle before the while cicle
                    spacePressed = True
                    break
            
            if isWrong:
                print('Wrong - Wrote: ' + str(keys))
            else:
                print('Correct - Wrote: ' + str(keys))

            print('')                           #Just a visual element

            #Increase in the completition vars
            nowTime = time()
            wordWritten += 1
            numberInputs += 1

            inputDuration = nowTime - inputStartTime

            #Storing the data in tupple form
            inputData = Input(randomWord, keys, inputDuration)


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
                print('Correct - Pressed: ' + str(k))
                numberHits += 1
            else:
                print('Wrong - Pressed: ' + str(k))

            #Increase in stats and stopping vars            
            nowTime = time()
            wordWritten += 1
            numberInputs += 1

            inputDuration = nowTime - inputStartTime

            #Storing the data in tupple form
            inputData = Input(randomChar, k, inputDuration)

            #Verify if the completition conditions were satisfied
            if conditionEnd == 'Time' and nowTime - startTime >= maxValue:
                break
            if conditionEnd == 'Words' and wordWritten >= maxValue:
                break
            if k == " ":
                break
    
    #Saving the end time of the test and calculating duration
    endTime = time()
    endDate = ctime()
    testDuration = endTime - startTime
    accuracyHits = numberHits / numberInputs

    print('Programa terminado')
    return