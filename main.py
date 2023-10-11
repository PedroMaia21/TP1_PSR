#!/usr/bin/env python3
#ola
#import section
import argparse #arguments
import readchar #read keys
import time     #time related functions

from program_run import runProgram      #function to not pollute the main
from readchar import readkey, key       #read keys
from colorama import Fore, Back, Style  #Color for the style




#Main running code
def main():

    #Principal elements of the help text
    parser = argparse.ArgumentParser( 
                    prog=Fore.LIGHTBLUE_EX+Style.BRIGHT+'Typing Velocity Test'+Style.RESET_ALL,
                    description=Style.BRIGHT+Fore.YELLOW+'A program that executes a typing test.'+Style.RESET_ALL+' You can choose to use '
                    +Style.BRIGHT+Fore.LIGHTCYAN_EX+'time mode or number of words,'+Style.RESET_ALL+' choose the'
                    +Style.BRIGHT+Fore.LIGHTCYAN_EX+' maximum value'+Style.RESET_ALL+' and choose between'
                    +Style.BRIGHT+Fore.LIGHTCYAN_EX+' words or characters'+Style.RESET_ALL,
                    epilog=Style.BRIGHT+'Pedro Maia, Salomé Dias, Vitor Gomes. UA PSR - 23/24'+Style.RESET_ALL,
                    formatter_class=argparse.RawTextHelpFormatter)
    
    #Arguments for the program: 'time mode', 'max value' and 'use words'
    parser.add_argument('-utm',
                        '--use_time_mode', 
                        help='If'+Style.BRIGHT+Fore.LIGHTCYAN_EX+' used'+Style.RESET_ALL+', the program will run in '+Fore.YELLOW+'time mode'+Style.RESET_ALL+'\nIf '+Style.BRIGHT+Fore.LIGHTRED_EX+'ignored'+Style.RESET_ALL+', it will run in '+Fore.YELLOW+'number of inputs mode'+Style.RESET_ALL,
                        action='store_true',
                        default=False)
    parser.add_argument('-mv',
                        '--max_value',
                        type=int,
                        help='Number of seconds or number of words to be typed',
                        required='true')
    parser.add_argument('-uw',
                        '--use_words', 
                        help='If'+Style.BRIGHT+Fore.LIGHTCYAN_EX+' used'+Style.RESET_ALL+', the program will run in '+Fore.YELLOW+'words mode'+Style.RESET_ALL+'\nIf '+Style.BRIGHT+Fore.LIGHTRED_EX+'ignored'+Style.RESET_ALL+', it will run in '+Fore.YELLOW+'characters mode'+Style.RESET_ALL,
                        action='store_true',
                        default=False)
    
    #Creating the vars to store or execute the arguments
    args = vars (parser.parse_args())

    #Creating vars to readability
    timeMode = args['use_time_mode']
    maxValue = args['max_value']
    useWords = args['use_words']

    #Creating the strings to show in the introduction
    if timeMode:
        modeString='time mode'
        numberString='have a duration of '+Style.BRIGHT+Fore.LIGHTYELLOW_EX + str(maxValue) + ' seconds' +Style.RESET_ALL
    else:
        modeString='number of inputs mode'
        numberString='consist in a number of '+Style.BRIGHT+Fore.LIGHTYELLOW_EX + str(maxValue) + 'levels' +Style.RESET_ALL

    if useWords:
        modeString2=Style.BRIGHT+Fore.LIGHTCYAN_EX+'type words'+Style.RESET_ALL
    else:
        modeString2=Style.BRIGHT+Fore.LIGHTCYAN_EX+'type single characters'+Style.RESET_ALL

    #Printing the introduction of the program
    print('----------------------------------------------------------------------------')
    print(Style.BRIGHT+Fore.LIGHTGREEN_EX+ 'Initializing program in '+ modeString+Style.RESET_ALL)
    print('----------------------------------------------------------------------------')
    time.sleep(0.5)     #Making a small transition
    print(Fore.YELLOW+ 'The game will ' + numberString + Style.RESET_ALL)
    print()
    time.sleep(0.75)
    print('Your objective is to ' +modeString2 + ' the '+Fore.BLUE+Style.BRIGHT+'quickest and most correctly as possible'+Style.RESET_ALL)
    print()
    time.sleep(1)
    print('When you are ready, '+Fore.LIGHTRED_EX+Style.BRIGHT+'press [ENTER] to start the challenge'+Style.RESET_ALL)
    print()
    
    #Cicle to wait for the character and run the main program
    while True:
        k = readkey()
        if k == key.ENTER:
            runProgram(timeMode,maxValue,useWords)
            break

if __name__ == "__main__":
    main()