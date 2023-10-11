#!/usr/bin/env python3

#Import section
import random   #Generate random values
import readchar #Read keys

from time import time, ctime            #Time related functions
from colorama import Fore, Back, Style  #Color for the style
from readchar import readkey, key       #Read keys
from collections import namedtuple      #Use namedtuples
from pprint import pprint               #Pretty-print

Input = namedtuple('Input', ['requested', 'received', 'duration']) #tupple to store the variables

#main program function
def runProgram(timeMode, maxValue, useWords):

    #Get a list of words
    wordFile = "palavras.txt"
    WORDS = open(wordFile).read().splitlines()

    #main vars for stats and for stoping reseted
    startTime = time()          #Start Time
    startDate = ctime()         #Start Date
    spacePressed = False        #Ensuring that this ending var starts false
    numberInputs = 0            #Reset number of inputs
    numberHits = 0              #Reset number of hits
    numberMiss = 0              #Reset number of miss
    inputDuration = []          #Empty lists to append values later
    hitDuration = []
    missDuration = []
    inputData = []

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
            size = len(randomWord)              #Get the lenght of the word
            printBox(randomWord)                #Show the word
            
            #Cicle to wait for the whole word be typed
            isWrong = False
            keys = ''
            for i in range(0,size):
                k = readkey()
                keys += k
                print(k,end='',flush=True)

                if k != randomWord[i]:          #this verifies if there is any lether wrong
                    isWrong = True

                if k == " ":                    #Spacebar has to interrupt the for cicle before the while cicle
                    spacePressed = True
                    break
            
            #Increase in the completition vars
            nowTime = time()
            numberInputs += 1

            inputDuration.append(nowTime - inputStartTime)

            print() #Just a visual cleaning element
            
            #Verifying process
            if isWrong:
                print(Fore.RED+Style.BRIGHT+'Wrong - You wrote: ' + str(keys)+Style.RESET_ALL)
                numberMiss += 1
                missDuration.append(inputDuration[-1])
            else:
                print(Fore.GREEN+Style.BRIGHT+'Correct - You wrote: ' + str(keys)+Style.RESET_ALL)
                numberHits += 1
                hitDuration.append(inputDuration[-1])

            print() #Just a visual element

            #Storing the data in tupple form
            inputData.append(Input(randomWord, keys, f"{inputDuration[-1]:.2f}"))

            #Verify if the completition conditions were satisfied
            if conditionEnd == 'Time' and nowTime - startTime >= maxValue:      #Ending with time
                break
            elif conditionEnd == 'Words' and numberInputs >= maxValue:          #Ending with number of words
                break
            elif spacePressed:                                                  #Ending with spacebar
                break

    else:
        while True: #Mode of chars

            inputStartTime = time()             #Getting the time of the input started

            randomChar = random.choice('abcdefghijklmnopqrstuvwxyz')    #Generate the char
            printBox(randomChar)                                        #Show the char
            k = readkey()                                               #Wait for the typing
            print()                                                     #Just a visual element


            #Increment stats and stopping vars            
            nowTime = time()
            numberInputs += 1
            
            inputDuration.append(nowTime - inputStartTime)

            #Verification process
            if k == randomChar:                         #Its Correct
                print(Fore.GREEN+Style.BRIGHT+'Correct - Pressed: ' + str(k)+Style.RESET_ALL)
                numberHits += 1
                hitDuration.append(inputDuration[-1])
            else:                                       #Its Wrong
                print(Fore.RED+Style.BRIGHT+'Wrong - Pressed: ' + str(k)+Style.RESET_ALL)
                numberMiss += 1
                missDuration.append(inputDuration[-1])

            #Storing the data in tupple form
            inputData.append(Input(randomChar, k, f"{inputDuration[-1]:.2f}"))

            #Verify if the completition conditions were satisfied
            if conditionEnd == 'Time' and nowTime - startTime >= maxValue:  #Ending with time
                break
            elif conditionEnd == 'Words' and numberInputs >= maxValue:         #Ending with number of words
                break
            elif k == " ":                                                    #Ending with spacebar
                break
    
    #Avoiding diving for zero
    if numberInputs == 0:
        numberInputs = 1
    if numberHits == 0:
        numberHits = 1
    if numberMiss == 0:
        numberMiss = 1

    #Saving the end time of the test and calculating duration
    endTime = time()                                            #Time of ending
    endDate = ctime()                                           #Date of ending
    testDuration = endTime - startTime                          #Duration of the test
    accuracy = numberHits / numberInputs * 100                  #Accuracy of the test
    typeAverageDuration = sum(inputDuration) / numberInputs     #Average duration
    hitAverageDuration = sum(hitDuration) / numberHits          #Average duration of the hits
    missAverageDuration = sum(missDuration) / numberMiss        #Average duration of the miss

    #Formating the main vars to declutter the final visual
    fAccuracy = str(f"{accuracy:.1f}")+'%'
    fHitDuration = f"{hitAverageDuration:.2f}"
    fMissDuration = f"{missAverageDuration:.2f}"
    fTestDuration = f"{testDuration:.2f}"
    fTypeDuration = f"{typeAverageDuration:.2f}"

    #Dictionary with all the stats vars
    result = {
        "Inputs": inputData,
        "Test Start": startDate,
        "Test End": endDate,
        "Test Duration": fTestDuration,
        "Number of Types": numberInputs,
        "Number of Hits": numberHits,
        "Number of Miss": numberMiss,
        "Accuracy": fAccuracy,
        "Type Average Duration": fTypeDuration,
        "Hit Average Duration": fHitDuration,
        "Miss Average Duration": fMissDuration
    }

    #Printing the end of the programm
    print()
    pprint(result)
    return

#Function that creates a visual box to include the word/character
def printBox(text):
    textLength = len(text)
    border = "+" + "-" * (textLength + 2) + "+"
    emptyLine = "|" + " " * (textLength + 2) + "|"
    
    print(border)
    print(emptyLine)
    print(f"| {text} |")
    print(emptyLine)
    print(border)
