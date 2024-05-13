# pseudo code
# split a word into an array
# loop over the array from both ends
# check if the arr[start] == arr[end]

import argparse

def isPalindrome(s):
    arr = tuple(s)
    print(len(arr))
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        if(arr[start] != arr[end]):
            print('False: Not a palindrome')
            return
        start = start + 1
        end = end - 1
        # print('start: ', end)
    
        
    print('IS PALINDROME')
    return
    
    
if __name__ == '__main__':
    # This code won't run if this file is imported.
    parser = argparse.ArgumentParser("mininet_topo.py <optional_args>")
    parser.add_argument('-w', '--word', type=str, help='word to be tested : ')
    # inp = input('Please enter the string : ')

    args = parser.parse_args()
    print(args)
    
    word = args.word or 'abc'
    isPalindrome(word)