"""
File: boggle.py
Name: Hui-Chieh Chen
----------------------------------------
This program imitates the word game "Boggle".
User is asked to enter 4 rows of letters, each row contains 4 letters,
which can be viewed as a 4x4 square grids.

This program searches for all words that can be constructed from the
letters of sequentially adjacent cubes, where adjacent cubes are those
horizontally, vertically, and diagonally neighboring.
Each word must have at least 4 letters, and each letter cube can be
used only once per word.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    This program finds out all words that are formed by sequentially
    adjacent letter cubes in the 4 rows of letters input by user,
    and shows total number of words found
    """
    dic = read_dictionary()
    board = []
    for i in range(1, 5):
        b_row = []      # Each row of letters
        s = input(f'{i} row of letters: ').lower()
        if check(s):
            for ch in s:
                if ch.isalpha():
                    b_row.append(ch)
            board.append(b_row)
        else:
            print('Illegal input')
            break
    start = time.time()
    if len(board) == 4:
        find_words(board, dic)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_words(board, dic):
    """
    This function loops through all the letters input by user,
    and prints out total number of words found.

    :param board: list[list[str]], a list containing lists of letters (rows of letters) input by user
    :param dic: list, a list containing all words

    :return: This function does not return any value
    """
    ans_lst = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            helper(board, row, col, '', ans_lst, [], dic)
    print(f'There are {len(ans_lst)} words in total.')


def helper(board, r, c, ans, ans_lst, path, dic):
    """
    This function recursively finds out all words constructed from
    sequentially neighboring letter cubes and prints the found words.

    :param board: list[list[str]], a list containing lists of letters (rows of letters) input by user
    :param r: int, the row number of the letter cube on the 4x4 board
    :param c: int, the position of the letter cube in the row
    :param ans: str, words that are found
    :param ans_lst: list, a list containing all found words
    :param path: list, a list containing position coordinates that have been visited
    :param dic: list, a list containing all words

    :return: This function does not return any value
    """
    if ans in dic and ans not in ans_lst:
        print(f'Found: {ans}')
        ans_lst.append(ans)
    if r < 0 or r == len(board) or c < 0 or c == len(board[0]) or [r, c] in path:
        return
    path.append([r, c])                     # Record the coordinates
    ans += board[r][c]                      # Choose
    sub_dic = has_prefix(ans, dic)          # Explore
    if sub_dic:
        for move_r in range(-1, 2):         # Find neighboring letters
            for move_c in range(-1, 2):
                n_r = move_r + r
                n_c = move_c + c
                helper(board, n_r, n_c, ans, ans_lst, path, sub_dic)
    # Un-choose
    ans = ans[:-1]
    path.pop()


def has_prefix(sub_s, sub_dic):
    """
    This function checks if there are any words that start with sub_s and
    narrows down the range of dic that will be searched.

    :param sub_s: str, a substring that is constructed by neighboring letters on a 4x4 square grid
    :param sub_dic: list, a list containing all searchable words

    :return: list, a list containing all words that start with sub_s and have at least 4 letters
    """
    temp = []
    for voc in sub_dic:
        if voc.startswith(sub_s) and len(voc) >= 4:
            temp.append(voc)
    return temp


def check(s):
    """
    This function checks if input follow the rules:
    1. contains 4 letters
    2. there is a space between each letter

    :param s: str, a row of letters input by user
    :return: bool, if input meets the rules
    """
    if len(s) < 7:
        return False
    elif 7 <= len(s) <= 8:
        for i in range(len(s)):
            if i % 2 == 1 and s[i] != ' ':        # If no space between each letter
                return False
            elif i % 2 == 0 and s[i] == ' ':      # If less than 4 letters but with many spaces
                return False
        return True


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list

    :return: list, a list containing all words
    """
    dic = []
    with open('dictionary.txt', 'r') as f:
        for line in f:
            dic.append(line.strip())
    return dic


if __name__ == '__main__':
    main()