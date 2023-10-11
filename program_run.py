#!/usr/bin/env python3

#Import section
import random   #Generate random values
import readchar #Read keys
import time     #Time functions

from colorama import Fore, Back, Style  #Color for the style
from readchar import readkey, key       #Read keys
from collections import namedtuple      #Use namedtuples
from pprint import pprint               #Pretty-print

Input = namedtuple('Input', ['requested', 'received', 'duration']) #tupple to store the variables

#main program function
def runProgram(timeMode, maxValue, useWords, english):

    #Get a list of words
    if english:
        wordFile = "wordlist.txt"
    else:
        wordFile = "palavras.txt"
    
    WORDS = open(wordFile).read().splitlines()

    #main vars for stats and for stoping reseted
    startTime = time.time()          #Start Time
    startDate = time.ctime()         #Start Date
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
            inputStartTime = time.time()                 #Getting the time the input started

            while True: #Note: this cicle was made because some of the english words were too small. For the pr version, it wasn't needed
                randomWord = random.choice(WORDS)   #Generate the word
                size = len(randomWord)              #Get the lenght of the word
                if size >= 4:
                    printBox(randomWord)            #Show the word
                    break
            
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
            nowTime = time.time()
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

            #Storing the data in tupple form
            inputData.append(Input(randomWord, keys, f"{inputDuration[-1]:.2f}"))

            #Verify if the completition conditions were satisfied
            if conditionEnd == 'Time':
                progress = (nowTime - startTime) / maxValue

                if nowTime - startTime >= maxValue:                             #Ending in time limit
                    break

            elif conditionEnd == 'Words':
                progress = numberInputs / maxValue
                
                if numberInputs >= maxValue:                                    #Ending in number of words
                    break

            elif spacePressed:                                                  #Ending with spacebar
                break

            progressBar(progress)
            print()
    else:
        while True: #Mode of chars

            inputStartTime = time.time()             #Getting the time of the input started

            randomChar = random.choice('abcdefghijklmnopqrstuvwxyz')    #Generate the char
            printBox(randomChar)                                        #Show the char
            k = readkey()                                               #Wait for the typing
            print()                                                     #Just a visual element


            #Increment stats and stopping vars            
            nowTime = time.time()
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
            if conditionEnd == 'Time':
                progress = (nowTime - startTime) / maxValue                
                
                if nowTime - startTime >= maxValue:                             #Ending with time
                    break

            elif conditionEnd == 'Words':
                progress = numberInputs / maxValue               
                
                if numberInputs >= maxValue:                                    #Ending with number of words
                    break
            
            elif k == " ":                                                      #Ending with spacebar
                break

            progressBar(progress)
            print()

    
    #Avoiding diving for zero
    if numberInputs == 0:
        numberInputs = 1
    if numberHits == 0:
        numberHits = 1
    if numberMiss == 0:
        numberMiss = 1

    #Saving the end time of the test and calculating duration
    endTime = time.time()                                            #Time of ending
    endDate = time.ctime()                                           #Date of ending
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

    print(Style.BRIGHT+Fore.YELLOW+'Program ended.'+Style.NORMAL+'\nProcessing stats')
    print()
    time.sleep(2)

    if accuracy >= 75:
        print(Style.BRIGHT+Fore.GREEN+'Well done!!!\nAccuracy --> '+fAccuracy+'%'+Style.RESET_ALL)
    
    elif accuracy>=50:
        print(Style.BRIGHT+Fore.YELLOW+'Not bad!\nAccuracy --> '+fAccuracy+'%'+Style.RESET_ALL)        
    
    else:
        print(Style.BRIGHT+Fore.RED+'You can do better!\nAccuracy --> '+fAccuracy+'%'+Style.RESET_ALL)
    print()
    time.sleep(2)

    if useWords:
        if typeAverageDuration > 4:
            print(Style.BRIGHT+Fore.RED+'Bad typing speed\nTime per word: --> '+fTypeDuration+' seconds'+Style.RESET_ALL)
        elif typeAverageDuration > 3:
            print(Style.BRIGHT+Fore.LIGHTRED_EX+'Below average typing speed\nTime per word: --> '+fTypeDuration+' seconds'+Style.RESET_ALL)
        elif typeAverageDuration > 2.4:
            print(Style.BRIGHT+Fore.YELLOW+'Average typing speed\nTime per word: --> '+fTypeDuration+' seconds'+Style.RESET_ALL)
        elif typeAverageDuration > 2:
            print(Style.BRIGHT+Fore.LIGHTYELLOW_EX+'Above average typing speed\nTime per word: --> '+fTypeDuration+' seconds'+Style.RESET_ALL)
        elif typeAverageDuration > 1.7:
            print(Style.BRIGHT+Fore.GREEN+'Good typing speed\nTime per word: --> '+fTypeDuration+' seconds'+Style.RESET_ALL)
        else:
             print(Style.BRIGHT+Fore.LIGHTGREEN_EX+'Professional typing speed\nTime per word: --> '+fTypeDuration+' seconds'+Style.RESET_ALL)

    else:
        if typeAverageDuration > 1.2:
            print(Style.BRIGHT+Fore.RED+'Bad typing speed\nTime per character: --> '+fTypeDuration+' seconds'+Style.RESET_ALL)
        elif typeAverageDuration > 0.9:
            print(Style.BRIGHT+Fore.LIGHTRED_EX+'Below average typing speed\nTime per character: --> '+fTypeDuration+' seconds'+Style.RESET_ALL)
        elif typeAverageDuration > 0.72:
            print(Style.BRIGHT+Fore.YELLOW+'Average typing speed\nTime per character: --> '+fTypeDuration+' seconds'+Style.RESET_ALL)
        elif typeAverageDuration > 0.6:
            print(Style.BRIGHT+Fore.LIGHTYELLOW_EX+'Above average typing speed\nTime per character: --> '+fTypeDuration+' seconds'+Style.RESET_ALL)
        elif typeAverageDuration > 0.51:
            print(Style.BRIGHT+Fore.GREEN+'Good typing speed\nTime per character: --> '+fTypeDuration+' seconds'+Style.RESET_ALL)
        else:
             print(Style.BRIGHT+Fore.LIGHTGREEN_EX+'Professional typing speed\nTime per character: --> '+fTypeDuration+' seconds'+Style.RESET_ALL)
    print()
    time.sleep(2)
    print(Style.BRIGHT+Fore.LIGHTCYAN_EX+'The detailed stats will be printed right away'+Style.RESET_ALL)
    time.sleep(2)

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
    print()

#Function to create a progress bar and update it
def progressBar(progress):
    barLength = 40
    completedLength = int(barLength * progress)     #How much of the bar is completed
    remainingLength = barLength - completedLength   #How much is remaining
    completedPart = Fore.GREEN + '-' * completedLength
    remainingPart = Fore.RESET + ' ' * remainingLength
    print(Style.BRIGHT+'|'+completedPart + remainingPart+'| -> Progress: '+str(int(progress*100))+'%'+Style.RESET_ALL)  # Print the progress bar, and use '\r' to overwrite the same line
