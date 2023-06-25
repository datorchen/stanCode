"""
File: boggle.py
Name: Sean Chen
----------------------------------------
This program lets user input a 4*4 Boggle game, and returns all the answers.
"""


import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""

	"""
	letter_lst = []
	for i in range(4):
		string = input(f'{i+1} row of letters: ')
		string = string.split()
		if len(string) != 4:
			print('Illegal input')
			exit()
		for i in range(len(string)):
			if len(string[i]) != 1:
				print('Illegal input')
				exit()
			string[i] = string[i].lower()
			letter_lst.append(string[i])
	# the above checks if user input in legal format

	dic = read_dictionary()
	start = time.time()
	output = solve_boggle(letter_lst, '', dic, [], 0, [])
	end = time.time()
	print(f'There are {len(output)} words in total.')
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def solve_boggle(letter_lst, current_string, dic, used_lst, idx, output):
	if len(current_string) >= 4:
		if current_string in dic:
			if current_string not in output:
				output.append(current_string)
				print(f'Found "{current_string}"')
	for i in range(len(letter_lst)):
		if idx == 0 and used_lst == []:
			# choose
			used_lst.append(i)
			current_string += letter_lst[i]
			# explore
			if has_prefix(current_string, dic):
				solve_boggle(letter_lst, current_string, dic, used_lst, i, output)
			# unchoose
			used_lst.pop()
			current_string = current_string[:-1]
		elif idx % 4 == 0:
			if i in [idx-4, idx-3, idx+1, idx+4, idx+5]:
				if i not in used_lst:
					# choose
					used_lst.append(i)
					current_string += letter_lst[i]
					# explore
					if has_prefix(current_string, dic):
						solve_boggle(letter_lst, current_string, dic, used_lst, i, output)
					# unchoose
					used_lst.pop()
					current_string = current_string[:-1]
		elif idx % 4 == 3:
			if i in [idx-5, idx-4, idx-1, idx+3, idx+4]:
				if i not in used_lst:
					# choose
					used_lst.append(i)
					current_string += letter_lst[i]
					# explore
					if has_prefix(current_string, dic):
						solve_boggle(letter_lst, current_string, dic, used_lst, i, output)
					# unchoose
					used_lst.pop()
					current_string = current_string[:-1]
		else:
			if i in [idx-5, idx-4, idx-3, idx-1, idx+1, idx+3, idx+4, idx+5]:
				if i not in used_lst:
					# choose
					used_lst.append(i)
					current_string += letter_lst[i]
					# explore
					if has_prefix(current_string, dic):
						solve_boggle(letter_lst, current_string, dic, used_lst, i, output)
					# unchoose
					used_lst.pop()
					current_string = current_string[:-1]
	return output


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	:return: a list contains all the words in 'dictionary.txt'
	"""
	dic = {}
	f = open(FILE, 'r')
	for line in f:
		dic[line.strip()] = 0
	return dic


def has_prefix(sub_s, dic):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dic: (dict) A dictionary contains all the words to be matched
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
