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
	start = time.time()
	####################
	s_lst = []
	for i in range(4):
		s_row = []		# Each row of letters
		s = input(f'{i+1} row of letters: ').lower()
		if check(s):
			for ch in s:
				if ch.isalpha():
					s_row.append(ch)
			s_lst.append(s_row)
		else:
			print('Illegal input')
			break
	if len(s_lst) == 4:
		find_words(s_lst, dic)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


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
			if i % 2 == 1 and s[i] != ' ':			# If no space between each letter
				return False
			elif i % 2 == 0 and s[i].isspace():		# If less than 4 letters but with many spaces
				return False
		return True


def find_words(s_lst, dic):
	"""
	This function loops through all the letters input by user,
	and prints out total number of words found.

	:param s_lst: list[list[str]], a list containing lists of letters (rows of letters) input by user
	:param dic: list, a list containing all words

	:return: This function does not return any value
	"""
	ans_lst = []
	for row in range(len(s_lst)):
		for col in range(len(s_lst[row])):
			helper(s_lst, row, col, '', ans_lst, [], dic)
	print(f'There are {len(ans_lst)} words in total.')


def helper(s_lst, r, c, ans, ans_lst, path, dic):
	"""
	This function recursively finds out all words constructed from
	sequentially neighboring letter cubes and prints the found words.

	:param s_lst: list[list[str]], a list containing lists of letters (rows of letters) input by user
	:param r: int, the row number of the letter cube
	:param c: int, the position of the letter cube in the row
	:param ans: str, words that are found
	:param ans_lst: list, a list containing all found words
	:param path: list, a list containing position coordinates that have been visited
	:param dic: list, a list containing all words

	:return: This function does not return any value
	"""
	if ans in dic and len(ans) >= 4 and ans not in ans_lst:
		print(f'Found: {ans}')
		ans_lst.append(ans)
	if r < 0 or r == len(s_lst) or c < 0 or c == len(s_lst[0]) or [r, c] in path:
		return
	path.append([r, c])					# Record the coordinates
	ans += s_lst[r][c]					# Choose
	if has_prefix(ans, dic):			# Explore
		for move_r in range(-1, 2):		# Find neighboring letters
			for move_c in range(-1, 2):
				neighbor_r = move_r + r
				neighbor_c = move_c + c
				helper(s_lst, neighbor_r, neighbor_c, ans, ans_lst, path, dic)
	# Un-choose
	ans = ans[:-1]
	path.pop()


def has_prefix(sub_s, dic):
	"""
	This function checks if there are any words that start with sub_s.

	:param sub_s: str, a substring that is constructed by neighboring letters on a 4x4 square grid
	:param dic: list, a list containing all words

	:return: bool, if there are any words with prefix stored in sub_s
	"""
	for voc in dic:
		if voc.startswith(sub_s):
			return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dic = []
	with open('dictionary.txt', 'r') as f:
		for line in f:
			dic.append(line.strip())
	return dic


if __name__ == '__main__':
	main()
