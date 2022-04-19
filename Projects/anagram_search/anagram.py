"""
File: anagram.py
Name: Hui-Chieh Chen
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This program finds out all the anagram(s) for the input word
    """
    dic = read_dictionary()
    print("Welcome to stanCode \"Anagram Generator\" (or" + EXIT + "to quit)")
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        start = time.time()
        find_anagrams(s, dic)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    Reads the information from the specified file and stores all the data in dic.

    :return: dic (lst), a list containing all words
    """
    dic = []
    with open(FILE, 'r') as f:
        for line in f:
            dic.append(line.strip())
    return dic


def find_anagrams(s, dic):
    """
    This function prints out a list of all anagrams of the input word.

    :param s: str, the word input by user
    :param dic: lst, a list containing all words

    :return: This function does not return any value.
    """
    print('Searching...')
    ans_lst = find_anagrams_helper(s, '', [], dic)
    print(f'{len(ans_lst)} anagrams: {ans_lst}')


def find_anagrams_helper(s, ans, ans_lst, dic):
    """
    This function recursively finds out all anagrams of the input word and
    prints out the anagram(s) individually.

    :param s: str, the word input by user
    :param ans: str, anagram(s) of the input word
    :param ans_lst: lst, a list containing all anagram(s) of the input word
    :param dic: lst, a list containing all words
    :return ans_lst: a list that contains all anagram(s) of the input word
    """
    if len(ans) == len(s) and ans not in ans_lst:
        ans_lst.append(ans)
        print('Found: '+ans)
        print('Searching...')
    else:
        for ch in s:
            if ans.count(ch) == s.count(ch):
                pass
            else:
                # Choose
                ans += ch
                # Explore
                sub_dic = has_prefix(s, ans, dic)
                if sub_dic:         # If the sub_dic is not empty
                    find_anagrams_helper(s, ans, ans_lst, sub_dic)
                # Un-choose
                ans = ans[:-1]
    return ans_lst


def has_prefix(s, sub_s, sub_dic):
    """
    This function narrows down the range of dic that will be searched.

    :param s: str, the word input by user
    :param sub_s: str, substring of an attempted answer
    :param sub_dic: lst, a list containing all words that start with the previous sub_s
    :return: lst, a list containing all words that start with the current sub_s and are not longer than the input word
    """
    temp_dic = []
    for voc in sub_dic:
        if voc.startswith(sub_s) and len(voc) == len(s):
            temp_dic.append(voc)
    return temp_dic


if __name__ == '__main__':
    main()
