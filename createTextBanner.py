import pyperclip
import sys
import math

def main():   
    flag = True
    try:
        if(len(sys.argv) < 3):
            raise Exception('Provide a number as first and symbol as second argument please')

        value = pyperclip.paste().split('\n')
        offset = int(sys.argv[1])
        symbol = sys.argv[2]
        
        if(len(value) < 1):
            raise Exception('Copy your message please!')

        if(len(symbol)>1):
            raise Exception('Symbol cant be more than 1')
        
    except Exception as e:
        print(e)
        return

    while flag:
        confirmation = input(f'Your offset={offset} and symbol={symbol} (c)onfirm (x)cancel?: ')
        if confirmation == 'c' or confirmation == 'x':
            if confirmation == 'c':
                createBanner(value, offset, symbol)
                # print(longestVal)
            else:
                print('Provide your desire offset again by running the script with the appropriate offset')
            flag = False


def createBanner(value, offset, symbol):
    max_length = len(max(value, key=len)) + (2*int(offset))
    new_strings = [add_offset(x, max_length) for x in value]
    # print(f'''
    # {symbol*max_length}
    # '''.strip())
    print(new_strings)

def add_offset(val, max_length):
    offset = (max_length - len(val))/2 
    print(offset)
    if not offset.is_integer():
        first_part = math.ceil(offset) 
        second_part = math.floor(offset)
        return (' '*first_part) + val + (' '* second_part)
    return (' ' * int(offset)) + val + (' '* int(offset))


# print(sys.argv)
main()
# value = pyperclip.paste()
# print(value.split('\n'))