#!/usr/bin/env python3

#import section
import argparse
import readchar

from program_run import runProgram
from readchar import readkey, key

#Main running code
def main():
    #Principal elements of the help text
    parser = argparse.ArgumentParser( 
                    prog='Typing Velocity Test',
                    description='A program that executes a typing test. You can choose to use time mode or number of words, choose the maximum value and choose between words or characters',
                    epilog='Pedro Maia, Salomé Dias, Vitor Gomes. UA PSR - 23/24')
    
    #Arguments for the program: 'time mode', 'max value' and 'use words'
    parser.add_argument('-utm', '--use_time_mode', type=bool, help='option to use time mode insted of number of inputs (default)')
    parser.add_argument('-mv', '--max_value', type=int, help='number of seconds or number of words to be typed', required='true')
    parser.add_argument('-uw', '--use_words', type=bool, help='Use the words mode instead of the characters (default)')
    
    #Create the vars to store or execute the arguments
    args = vars (parser.parse_args())

    if args['use_time_mode']:
        modeString='time mode'
        numberString='have a duration of ' + str(args['max_value']) + ' seconds'
    else:
        modeString='number of inputs mode'
        numberString='consist in a number of ' + str(args['max_value']) + 'levels'

    if args['use_words']:
        modeString2='type words'
    else:
        modeString2='type single characters'

    print('Initializing program in '+ modeString)
    print('The game will '+ numberString)
    print('Your objective is to ' +modeString2 + ' the quickest and most correctly as possible')
    print('When you are ready, press [ENTER] to start the challenge')
    
    while True:
        k = readkey()
        if k==key.ENTER:
            runProgram()

if __name__ == "__main__":
    main()