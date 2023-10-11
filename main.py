#!/usr/bin/env python3
#ola
#import section
import argparse #arguments
import readchar #read keys

from program_run import runProgram #function to not pollute the main
from readchar import readkey, key #read keys
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
                    epilog=Style.BRIGHT+'Pedro Maia, Salomé Dias, Vitor Gomes. UA PSR - 23/24'+Style.RESET_ALL)
    
    #Arguments for the program: 'time mode', 'max value' and 'use words'
    parser.add_argument('-utm', '--use_time_mode', help='option to use time mode insted of number of inputs (default)', action='store_true', default=False)
    parser.add_argument('-mv', '--max_value', type=int, help='number of seconds or number of words to be typed', required='true')
    parser.add_argument('-uw', '--use_words', help='Use the words mode instead of the characters (default)', action='store_true', default=False)
    
    #Creating the vars to store or execute the arguments
    args = vars (parser.parse_args())

    #Creating vars to readability
    timeMode = args['use_time_mode']
    maxValue = args['max_value']
    useWords = args['use_words']

    #Creating the strings to show in the introduction
    if timeMode:
        modeString='time mode'
        numberString='have a duration of ' + str(maxValue) + ' seconds'
    else:
        modeString='number of inputs mode'
        numberString='consist in a number of ' + str(maxValue) + 'levels'

    if useWords:
        modeString2='type words'
    else:
        modeString2='type single characters'

    #Printing the introduction of the program
    print('Initializing program in '+ modeString)
    print('The game will '+ numberString)
    print('Your objective is to ' +modeString2 + ' the quickest and most correctly as possible')
    print('When you are ready, press [ENTER] to start the challenge')
    
    #Cicle to wait for the character and run the main program
    while True:
        k = readkey()
        if k == key.ENTER:
            runProgram(timeMode,maxValue,useWords)
            break

if __name__ == "__main__":
    main()