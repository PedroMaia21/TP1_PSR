#!/usr/bin/env python3

#import section
import argparse

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

if __name__ == "__main__":
    main()