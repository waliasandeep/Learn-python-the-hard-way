#Exercise 25
#I will also write function to show first and last words without popping them off 
# this program was imported after the command
#import sys 
#sys.path.append(r'C:\Users\Brandon\Experiment\Python_ex')

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words"""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word afterpopping it off"""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off"""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a dull sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words) 

def print_first_and_last(sentence):
	"""Print the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_without_popping(sentence):
	print sentence[0]

def print_last_without_popping(sentence):
	print sentence[len(sentence)-1]
"""This program will be used after importing and we can either use
import Ex25
or from Ex25 import *"""