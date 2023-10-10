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
    numberMiss = 0
    inputDuration = []
    hitDuration = []
    missDuration = []

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

                if k == " ":                    #Note: Spacebar has to interrupt the for cicle before the while cicle
                    spacePressed = True
                    break
            
            #Increase in the completition vars
            nowTime = time()
            wordWritten += 1
            numberInputs += 1

            inputDuration.append(nowTime - inputStartTime)

            if isWrong:
                print('Wrong - Wrote: ' + str(keys))
                numberMiss += 1
                missDuration.append(inputDuration[-1])
            else:
                print('Correct - Wrote: ' + str(keys))
                numberHits += 1
                hitDuration.append(inputDuration[-1])

            print('')                           #Just a visual element

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

            inputStartTime = time()             #Getting the time the input started

            randomChar = random.choice('abcdefghijklmnopqrstuvwxyz')    #Generate the char
            print(randomChar)                                           #Show the char
            print('')                                                   #Just a visual element
            k = readkey()                                               #Wait for the typing

            #Increase in stats and stopping vars            
            nowTime = time()
            wordWritten += 1
            numberInputs += 1

            inputDuration.append(nowTime - inputStartTime)

            #Verification process
            if k == randomChar:
                print('Correct - Pressed: ' + str(k))
                numberHits += 1
                hitDuration.append(inputDuration[-1])
            else:
                print('Wrong - Pressed: ' + str(k))
                numberMiss += 1
                missDuration.append(inputDuration[-1])

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
    accuracy = numberHits / numberInputs
    typeAverageDuration = sum(inputDuration) / numberInputs
    hitAverageDuration = sum(hitDuration) / numberHits
    missAverageDuration = sum(missDuration) / numberMiss

    result = {
        "Test Start": startTime,
        "Test End": endDate,
        "Test Duration": testDuration,
        "Number of Types": numberInputs,
        "Number of Hits": numberHits,
        "Accuracy": accuracy,
        "Type Average Duration": typeAverageDuration,
        "Hit Average Duration": hitAverageDuration,
        "Miss Average Duration": missAverageDuration
    }

    print('Programa terminado')
    print(result)
    return