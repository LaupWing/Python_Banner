import pyperclip
import sys


def main():   
    flag = True
    try:
        if(len(sys.argv) < 3):
            raise ValueError()
        offset = int(sys.argv[1])
        symbol = sys.argv[2]

        if(len(symbol)>1):
            raise Exception()

    except ValueError:
        print('Provide a number as first and symbol as second argument please')
        return
    except:
        print('Symbol cant be more than 1')
        return


    while flag:
        confirmation = input(f'Your offset={offset} and symbol={symbol} (c)onfirm (x)cancel?: ')
        if confirmation == 'c' or confirmation == 'x':
            if confirmation == 'c':
                print('hey')
            else:
                print('Provide your desire offset again by running the script with the appropriate offset')
            flag = False

main()