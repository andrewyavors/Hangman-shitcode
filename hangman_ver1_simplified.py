import os

word = ""
loser = False
_ = os.system('cls' if os.name=='nt' else 'clear')
while not word.isalpha() :
	word = input("Hi, Player 1! It's a game 'Hangman'! Write your word below:\n(Note that word must be between 4 and 8 letters & without spaces!)\n")
_ = os.system('cls' if os.name=='nt' else 'clear')
print("Hi, Player 2! it's a game 'Hangman'! This is the word you need to guess:\n")

if len(word) == 4 :
	toGuess = str(word[0]) + "__" + str(word[3])
	numberOfErrors = 0
	wrongChars=""
	print("\t___________")
	print("\t|         |")
	print("\t|")
	print("\t|")
	print("\t|")
	print("\t|")
	print("\t|")
	print("\n\tWord: " + toGuess)
	print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if not "_" in toGuess :
		print("\nCONGRATULATIONS! You win!!!")

if len(word) == 5 :
	toGuess = str(word[0]) + "___" + str(word[4])
	numberOfErrors = 0
	wrongChars=""
	print("\t___________")
	print("\t|         |")
	print("\t|")
	print("\t|")
	print("\t|")
	print("\t|")
	print("\t|")
	print("\n\tWord: " + toGuess)
	print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if not "_" in toGuess :
		print("\nCONGRATULATIONS! You win!!!")

if len(word) == 6 :
	toGuess = str(word[0]) + "____" + str(word[5])
	numberOfErrors = 0
	wrongChars=""
	print("\t___________")
	print("\t|         |")
	print("\t|")
	print("\t|")
	print("\t|")
	print("\t|")
	print("\t|")
	print("\n\tWord: " + toGuess)
	print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if not "_" in toGuess :
		print("\nCONGRATULATIONS! You win!!!")

if len(word) == 7 :
	toGuess = str(word[0]) + "_____" + str(word[6])
	numberOfErrors = 0
	wrongChars=""
	print("\t___________")
	print("\t|         |")
	print("\t|")
	print("\t|")
	print("\t|")
	print("\t|")
	print("\t|")
	print("\n\tWord: " + toGuess)
	print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if not "_" in toGuess :
		print("\nCONGRATULATIONS! You win!!!")

if len(word) == 8 :
	toGuess = str(word[0]) + "______" + str(word[7])
	numberOfErrors = 0
	wrongChars=""
	print("\t___________")
	print("\t|         |")
	print("\t|")
	print("\t|")
	print("\t|")
	print("\t|")
	print("\t|")
	print("\n\tWord: " + toGuess)
	print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[6] == "A" or word[6] == "a" :
				toGuess = toGuess[:6] + "a" + toGuess[7:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" and word[6] != "A" and word[6] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[6] == "B" or word[6] == "b" :
				toGuess = toGuess[:6] + "b" + toGuess[7:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" and word[6] != "B" and word[6] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[6] == "C" or word[6] == "c" :
				toGuess = toGuess[:6] + "c" + toGuess[7:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" and word[6] != "C" and word[6] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[6] == "D" or word[6] == "d" :
				toGuess = toGuess[:6] + "d" + toGuess[7:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" and word[6] != "D" and word[6] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[6] == "E" or word[6] == "e" :
				toGuess = toGuess[:6] + "e" + toGuess[7:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" and word[6] != "E" and word[6] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[6] == "F" or word[6] == "f" :
				toGuess = toGuess[:6] + "f" + toGuess[7:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" and word[6] != "F" and word[6] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[6] == "G" or word[6] == "g" :
				toGuess = toGuess[:6] + "g" + toGuess[7:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" and word[6] != "G" and word[6] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[6] == "H" or word[6] == "h" :
				toGuess = toGuess[:6] + "h" + toGuess[7:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" and word[6] != "H" and word[6] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[6] == "I" or word[6] == "i" :
				toGuess = toGuess[:6] + "i" + toGuess[7:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" and word[6] != "I" and word[6] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[6] == "J" or word[6] == "j" :
				toGuess = toGuess[:6] + "j" + toGuess[7:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" and word[6] != "J" and word[6] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[6] == "K" or word[6] == "k" :
				toGuess = toGuess[:6] + "k" + toGuess[7:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" and word[6] != "K" and word[6] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[6] == "L" or word[6] == "l" :
				toGuess = toGuess[:6] + "l" + toGuess[7:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" and word[6] != "L" and word[6] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[6] == "M" or word[6] == "m" :
				toGuess = toGuess[:6] + "m" + toGuess[7:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" and word[6] != "M" and word[6] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[6] == "N" or word[6] == "n" :
				toGuess = toGuess[:6] + "n" + toGuess[7:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" and word[6] != "N" and word[6] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[6] == "O" or word[6] == "o" :
				toGuess = toGuess[:6] + "o" + toGuess[7:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" and word[6] != "O" and word[6] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[6] == "P" or word[6] == "p" :
				toGuess = toGuess[:6] + "p" + toGuess[7:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" and word[6] != "P" and word[6] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[6] == "Q" or word[6] == "q" :
				toGuess = toGuess[:6] + "q" + toGuess[7:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" and word[6] != "Q" and word[6] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[6] == "R" or word[6] == "r" :
				toGuess = toGuess[:6] + "r" + toGuess[7:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" and word[6] != "R" and word[6] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[6] == "S" or word[6] == "s" :
				toGuess = toGuess[:6] + "s" + toGuess[7:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" and word[6] != "S" and word[6] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[6] == "T" or word[6] == "t" :
				toGuess = toGuess[:6] + "t" + toGuess[7:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" and word[6] != "T" and word[6] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[6] == "U" or word[6] == "u" :
				toGuess = toGuess[:6] + "u" + toGuess[7:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" and word[6] != "U" and word[6] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[6] == "V" or word[6] == "v" :
				toGuess = toGuess[:6] + "v" + toGuess[7:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" and word[6] != "V" and word[6] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[6] == "W" or word[6] == "w" :
				toGuess = toGuess[:6] + "w" + toGuess[7:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" and word[6] != "W" and word[6] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[6] == "X" or word[6] == "x" :
				toGuess = toGuess[:6] + "x" + toGuess[7:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" and word[6] != "X" and word[6] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[6] == "Y" or word[6] == "y" :
				toGuess = toGuess[:6] + "y" + toGuess[7:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" and word[6] != "Y" and word[6] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[6] == "Z" or word[6] == "z" :
				toGuess = toGuess[:6] + "z" + toGuess[7:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" and word[6] != "Z" and word[6] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[6] == "A" or word[6] == "a" :
				toGuess = toGuess[:6] + "a" + toGuess[7:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" and word[6] != "A" and word[6] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[6] == "B" or word[6] == "b" :
				toGuess = toGuess[:6] + "b" + toGuess[7:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" and word[6] != "B" and word[6] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[6] == "C" or word[6] == "c" :
				toGuess = toGuess[:6] + "c" + toGuess[7:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" and word[6] != "C" and word[6] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[6] == "D" or word[6] == "d" :
				toGuess = toGuess[:6] + "d" + toGuess[7:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" and word[6] != "D" and word[6] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[6] == "E" or word[6] == "e" :
				toGuess = toGuess[:6] + "e" + toGuess[7:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" and word[6] != "E" and word[6] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[6] == "F" or word[6] == "f" :
				toGuess = toGuess[:6] + "f" + toGuess[7:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" and word[6] != "F" and word[6] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[6] == "G" or word[6] == "g" :
				toGuess = toGuess[:6] + "g" + toGuess[7:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" and word[6] != "G" and word[6] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[6] == "H" or word[6] == "h" :
				toGuess = toGuess[:6] + "h" + toGuess[7:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" and word[6] != "H" and word[6] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[6] == "I" or word[6] == "i" :
				toGuess = toGuess[:6] + "i" + toGuess[7:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" and word[6] != "I" and word[6] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[6] == "J" or word[6] == "j" :
				toGuess = toGuess[:6] + "j" + toGuess[7:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" and word[6] != "J" and word[6] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[6] == "K" or word[6] == "k" :
				toGuess = toGuess[:6] + "k" + toGuess[7:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" and word[6] != "K" and word[6] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[6] == "L" or word[6] == "l" :
				toGuess = toGuess[:6] + "l" + toGuess[7:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" and word[6] != "L" and word[6] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[6] == "M" or word[6] == "m" :
				toGuess = toGuess[:6] + "m" + toGuess[7:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" and word[6] != "M" and word[6] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[6] == "N" or word[6] == "n" :
				toGuess = toGuess[:6] + "n" + toGuess[7:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" and word[6] != "N" and word[6] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[6] == "O" or word[6] == "o" :
				toGuess = toGuess[:6] + "o" + toGuess[7:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" and word[6] != "O" and word[6] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[6] == "P" or word[6] == "p" :
				toGuess = toGuess[:6] + "p" + toGuess[7:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" and word[6] != "P" and word[6] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[6] == "Q" or word[6] == "q" :
				toGuess = toGuess[:6] + "q" + toGuess[7:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" and word[6] != "Q" and word[6] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[6] == "R" or word[6] == "r" :
				toGuess = toGuess[:6] + "r" + toGuess[7:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" and word[6] != "R" and word[6] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[6] == "S" or word[6] == "s" :
				toGuess = toGuess[:6] + "s" + toGuess[7:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" and word[6] != "S" and word[6] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[6] == "T" or word[6] == "t" :
				toGuess = toGuess[:6] + "t" + toGuess[7:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" and word[6] != "T" and word[6] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[6] == "U" or word[6] == "u" :
				toGuess = toGuess[:6] + "u" + toGuess[7:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" and word[6] != "U" and word[6] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[6] == "V" or word[6] == "v" :
				toGuess = toGuess[:6] + "v" + toGuess[7:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" and word[6] != "V" and word[6] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[6] == "W" or word[6] == "w" :
				toGuess = toGuess[:6] + "w" + toGuess[7:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" and word[6] != "W" and word[6] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[6] == "X" or word[6] == "x" :
				toGuess = toGuess[:6] + "x" + toGuess[7:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" and word[6] != "X" and word[6] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[6] == "Y" or word[6] == "y" :
				toGuess = toGuess[:6] + "y" + toGuess[7:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" and word[6] != "Y" and word[6] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[6] == "Z" or word[6] == "z" :
				toGuess = toGuess[:6] + "z" + toGuess[7:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" and word[6] != "Z" and word[6] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[6] == "A" or word[6] == "a" :
				toGuess = toGuess[:6] + "a" + toGuess[7:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" and word[6] != "A" and word[6] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[6] == "B" or word[6] == "b" :
				toGuess = toGuess[:6] + "b" + toGuess[7:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" and word[6] != "B" and word[6] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[6] == "C" or word[6] == "c" :
				toGuess = toGuess[:6] + "c" + toGuess[7:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" and word[6] != "C" and word[6] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[6] == "D" or word[6] == "d" :
				toGuess = toGuess[:6] + "d" + toGuess[7:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" and word[6] != "D" and word[6] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[6] == "E" or word[6] == "e" :
				toGuess = toGuess[:6] + "e" + toGuess[7:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" and word[6] != "E" and word[6] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[6] == "F" or word[6] == "f" :
				toGuess = toGuess[:6] + "f" + toGuess[7:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" and word[6] != "F" and word[6] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[6] == "G" or word[6] == "g" :
				toGuess = toGuess[:6] + "g" + toGuess[7:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" and word[6] != "G" and word[6] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[6] == "H" or word[6] == "h" :
				toGuess = toGuess[:6] + "h" + toGuess[7:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" and word[6] != "H" and word[6] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[6] == "I" or word[6] == "i" :
				toGuess = toGuess[:6] + "i" + toGuess[7:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" and word[6] != "I" and word[6] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[6] == "J" or word[6] == "j" :
				toGuess = toGuess[:6] + "j" + toGuess[7:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" and word[6] != "J" and word[6] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[6] == "K" or word[6] == "k" :
				toGuess = toGuess[:6] + "k" + toGuess[7:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" and word[6] != "K" and word[6] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[6] == "L" or word[6] == "l" :
				toGuess = toGuess[:6] + "l" + toGuess[7:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" and word[6] != "L" and word[6] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[6] == "M" or word[6] == "m" :
				toGuess = toGuess[:6] + "m" + toGuess[7:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" and word[6] != "M" and word[6] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[6] == "N" or word[6] == "n" :
				toGuess = toGuess[:6] + "n" + toGuess[7:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" and word[6] != "N" and word[6] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[6] == "O" or word[6] == "o" :
				toGuess = toGuess[:6] + "o" + toGuess[7:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" and word[6] != "O" and word[6] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[6] == "P" or word[6] == "p" :
				toGuess = toGuess[:6] + "p" + toGuess[7:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" and word[6] != "P" and word[6] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[6] == "Q" or word[6] == "q" :
				toGuess = toGuess[:6] + "q" + toGuess[7:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" and word[6] != "Q" and word[6] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[6] == "R" or word[6] == "r" :
				toGuess = toGuess[:6] + "r" + toGuess[7:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" and word[6] != "R" and word[6] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[6] == "S" or word[6] == "s" :
				toGuess = toGuess[:6] + "s" + toGuess[7:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" and word[6] != "S" and word[6] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[6] == "T" or word[6] == "t" :
				toGuess = toGuess[:6] + "t" + toGuess[7:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" and word[6] != "T" and word[6] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[6] == "U" or word[6] == "u" :
				toGuess = toGuess[:6] + "u" + toGuess[7:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" and word[6] != "U" and word[6] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[6] == "V" or word[6] == "v" :
				toGuess = toGuess[:6] + "v" + toGuess[7:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" and word[6] != "V" and word[6] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[6] == "W" or word[6] == "w" :
				toGuess = toGuess[:6] + "w" + toGuess[7:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" and word[6] != "W" and word[6] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[6] == "X" or word[6] == "x" :
				toGuess = toGuess[:6] + "x" + toGuess[7:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" and word[6] != "X" and word[6] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[6] == "Y" or word[6] == "y" :
				toGuess = toGuess[:6] + "y" + toGuess[7:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" and word[6] != "Y" and word[6] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[6] == "Z" or word[6] == "z" :
				toGuess = toGuess[:6] + "z" + toGuess[7:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" and word[6] != "Z" and word[6] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[6] == "A" or word[6] == "a" :
				toGuess = toGuess[:6] + "a" + toGuess[7:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" and word[6] != "A" and word[6] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[6] == "B" or word[6] == "b" :
				toGuess = toGuess[:6] + "b" + toGuess[7:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" and word[6] != "B" and word[6] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[6] == "C" or word[6] == "c" :
				toGuess = toGuess[:6] + "c" + toGuess[7:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" and word[6] != "C" and word[6] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[6] == "D" or word[6] == "d" :
				toGuess = toGuess[:6] + "d" + toGuess[7:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" and word[6] != "D" and word[6] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[6] == "E" or word[6] == "e" :
				toGuess = toGuess[:6] + "e" + toGuess[7:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" and word[6] != "E" and word[6] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[6] == "F" or word[6] == "f" :
				toGuess = toGuess[:6] + "f" + toGuess[7:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" and word[6] != "F" and word[6] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[6] == "G" or word[6] == "g" :
				toGuess = toGuess[:6] + "g" + toGuess[7:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" and word[6] != "G" and word[6] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[6] == "H" or word[6] == "h" :
				toGuess = toGuess[:6] + "h" + toGuess[7:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" and word[6] != "H" and word[6] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[6] == "I" or word[6] == "i" :
				toGuess = toGuess[:6] + "i" + toGuess[7:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" and word[6] != "I" and word[6] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[6] == "J" or word[6] == "j" :
				toGuess = toGuess[:6] + "j" + toGuess[7:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" and word[6] != "J" and word[6] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[6] == "K" or word[6] == "k" :
				toGuess = toGuess[:6] + "k" + toGuess[7:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" and word[6] != "K" and word[6] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[6] == "L" or word[6] == "l" :
				toGuess = toGuess[:6] + "l" + toGuess[7:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" and word[6] != "L" and word[6] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[6] == "M" or word[6] == "m" :
				toGuess = toGuess[:6] + "m" + toGuess[7:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" and word[6] != "M" and word[6] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[6] == "N" or word[6] == "n" :
				toGuess = toGuess[:6] + "n" + toGuess[7:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" and word[6] != "N" and word[6] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[6] == "O" or word[6] == "o" :
				toGuess = toGuess[:6] + "o" + toGuess[7:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" and word[6] != "O" and word[6] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[6] == "P" or word[6] == "p" :
				toGuess = toGuess[:6] + "p" + toGuess[7:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" and word[6] != "P" and word[6] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[6] == "Q" or word[6] == "q" :
				toGuess = toGuess[:6] + "q" + toGuess[7:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" and word[6] != "Q" and word[6] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[6] == "R" or word[6] == "r" :
				toGuess = toGuess[:6] + "r" + toGuess[7:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" and word[6] != "R" and word[6] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[6] == "S" or word[6] == "s" :
				toGuess = toGuess[:6] + "s" + toGuess[7:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" and word[6] != "S" and word[6] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[6] == "T" or word[6] == "t" :
				toGuess = toGuess[:6] + "t" + toGuess[7:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" and word[6] != "T" and word[6] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[6] == "U" or word[6] == "u" :
				toGuess = toGuess[:6] + "u" + toGuess[7:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" and word[6] != "U" and word[6] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[6] == "V" or word[6] == "v" :
				toGuess = toGuess[:6] + "v" + toGuess[7:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" and word[6] != "V" and word[6] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[6] == "W" or word[6] == "w" :
				toGuess = toGuess[:6] + "w" + toGuess[7:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" and word[6] != "W" and word[6] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[6] == "X" or word[6] == "x" :
				toGuess = toGuess[:6] + "x" + toGuess[7:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" and word[6] != "X" and word[6] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[6] == "Y" or word[6] == "y" :
				toGuess = toGuess[:6] + "y" + toGuess[7:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" and word[6] != "Y" and word[6] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[6] == "Z" or word[6] == "z" :
				toGuess = toGuess[:6] + "z" + toGuess[7:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" and word[6] != "Z" and word[6] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[6] == "A" or word[6] == "a" :
				toGuess = toGuess[:6] + "a" + toGuess[7:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" and word[6] != "A" and word[6] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[6] == "B" or word[6] == "b" :
				toGuess = toGuess[:6] + "b" + toGuess[7:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" and word[6] != "B" and word[6] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[6] == "C" or word[6] == "c" :
				toGuess = toGuess[:6] + "c" + toGuess[7:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" and word[6] != "C" and word[6] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[6] == "D" or word[6] == "d" :
				toGuess = toGuess[:6] + "d" + toGuess[7:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" and word[6] != "D" and word[6] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[6] == "E" or word[6] == "e" :
				toGuess = toGuess[:6] + "e" + toGuess[7:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" and word[6] != "E" and word[6] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[6] == "F" or word[6] == "f" :
				toGuess = toGuess[:6] + "f" + toGuess[7:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" and word[6] != "F" and word[6] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[6] == "G" or word[6] == "g" :
				toGuess = toGuess[:6] + "g" + toGuess[7:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" and word[6] != "G" and word[6] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[6] == "H" or word[6] == "h" :
				toGuess = toGuess[:6] + "h" + toGuess[7:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" and word[6] != "H" and word[6] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[6] == "I" or word[6] == "i" :
				toGuess = toGuess[:6] + "i" + toGuess[7:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" and word[6] != "I" and word[6] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[6] == "J" or word[6] == "j" :
				toGuess = toGuess[:6] + "j" + toGuess[7:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" and word[6] != "J" and word[6] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[6] == "K" or word[6] == "k" :
				toGuess = toGuess[:6] + "k" + toGuess[7:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" and word[6] != "K" and word[6] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[6] == "L" or word[6] == "l" :
				toGuess = toGuess[:6] + "l" + toGuess[7:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" and word[6] != "L" and word[6] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[6] == "M" or word[6] == "m" :
				toGuess = toGuess[:6] + "m" + toGuess[7:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" and word[6] != "M" and word[6] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[6] == "N" or word[6] == "n" :
				toGuess = toGuess[:6] + "n" + toGuess[7:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" and word[6] != "N" and word[6] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[6] == "O" or word[6] == "o" :
				toGuess = toGuess[:6] + "o" + toGuess[7:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" and word[6] != "O" and word[6] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[6] == "P" or word[6] == "p" :
				toGuess = toGuess[:6] + "p" + toGuess[7:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" and word[6] != "P" and word[6] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[6] == "Q" or word[6] == "q" :
				toGuess = toGuess[:6] + "q" + toGuess[7:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" and word[6] != "Q" and word[6] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[6] == "R" or word[6] == "r" :
				toGuess = toGuess[:6] + "r" + toGuess[7:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" and word[6] != "R" and word[6] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[6] == "S" or word[6] == "s" :
				toGuess = toGuess[:6] + "s" + toGuess[7:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" and word[6] != "S" and word[6] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[6] == "T" or word[6] == "t" :
				toGuess = toGuess[:6] + "t" + toGuess[7:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" and word[6] != "T" and word[6] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[6] == "U" or word[6] == "u" :
				toGuess = toGuess[:6] + "u" + toGuess[7:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" and word[6] != "U" and word[6] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[6] == "V" or word[6] == "v" :
				toGuess = toGuess[:6] + "v" + toGuess[7:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" and word[6] != "V" and word[6] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[6] == "W" or word[6] == "w" :
				toGuess = toGuess[:6] + "w" + toGuess[7:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" and word[6] != "W" and word[6] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[6] == "X" or word[6] == "x" :
				toGuess = toGuess[:6] + "x" + toGuess[7:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" and word[6] != "X" and word[6] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[6] == "Y" or word[6] == "y" :
				toGuess = toGuess[:6] + "y" + toGuess[7:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" and word[6] != "Y" and word[6] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[6] == "Z" or word[6] == "z" :
				toGuess = toGuess[:6] + "z" + toGuess[7:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" and word[6] != "Z" and word[6] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		print("\n\tWord: " + toGuess)
		print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[6] == "A" or word[6] == "a" :
				toGuess = toGuess[:6] + "a" + toGuess[7:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" and word[6] != "A" and word[6] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[6] == "B" or word[6] == "b" :
				toGuess = toGuess[:6] + "b" + toGuess[7:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" and word[6] != "B" and word[6] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[6] == "C" or word[6] == "c" :
				toGuess = toGuess[:6] + "c" + toGuess[7:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" and word[6] != "C" and word[6] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[6] == "D" or word[6] == "d" :
				toGuess = toGuess[:6] + "d" + toGuess[7:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" and word[6] != "D" and word[6] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[6] == "E" or word[6] == "e" :
				toGuess = toGuess[:6] + "e" + toGuess[7:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" and word[6] != "E" and word[6] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[6] == "F" or word[6] == "f" :
				toGuess = toGuess[:6] + "f" + toGuess[7:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" and word[6] != "F" and word[6] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[6] == "G" or word[6] == "g" :
				toGuess = toGuess[:6] + "g" + toGuess[7:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" and word[6] != "G" and word[6] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[6] == "H" or word[6] == "h" :
				toGuess = toGuess[:6] + "h" + toGuess[7:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" and word[6] != "H" and word[6] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[6] == "I" or word[6] == "i" :
				toGuess = toGuess[:6] + "i" + toGuess[7:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" and word[6] != "I" and word[6] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[6] == "J" or word[6] == "j" :
				toGuess = toGuess[:6] + "j" + toGuess[7:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" and word[6] != "J" and word[6] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[6] == "K" or word[6] == "k" :
				toGuess = toGuess[:6] + "k" + toGuess[7:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" and word[6] != "K" and word[6] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[6] == "L" or word[6] == "l" :
				toGuess = toGuess[:6] + "l" + toGuess[7:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" and word[6] != "L" and word[6] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[6] == "M" or word[6] == "m" :
				toGuess = toGuess[:6] + "m" + toGuess[7:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" and word[6] != "M" and word[6] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[6] == "N" or word[6] == "n" :
				toGuess = toGuess[:6] + "n" + toGuess[7:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" and word[6] != "N" and word[6] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[6] == "O" or word[6] == "o" :
				toGuess = toGuess[:6] + "o" + toGuess[7:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" and word[6] != "O" and word[6] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[6] == "P" or word[6] == "p" :
				toGuess = toGuess[:6] + "p" + toGuess[7:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" and word[6] != "P" and word[6] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[6] == "Q" or word[6] == "q" :
				toGuess = toGuess[:6] + "q" + toGuess[7:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" and word[6] != "Q" and word[6] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[6] == "R" or word[6] == "r" :
				toGuess = toGuess[:6] + "r" + toGuess[7:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" and word[6] != "R" and word[6] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[6] == "S" or word[6] == "s" :
				toGuess = toGuess[:6] + "s" + toGuess[7:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" and word[6] != "S" and word[6] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[6] == "T" or word[6] == "t" :
				toGuess = toGuess[:6] + "t" + toGuess[7:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" and word[6] != "T" and word[6] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[6] == "U" or word[6] == "u" :
				toGuess = toGuess[:6] + "u" + toGuess[7:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" and word[6] != "U" and word[6] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[6] == "V" or word[6] == "v" :
				toGuess = toGuess[:6] + "v" + toGuess[7:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" and word[6] != "V" and word[6] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[6] == "W" or word[6] == "w" :
				toGuess = toGuess[:6] + "w" + toGuess[7:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" and word[6] != "W" and word[6] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[6] == "X" or word[6] == "x" :
				toGuess = toGuess[:6] + "x" + toGuess[7:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" and word[6] != "X" and word[6] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[6] == "Y" or word[6] == "y" :
				toGuess = toGuess[:6] + "y" + toGuess[7:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" and word[6] != "Y" and word[6] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[6] == "Z" or word[6] == "z" :
				toGuess = toGuess[:6] + "z" + toGuess[7:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" and word[6] != "Z" and word[6] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[6] == "A" or word[6] == "a" :
				toGuess = toGuess[:6] + "a" + toGuess[7:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" and word[6] != "A" and word[6] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[6] == "B" or word[6] == "b" :
				toGuess = toGuess[:6] + "b" + toGuess[7:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" and word[6] != "B" and word[6] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[6] == "C" or word[6] == "c" :
				toGuess = toGuess[:6] + "c" + toGuess[7:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" and word[6] != "C" and word[6] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[6] == "D" or word[6] == "d" :
				toGuess = toGuess[:6] + "d" + toGuess[7:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" and word[6] != "D" and word[6] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[6] == "E" or word[6] == "e" :
				toGuess = toGuess[:6] + "e" + toGuess[7:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" and word[6] != "E" and word[6] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[6] == "F" or word[6] == "f" :
				toGuess = toGuess[:6] + "f" + toGuess[7:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" and word[6] != "F" and word[6] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[6] == "G" or word[6] == "g" :
				toGuess = toGuess[:6] + "g" + toGuess[7:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" and word[6] != "G" and word[6] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[6] == "H" or word[6] == "h" :
				toGuess = toGuess[:6] + "h" + toGuess[7:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" and word[6] != "H" and word[6] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[6] == "I" or word[6] == "i" :
				toGuess = toGuess[:6] + "i" + toGuess[7:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" and word[6] != "I" and word[6] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[6] == "J" or word[6] == "j" :
				toGuess = toGuess[:6] + "j" + toGuess[7:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" and word[6] != "J" and word[6] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[6] == "K" or word[6] == "k" :
				toGuess = toGuess[:6] + "k" + toGuess[7:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" and word[6] != "K" and word[6] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[6] == "L" or word[6] == "l" :
				toGuess = toGuess[:6] + "l" + toGuess[7:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" and word[6] != "L" and word[6] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[6] == "M" or word[6] == "m" :
				toGuess = toGuess[:6] + "m" + toGuess[7:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" and word[6] != "M" and word[6] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[6] == "N" or word[6] == "n" :
				toGuess = toGuess[:6] + "n" + toGuess[7:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" and word[6] != "N" and word[6] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[6] == "O" or word[6] == "o" :
				toGuess = toGuess[:6] + "o" + toGuess[7:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" and word[6] != "O" and word[6] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[6] == "P" or word[6] == "p" :
				toGuess = toGuess[:6] + "p" + toGuess[7:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" and word[6] != "P" and word[6] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[6] == "Q" or word[6] == "q" :
				toGuess = toGuess[:6] + "q" + toGuess[7:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" and word[6] != "Q" and word[6] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[6] == "R" or word[6] == "r" :
				toGuess = toGuess[:6] + "r" + toGuess[7:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" and word[6] != "R" and word[6] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[6] == "S" or word[6] == "s" :
				toGuess = toGuess[:6] + "s" + toGuess[7:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" and word[6] != "S" and word[6] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[6] == "T" or word[6] == "t" :
				toGuess = toGuess[:6] + "t" + toGuess[7:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" and word[6] != "T" and word[6] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[6] == "U" or word[6] == "u" :
				toGuess = toGuess[:6] + "u" + toGuess[7:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" and word[6] != "U" and word[6] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[6] == "V" or word[6] == "v" :
				toGuess = toGuess[:6] + "v" + toGuess[7:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" and word[6] != "V" and word[6] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[6] == "W" or word[6] == "w" :
				toGuess = toGuess[:6] + "w" + toGuess[7:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" and word[6] != "W" and word[6] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[6] == "X" or word[6] == "x" :
				toGuess = toGuess[:6] + "x" + toGuess[7:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" and word[6] != "X" and word[6] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[6] == "Y" or word[6] == "y" :
				toGuess = toGuess[:6] + "y" + toGuess[7:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" and word[6] != "Y" and word[6] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[6] == "Z" or word[6] == "z" :
				toGuess = toGuess[:6] + "z" + toGuess[7:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" and word[6] != "Z" and word[6] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[6] == "A" or word[6] == "a" :
				toGuess = toGuess[:6] + "a" + toGuess[7:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" and word[6] != "A" and word[6] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[6] == "B" or word[6] == "b" :
				toGuess = toGuess[:6] + "b" + toGuess[7:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" and word[6] != "B" and word[6] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[6] == "C" or word[6] == "c" :
				toGuess = toGuess[:6] + "c" + toGuess[7:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" and word[6] != "C" and word[6] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[6] == "D" or word[6] == "d" :
				toGuess = toGuess[:6] + "d" + toGuess[7:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" and word[6] != "D" and word[6] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[6] == "E" or word[6] == "e" :
				toGuess = toGuess[:6] + "e" + toGuess[7:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" and word[6] != "E" and word[6] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[6] == "F" or word[6] == "f" :
				toGuess = toGuess[:6] + "f" + toGuess[7:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" and word[6] != "F" and word[6] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[6] == "G" or word[6] == "g" :
				toGuess = toGuess[:6] + "g" + toGuess[7:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" and word[6] != "G" and word[6] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[6] == "H" or word[6] == "h" :
				toGuess = toGuess[:6] + "h" + toGuess[7:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" and word[6] != "H" and word[6] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[6] == "I" or word[6] == "i" :
				toGuess = toGuess[:6] + "i" + toGuess[7:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" and word[6] != "I" and word[6] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[6] == "J" or word[6] == "j" :
				toGuess = toGuess[:6] + "j" + toGuess[7:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" and word[6] != "J" and word[6] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[6] == "K" or word[6] == "k" :
				toGuess = toGuess[:6] + "k" + toGuess[7:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" and word[6] != "K" and word[6] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[6] == "L" or word[6] == "l" :
				toGuess = toGuess[:6] + "l" + toGuess[7:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" and word[6] != "L" and word[6] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[6] == "M" or word[6] == "m" :
				toGuess = toGuess[:6] + "m" + toGuess[7:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" and word[6] != "M" and word[6] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[6] == "N" or word[6] == "n" :
				toGuess = toGuess[:6] + "n" + toGuess[7:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" and word[6] != "N" and word[6] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[6] == "O" or word[6] == "o" :
				toGuess = toGuess[:6] + "o" + toGuess[7:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" and word[6] != "O" and word[6] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[6] == "P" or word[6] == "p" :
				toGuess = toGuess[:6] + "p" + toGuess[7:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" and word[6] != "P" and word[6] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[6] == "Q" or word[6] == "q" :
				toGuess = toGuess[:6] + "q" + toGuess[7:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" and word[6] != "Q" and word[6] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[6] == "R" or word[6] == "r" :
				toGuess = toGuess[:6] + "r" + toGuess[7:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" and word[6] != "R" and word[6] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[6] == "S" or word[6] == "s" :
				toGuess = toGuess[:6] + "s" + toGuess[7:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" and word[6] != "S" and word[6] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[6] == "T" or word[6] == "t" :
				toGuess = toGuess[:6] + "t" + toGuess[7:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" and word[6] != "T" and word[6] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[6] == "U" or word[6] == "u" :
				toGuess = toGuess[:6] + "u" + toGuess[7:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" and word[6] != "U" and word[6] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[6] == "V" or word[6] == "v" :
				toGuess = toGuess[:6] + "v" + toGuess[7:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" and word[6] != "V" and word[6] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[6] == "W" or word[6] == "w" :
				toGuess = toGuess[:6] + "w" + toGuess[7:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" and word[6] != "W" and word[6] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[6] == "X" or word[6] == "x" :
				toGuess = toGuess[:6] + "x" + toGuess[7:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" and word[6] != "X" and word[6] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[6] == "Y" or word[6] == "y" :
				toGuess = toGuess[:6] + "y" + toGuess[7:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" and word[6] != "Y" and word[6] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[6] == "Z" or word[6] == "z" :
				toGuess = toGuess[:6] + "z" + toGuess[7:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" and word[6] != "Z" and word[6] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[6] == "A" or word[6] == "a" :
				toGuess = toGuess[:6] + "a" + toGuess[7:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" and word[6] != "A" and word[6] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[6] == "B" or word[6] == "b" :
				toGuess = toGuess[:6] + "b" + toGuess[7:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" and word[6] != "B" and word[6] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[6] == "C" or word[6] == "c" :
				toGuess = toGuess[:6] + "c" + toGuess[7:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" and word[6] != "C" and word[6] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[6] == "D" or word[6] == "d" :
				toGuess = toGuess[:6] + "d" + toGuess[7:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" and word[6] != "D" and word[6] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[6] == "E" or word[6] == "e" :
				toGuess = toGuess[:6] + "e" + toGuess[7:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" and word[6] != "E" and word[6] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[6] == "F" or word[6] == "f" :
				toGuess = toGuess[:6] + "f" + toGuess[7:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" and word[6] != "F" and word[6] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[6] == "G" or word[6] == "g" :
				toGuess = toGuess[:6] + "g" + toGuess[7:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" and word[6] != "G" and word[6] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[6] == "H" or word[6] == "h" :
				toGuess = toGuess[:6] + "h" + toGuess[7:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" and word[6] != "H" and word[6] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[6] == "I" or word[6] == "i" :
				toGuess = toGuess[:6] + "i" + toGuess[7:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" and word[6] != "I" and word[6] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[6] == "J" or word[6] == "j" :
				toGuess = toGuess[:6] + "j" + toGuess[7:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" and word[6] != "J" and word[6] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[6] == "K" or word[6] == "k" :
				toGuess = toGuess[:6] + "k" + toGuess[7:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" and word[6] != "K" and word[6] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[6] == "L" or word[6] == "l" :
				toGuess = toGuess[:6] + "l" + toGuess[7:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" and word[6] != "L" and word[6] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[6] == "M" or word[6] == "m" :
				toGuess = toGuess[:6] + "m" + toGuess[7:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" and word[6] != "M" and word[6] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[6] == "N" or word[6] == "n" :
				toGuess = toGuess[:6] + "n" + toGuess[7:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" and word[6] != "N" and word[6] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[6] == "O" or word[6] == "o" :
				toGuess = toGuess[:6] + "o" + toGuess[7:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" and word[6] != "O" and word[6] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[6] == "P" or word[6] == "p" :
				toGuess = toGuess[:6] + "p" + toGuess[7:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" and word[6] != "P" and word[6] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[6] == "Q" or word[6] == "q" :
				toGuess = toGuess[:6] + "q" + toGuess[7:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" and word[6] != "Q" and word[6] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[6] == "R" or word[6] == "r" :
				toGuess = toGuess[:6] + "r" + toGuess[7:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" and word[6] != "R" and word[6] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[6] == "S" or word[6] == "s" :
				toGuess = toGuess[:6] + "s" + toGuess[7:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" and word[6] != "S" and word[6] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[6] == "T" or word[6] == "t" :
				toGuess = toGuess[:6] + "t" + toGuess[7:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" and word[6] != "T" and word[6] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[6] == "U" or word[6] == "u" :
				toGuess = toGuess[:6] + "u" + toGuess[7:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" and word[6] != "U" and word[6] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[6] == "V" or word[6] == "v" :
				toGuess = toGuess[:6] + "v" + toGuess[7:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" and word[6] != "V" and word[6] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[6] == "W" or word[6] == "w" :
				toGuess = toGuess[:6] + "w" + toGuess[7:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" and word[6] != "W" and word[6] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[6] == "X" or word[6] == "x" :
				toGuess = toGuess[:6] + "x" + toGuess[7:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" and word[6] != "X" and word[6] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[6] == "Y" or word[6] == "y" :
				toGuess = toGuess[:6] + "y" + toGuess[7:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" and word[6] != "Y" and word[6] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[6] == "Z" or word[6] == "z" :
				toGuess = toGuess[:6] + "z" + toGuess[7:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" and word[6] != "Z" and word[6] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[6] == "A" or word[6] == "a" :
				toGuess = toGuess[:6] + "a" + toGuess[7:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" and word[6] != "A" and word[6] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[6] == "B" or word[6] == "b" :
				toGuess = toGuess[:6] + "b" + toGuess[7:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" and word[6] != "B" and word[6] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[6] == "C" or word[6] == "c" :
				toGuess = toGuess[:6] + "c" + toGuess[7:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" and word[6] != "C" and word[6] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[6] == "D" or word[6] == "d" :
				toGuess = toGuess[:6] + "d" + toGuess[7:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" and word[6] != "D" and word[6] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[6] == "E" or word[6] == "e" :
				toGuess = toGuess[:6] + "e" + toGuess[7:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" and word[6] != "E" and word[6] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[6] == "F" or word[6] == "f" :
				toGuess = toGuess[:6] + "f" + toGuess[7:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" and word[6] != "F" and word[6] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[6] == "G" or word[6] == "g" :
				toGuess = toGuess[:6] + "g" + toGuess[7:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" and word[6] != "G" and word[6] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[6] == "H" or word[6] == "h" :
				toGuess = toGuess[:6] + "h" + toGuess[7:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" and word[6] != "H" and word[6] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[6] == "I" or word[6] == "i" :
				toGuess = toGuess[:6] + "i" + toGuess[7:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" and word[6] != "I" and word[6] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[6] == "J" or word[6] == "j" :
				toGuess = toGuess[:6] + "j" + toGuess[7:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" and word[6] != "J" and word[6] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[6] == "K" or word[6] == "k" :
				toGuess = toGuess[:6] + "k" + toGuess[7:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" and word[6] != "K" and word[6] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[6] == "L" or word[6] == "l" :
				toGuess = toGuess[:6] + "l" + toGuess[7:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" and word[6] != "L" and word[6] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[6] == "M" or word[6] == "m" :
				toGuess = toGuess[:6] + "m" + toGuess[7:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" and word[6] != "M" and word[6] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[6] == "N" or word[6] == "n" :
				toGuess = toGuess[:6] + "n" + toGuess[7:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" and word[6] != "N" and word[6] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[6] == "O" or word[6] == "o" :
				toGuess = toGuess[:6] + "o" + toGuess[7:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" and word[6] != "O" and word[6] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[6] == "P" or word[6] == "p" :
				toGuess = toGuess[:6] + "p" + toGuess[7:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" and word[6] != "P" and word[6] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[6] == "Q" or word[6] == "q" :
				toGuess = toGuess[:6] + "q" + toGuess[7:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" and word[6] != "Q" and word[6] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[6] == "R" or word[6] == "r" :
				toGuess = toGuess[:6] + "r" + toGuess[7:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" and word[6] != "R" and word[6] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[6] == "S" or word[6] == "s" :
				toGuess = toGuess[:6] + "s" + toGuess[7:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" and word[6] != "S" and word[6] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[6] == "T" or word[6] == "t" :
				toGuess = toGuess[:6] + "t" + toGuess[7:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" and word[6] != "T" and word[6] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[6] == "U" or word[6] == "u" :
				toGuess = toGuess[:6] + "u" + toGuess[7:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" and word[6] != "U" and word[6] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[6] == "V" or word[6] == "v" :
				toGuess = toGuess[:6] + "v" + toGuess[7:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" and word[6] != "V" and word[6] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[6] == "W" or word[6] == "w" :
				toGuess = toGuess[:6] + "w" + toGuess[7:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" and word[6] != "W" and word[6] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[6] == "X" or word[6] == "x" :
				toGuess = toGuess[:6] + "x" + toGuess[7:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" and word[6] != "X" and word[6] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[6] == "Y" or word[6] == "y" :
				toGuess = toGuess[:6] + "y" + toGuess[7:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" and word[6] != "Y" and word[6] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[6] == "Z" or word[6] == "z" :
				toGuess = toGuess[:6] + "z" + toGuess[7:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" and word[6] != "Z" and word[6] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if "_" in toGuess and not loser :
		guessChar = ""
		while not guessChar.isalpha() :
			guessChar = input("\n---------------------------------\nEnter your letter: ")
		_ = os.system('cls' if os.name=='nt' else 'clear')
		if guessChar == "A" or guessChar == "a" :
			if word[1] == "A" or word[1] == "a" :
				toGuess = toGuess[:1] + "a" + toGuess[2:]
			if word[2] == "A" or word[2] == "a" :
				toGuess = toGuess[:2] + "a" + toGuess[3:]
			if word[3] == "A" or word[3] == "a" :
				toGuess = toGuess[:3] + "a" + toGuess[4:]
			if word[4] == "A" or word[4] == "a" :
				toGuess = toGuess[:4] + "a" + toGuess[5:]
			if word[5] == "A" or word[5] == "a" :
				toGuess = toGuess[:5] + "a" + toGuess[6:]
			if word[6] == "A" or word[6] == "a" :
				toGuess = toGuess[:6] + "a" + toGuess[7:]
			if word[1] != "A" and word[1] != "a" and word[2] != "A" and word[2] != "a" and word[3] != "A" and word[3] != "a" and word[4] != "A" and word[4] != "a" and word[5] != "A" and word[5] != "a" and word[6] != "A" and word[6] != "a" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "a" + ", "
		if guessChar == "B" or guessChar == "b" :
			if word[1] == "B" or word[1] == "b" :
				toGuess = toGuess[:1] + "b" + toGuess[2:]
			if word[2] == "B" or word[2] == "b" :
				toGuess = toGuess[:2] + "b" + toGuess[3:]
			if word[3] == "B" or word[3] == "b" :
				toGuess = toGuess[:3] + "b" + toGuess[4:]
			if word[4] == "B" or word[4] == "b" :
				toGuess = toGuess[:4] + "b" + toGuess[5:]
			if word[5] == "B" or word[5] == "b" :
				toGuess = toGuess[:5] + "b" + toGuess[6:]
			if word[6] == "B" or word[6] == "b" :
				toGuess = toGuess[:6] + "b" + toGuess[7:]
			if word[1] != "B" and word[1] != "b" and word[2] != "B" and word[2] != "b" and word[3] != "B" and word[3] != "b" and word[4] != "B" and word[4] != "b" and word[5] != "B" and word[5] != "b" and word[6] != "B" and word[6] != "b" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "b" + ", "
		if guessChar == "C" or guessChar == "c" :
			if word[1] == "C" or word[1] == "c" :
				toGuess = toGuess[:1] + "c" + toGuess[2:]
			if word[2] == "C" or word[2] == "c" :
				toGuess = toGuess[:2] + "c" + toGuess[3:]
			if word[3] == "C" or word[3] == "c" :
				toGuess = toGuess[:3] + "c" + toGuess[4:]
			if word[4] == "C" or word[4] == "c" :
				toGuess = toGuess[:4] + "c" + toGuess[5:]
			if word[5] == "C" or word[5] == "c" :
				toGuess = toGuess[:5] + "c" + toGuess[6:]
			if word[6] == "C" or word[6] == "c" :
				toGuess = toGuess[:6] + "c" + toGuess[7:]
			if word[1] != "C" and word[1] != "c" and word[2] != "C" and word[2] != "c" and word[3] != "C" and word[3] != "c" and word[4] != "C" and word[4] != "c" and word[5] != "C" and word[5] != "c" and word[6] != "C" and word[6] != "c" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "c" + ", "
		if guessChar == "D" or guessChar == "d" :
			if word[1] == "D" or word[1] == "d" :
				toGuess = toGuess[:1] + "d" + toGuess[2:]
			if word[2] == "D" or word[2] == "d" :
				toGuess = toGuess[:2] + "d" + toGuess[3:]
			if word[3] == "D" or word[3] == "d" :
				toGuess = toGuess[:3] + "d" + toGuess[4:]
			if word[4] == "D" or word[4] == "d" :
				toGuess = toGuess[:4] + "d" + toGuess[5:]
			if word[5] == "D" or word[5] == "d" :
				toGuess = toGuess[:5] + "d" + toGuess[6:]
			if word[6] == "D" or word[6] == "d" :
				toGuess = toGuess[:6] + "d" + toGuess[7:]
			if word[1] != "D" and word[1] != "d" and word[2] != "D" and word[2] != "d" and word[3] != "D" and word[3] != "d" and word[4] != "D" and word[4] != "d" and word[5] != "D" and word[5] != "d" and word[6] != "D" and word[6] != "d" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "d" + ", "
		if guessChar == "E" or guessChar == "e" :
			if word[1] == "E" or word[1] == "e" :
				toGuess = toGuess[:1] + "e" + toGuess[2:]
			if word[2] == "E" or word[2] == "e" :
				toGuess = toGuess[:2] + "e" + toGuess[3:]
			if word[3] == "E" or word[3] == "e" :
				toGuess = toGuess[:3] + "e" + toGuess[4:]
			if word[4] == "E" or word[4] == "e" :
				toGuess = toGuess[:4] + "e" + toGuess[5:]
			if word[5] == "E" or word[5] == "e" :
				toGuess = toGuess[:5] + "e" + toGuess[6:]
			if word[6] == "E" or word[6] == "e" :
				toGuess = toGuess[:6] + "e" + toGuess[7:]
			if word[1] != "E" and word[1] != "e" and word[2] != "E" and word[2] != "e" and word[3] != "E" and word[3] != "e" and word[4] != "E" and word[4] != "e" and word[5] != "E" and word[5] != "e" and word[6] != "E" and word[6] != "e" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "e" + ", "
		if guessChar == "F" or guessChar == "f" :
			if word[1] == "F" or word[1] == "f" :
				toGuess = toGuess[:1] + "f" + toGuess[2:]
			if word[2] == "F" or word[2] == "f" :
				toGuess = toGuess[:2] + "f" + toGuess[3:]
			if word[3] == "F" or word[3] == "f" :
				toGuess = toGuess[:3] + "f" + toGuess[4:]
			if word[4] == "F" or word[4] == "f" :
				toGuess = toGuess[:4] + "f" + toGuess[5:]
			if word[5] == "F" or word[5] == "f" :
				toGuess = toGuess[:5] + "f" + toGuess[6:]
			if word[6] == "F" or word[6] == "f" :
				toGuess = toGuess[:6] + "f" + toGuess[7:]
			if word[1] != "F" and word[1] != "f" and word[2] != "F" and word[2] != "f" and word[3] != "F" and word[3] != "f" and word[4] != "F" and word[4] != "f" and word[5] != "F" and word[5] != "f" and word[6] != "F" and word[6] != "f" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "f" + ", "
		if guessChar == "G" or guessChar == "g" :
			if word[1] == "G" or word[1] == "g" :
				toGuess = toGuess[:1] + "g" + toGuess[2:]
			if word[2] == "G" or word[2] == "g" :
				toGuess = toGuess[:2] + "g" + toGuess[3:]
			if word[3] == "G" or word[3] == "g" :
				toGuess = toGuess[:3] + "g" + toGuess[4:]
			if word[4] == "G" or word[4] == "g" :
				toGuess = toGuess[:4] + "g" + toGuess[5:]
			if word[5] == "G" or word[5] == "g" :
				toGuess = toGuess[:5] + "g" + toGuess[6:]
			if word[6] == "G" or word[6] == "g" :
				toGuess = toGuess[:6] + "g" + toGuess[7:]
			if word[1] != "G" and word[1] != "g" and word[2] != "G" and word[2] != "g" and word[3] != "G" and word[3] != "g" and word[4] != "G" and word[4] != "g" and word[5] != "G" and word[5] != "g" and word[6] != "G" and word[6] != "g" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "g" + ", "
		if guessChar == "H" or guessChar == "h" :
			if word[1] == "H" or word[1] == "h" :
				toGuess = toGuess[:1] + "h" + toGuess[2:]
			if word[2] == "H" or word[2] == "h" :
				toGuess = toGuess[:2] + "h" + toGuess[3:]
			if word[3] == "H" or word[3] == "h" :
				toGuess = toGuess[:3] + "h" + toGuess[4:]
			if word[4] == "H" or word[4] == "h" :
				toGuess = toGuess[:4] + "h" + toGuess[5:]
			if word[5] == "H" or word[5] == "h" :
				toGuess = toGuess[:5] + "h" + toGuess[6:]
			if word[6] == "H" or word[6] == "h" :
				toGuess = toGuess[:6] + "h" + toGuess[7:]
			if word[1] != "H" and word[1] != "h" and word[2] != "H" and word[2] != "h" and word[3] != "H" and word[3] != "h" and word[4] != "H" and word[4] != "h" and word[5] != "H" and word[5] != "h" and word[6] != "H" and word[6] != "h" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "h" + ", "
		if guessChar == "I" or guessChar == "i" :
			if word[1] == "I" or word[1] == "i" :
				toGuess = toGuess[:1] + "i" + toGuess[2:]
			if word[2] == "I" or word[2] == "i" :
				toGuess = toGuess[:2] + "i" + toGuess[3:]
			if word[3] == "I" or word[3] == "i" :
				toGuess = toGuess[:3] + "i" + toGuess[4:]
			if word[4] == "I" or word[4] == "i" :
				toGuess = toGuess[:4] + "i" + toGuess[5:]
			if word[5] == "I" or word[5] == "i" :
				toGuess = toGuess[:5] + "i" + toGuess[6:]
			if word[6] == "I" or word[6] == "i" :
				toGuess = toGuess[:6] + "i" + toGuess[7:]
			if word[1] != "I" and word[1] != "i" and word[2] != "I" and word[2] != "i" and word[3] != "I" and word[3] != "i" and word[4] != "I" and word[4] != "i" and word[5] != "I" and word[5] != "i" and word[6] != "I" and word[6] != "i" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "i" + ", "
		if guessChar == "J" or guessChar == "j" :
			if word[1] == "J" or word[1] == "j" :
				toGuess = toGuess[:1] + "j" + toGuess[2:]
			if word[2] == "J" or word[2] == "j" :
				toGuess = toGuess[:2] + "j" + toGuess[3:]
			if word[3] == "J" or word[3] == "j" :
				toGuess = toGuess[:3] + "j" + toGuess[4:]
			if word[4] == "J" or word[4] == "j" :
				toGuess = toGuess[:4] + "j" + toGuess[5:]
			if word[5] == "J" or word[5] == "j" :
				toGuess = toGuess[:5] + "j" + toGuess[6:]
			if word[6] == "J" or word[6] == "j" :
				toGuess = toGuess[:6] + "j" + toGuess[7:]
			if word[1] != "J" and word[1] != "j" and word[2] != "J" and word[2] != "j" and word[3] != "J" and word[3] != "j" and word[4] != "J" and word[4] != "j" and word[5] != "J" and word[5] != "j" and word[6] != "J" and word[6] != "j" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "j" + ", "
		if guessChar == "K" or guessChar == "k" :
			if word[1] == "K" or word[1] == "k" :
				toGuess = toGuess[:1] + "k" + toGuess[2:]
			if word[2] == "K" or word[2] == "k" :
				toGuess = toGuess[:2] + "k" + toGuess[3:]
			if word[3] == "K" or word[3] == "k" :
				toGuess = toGuess[:3] + "k" + toGuess[4:]
			if word[4] == "K" or word[4] == "k" :
				toGuess = toGuess[:4] + "k" + toGuess[5:]
			if word[5] == "K" or word[5] == "k" :
				toGuess = toGuess[:5] + "k" + toGuess[6:]
			if word[6] == "K" or word[6] == "k" :
				toGuess = toGuess[:6] + "k" + toGuess[7:]
			if word[1] != "K" and word[1] != "k" and word[2] != "K" and word[2] != "k" and word[3] != "K" and word[3] != "k" and word[4] != "K" and word[4] != "k" and word[5] != "K" and word[5] != "k" and word[6] != "K" and word[6] != "k" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "k" + ", "
		if guessChar == "L" or guessChar == "l" :
			if word[1] == "L" or word[1] == "l" :
				toGuess = toGuess[:1] + "l" + toGuess[2:]
			if word[2] == "L" or word[2] == "l" :
				toGuess = toGuess[:2] + "l" + toGuess[3:]
			if word[3] == "L" or word[3] == "l" :
				toGuess = toGuess[:3] + "l" + toGuess[4:]
			if word[4] == "L" or word[4] == "l" :
				toGuess = toGuess[:4] + "l" + toGuess[5:]
			if word[5] == "L" or word[5] == "l" :
				toGuess = toGuess[:5] + "l" + toGuess[6:]
			if word[6] == "L" or word[6] == "l" :
				toGuess = toGuess[:6] + "l" + toGuess[7:]
			if word[1] != "L" and word[1] != "l" and word[2] != "L" and word[2] != "l" and word[3] != "L" and word[3] != "l" and word[4] != "L" and word[4] != "l" and word[5] != "L" and word[5] != "l" and word[6] != "L" and word[6] != "l" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "l" + ", "
		if guessChar == "M" or guessChar == "m" :
			if word[1] == "M" or word[1] == "m" :
				toGuess = toGuess[:1] + "m" + toGuess[2:]
			if word[2] == "M" or word[2] == "m" :
				toGuess = toGuess[:2] + "m" + toGuess[3:]
			if word[3] == "M" or word[3] == "m" :
				toGuess = toGuess[:3] + "m" + toGuess[4:]
			if word[4] == "M" or word[4] == "m" :
				toGuess = toGuess[:4] + "m" + toGuess[5:]
			if word[5] == "M" or word[5] == "m" :
				toGuess = toGuess[:5] + "m" + toGuess[6:]
			if word[6] == "M" or word[6] == "m" :
				toGuess = toGuess[:6] + "m" + toGuess[7:]
			if word[1] != "M" and word[1] != "m" and word[2] != "M" and word[2] != "m" and word[3] != "M" and word[3] != "m" and word[4] != "M" and word[4] != "m" and word[5] != "M" and word[5] != "m" and word[6] != "M" and word[6] != "m" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "m" + ", "
		if guessChar == "N" or guessChar == "n" :
			if word[1] == "N" or word[1] == "n" :
				toGuess = toGuess[:1] + "n" + toGuess[2:]
			if word[2] == "N" or word[2] == "n" :
				toGuess = toGuess[:2] + "n" + toGuess[3:]
			if word[3] == "N" or word[3] == "n" :
				toGuess = toGuess[:3] + "n" + toGuess[4:]
			if word[4] == "N" or word[4] == "n" :
				toGuess = toGuess[:4] + "n" + toGuess[5:]
			if word[5] == "N" or word[5] == "n" :
				toGuess = toGuess[:5] + "n" + toGuess[6:]
			if word[6] == "N" or word[6] == "n" :
				toGuess = toGuess[:6] + "n" + toGuess[7:]
			if word[1] != "N" and word[1] != "n" and word[2] != "N" and word[2] != "n" and word[3] != "N" and word[3] != "n" and word[4] != "N" and word[4] != "n" and word[5] != "N" and word[5] != "n" and word[6] != "N" and word[6] != "n" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "n" + ", "
		if guessChar == "O" or guessChar == "o" :
			if word[1] == "O" or word[1] == "o" :
				toGuess = toGuess[:1] + "o" + toGuess[2:]
			if word[2] == "O" or word[2] == "o" :
				toGuess = toGuess[:2] + "o" + toGuess[3:]
			if word[3] == "O" or word[3] == "o" :
				toGuess = toGuess[:3] + "o" + toGuess[4:]
			if word[4] == "O" or word[4] == "o" :
				toGuess = toGuess[:4] + "o" + toGuess[5:]
			if word[5] == "O" or word[5] == "o" :
				toGuess = toGuess[:5] + "o" + toGuess[6:]
			if word[6] == "O" or word[6] == "o" :
				toGuess = toGuess[:6] + "o" + toGuess[7:]
			if word[1] != "O" and word[1] != "o" and word[2] != "O" and word[2] != "o" and word[3] != "O" and word[3] != "o" and word[4] != "O" and word[4] != "o" and word[5] != "O" and word[5] != "o" and word[6] != "O" and word[6] != "o" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "o" + ", "
		if guessChar == "P" or guessChar == "p" :
			if word[1] == "P" or word[1] == "p" :
				toGuess = toGuess[:1] + "p" + toGuess[2:]
			if word[2] == "P" or word[2] == "p" :
				toGuess = toGuess[:2] + "p" + toGuess[3:]
			if word[3] == "P" or word[3] == "p" :
				toGuess = toGuess[:3] + "p" + toGuess[4:]
			if word[4] == "P" or word[4] == "p" :
				toGuess = toGuess[:4] + "p" + toGuess[5:]
			if word[5] == "P" or word[5] == "p" :
				toGuess = toGuess[:5] + "p" + toGuess[6:]
			if word[6] == "P" or word[6] == "p" :
				toGuess = toGuess[:6] + "p" + toGuess[7:]
			if word[1] != "P" and word[1] != "p" and word[2] != "P" and word[2] != "p" and word[3] != "P" and word[3] != "p" and word[4] != "P" and word[4] != "p" and word[5] != "P" and word[5] != "p" and word[6] != "P" and word[6] != "p" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "p" + ", "
		if guessChar == "Q" or guessChar == "q" :
			if word[1] == "Q" or word[1] == "q" :
				toGuess = toGuess[:1] + "q" + toGuess[2:]
			if word[2] == "Q" or word[2] == "q" :
				toGuess = toGuess[:2] + "q" + toGuess[3:]
			if word[3] == "Q" or word[3] == "q" :
				toGuess = toGuess[:3] + "q" + toGuess[4:]
			if word[4] == "Q" or word[4] == "q" :
				toGuess = toGuess[:4] + "q" + toGuess[5:]
			if word[5] == "Q" or word[5] == "q" :
				toGuess = toGuess[:5] + "q" + toGuess[6:]
			if word[6] == "Q" or word[6] == "q" :
				toGuess = toGuess[:6] + "q" + toGuess[7:]
			if word[1] != "Q" and word[1] != "q" and word[2] != "Q" and word[2] != "q" and word[3] != "Q" and word[3] != "q" and word[4] != "Q" and word[4] != "q" and word[5] != "Q" and word[5] != "q" and word[6] != "Q" and word[6] != "q" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "q" + ", "
		if guessChar == "R" or guessChar == "r" :
			if word[1] == "R" or word[1] == "r" :
				toGuess = toGuess[:1] + "r" + toGuess[2:]
			if word[2] == "R" or word[2] == "r" :
				toGuess = toGuess[:2] + "r" + toGuess[3:]
			if word[3] == "R" or word[3] == "r" :
				toGuess = toGuess[:3] + "r" + toGuess[4:]
			if word[4] == "R" or word[4] == "r" :
				toGuess = toGuess[:4] + "r" + toGuess[5:]
			if word[5] == "R" or word[5] == "r" :
				toGuess = toGuess[:5] + "r" + toGuess[6:]
			if word[6] == "R" or word[6] == "r" :
				toGuess = toGuess[:6] + "r" + toGuess[7:]
			if word[1] != "R" and word[1] != "r" and word[2] != "R" and word[2] != "r" and word[3] != "R" and word[3] != "r" and word[4] != "R" and word[4] != "r" and word[5] != "R" and word[5] != "r" and word[6] != "R" and word[6] != "r" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "r" + ", "
		if guessChar == "S" or guessChar == "s" :
			if word[1] == "S" or word[1] == "s" :
				toGuess = toGuess[:1] + "s" + toGuess[2:]
			if word[2] == "S" or word[2] == "s" :
				toGuess = toGuess[:2] + "s" + toGuess[3:]
			if word[3] == "S" or word[3] == "s" :
				toGuess = toGuess[:3] + "s" + toGuess[4:]
			if word[4] == "S" or word[4] == "s" :
				toGuess = toGuess[:4] + "s" + toGuess[5:]
			if word[5] == "S" or word[5] == "s" :
				toGuess = toGuess[:5] + "s" + toGuess[6:]
			if word[6] == "S" or word[6] == "s" :
				toGuess = toGuess[:6] + "s" + toGuess[7:]
			if word[1] != "S" and word[1] != "s" and word[2] != "S" and word[2] != "s" and word[3] != "S" and word[3] != "s" and word[4] != "S" and word[4] != "s" and word[5] != "S" and word[5] != "s" and word[6] != "S" and word[6] != "s" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "s" + ", "
		if guessChar == "T" or guessChar == "t" :
			if word[1] == "T" or word[1] == "t" :
				toGuess = toGuess[:1] + "t" + toGuess[2:]
			if word[2] == "T" or word[2] == "t" :
				toGuess = toGuess[:2] + "t" + toGuess[3:]
			if word[3] == "T" or word[3] == "t" :
				toGuess = toGuess[:3] + "t" + toGuess[4:]
			if word[4] == "T" or word[4] == "t" :
				toGuess = toGuess[:4] + "t" + toGuess[5:]
			if word[5] == "T" or word[5] == "t" :
				toGuess = toGuess[:5] + "t" + toGuess[6:]
			if word[6] == "T" or word[6] == "t" :
				toGuess = toGuess[:6] + "t" + toGuess[7:]
			if word[1] != "T" and word[1] != "t" and word[2] != "T" and word[2] != "t" and word[3] != "T" and word[3] != "t" and word[4] != "T" and word[4] != "t" and word[5] != "T" and word[5] != "t" and word[6] != "T" and word[6] != "t" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "t" + ", "
		if guessChar == "U" or guessChar == "u" :
			if word[1] == "U" or word[1] == "u" :
				toGuess = toGuess[:1] + "u" + toGuess[2:]
			if word[2] == "U" or word[2] == "u" :
				toGuess = toGuess[:2] + "u" + toGuess[3:]
			if word[3] == "U" or word[3] == "u" :
				toGuess = toGuess[:3] + "u" + toGuess[4:]
			if word[4] == "U" or word[4] == "u" :
				toGuess = toGuess[:4] + "u" + toGuess[5:]
			if word[5] == "U" or word[5] == "u" :
				toGuess = toGuess[:5] + "u" + toGuess[6:]
			if word[6] == "U" or word[6] == "u" :
				toGuess = toGuess[:6] + "u" + toGuess[7:]
			if word[1] != "U" and word[1] != "u" and word[2] != "U" and word[2] != "u" and word[3] != "U" and word[3] != "u" and word[4] != "U" and word[4] != "u" and word[5] != "U" and word[5] != "u" and word[6] != "U" and word[6] != "u" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "u" + ", "
		if guessChar == "V" or guessChar == "v" :
			if word[1] == "V" or word[1] == "v" :
				toGuess = toGuess[:1] + "v" + toGuess[2:]
			if word[2] == "V" or word[2] == "v" :
				toGuess = toGuess[:2] + "v" + toGuess[3:]
			if word[3] == "V" or word[3] == "v" :
				toGuess = toGuess[:3] + "v" + toGuess[4:]
			if word[4] == "V" or word[4] == "v" :
				toGuess = toGuess[:4] + "v" + toGuess[5:]
			if word[5] == "V" or word[5] == "v" :
				toGuess = toGuess[:5] + "v" + toGuess[6:]
			if word[6] == "V" or word[6] == "v" :
				toGuess = toGuess[:6] + "v" + toGuess[7:]
			if word[1] != "V" and word[1] != "v" and word[2] != "V" and word[2] != "v" and word[3] != "V" and word[3] != "v" and word[4] != "V" and word[4] != "v" and word[5] != "V" and word[5] != "v" and word[6] != "V" and word[6] != "v" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "v" + ", "
		if guessChar == "W" or guessChar == "w" :
			if word[1] == "W" or word[1] == "w" :
				toGuess = toGuess[:1] + "w" + toGuess[2:]
			if word[2] == "W" or word[2] == "w" :
				toGuess = toGuess[:2] + "w" + toGuess[3:]
			if word[3] == "W" or word[3] == "w" :
				toGuess = toGuess[:3] + "w" + toGuess[4:]
			if word[4] == "W" or word[4] == "w" :
				toGuess = toGuess[:4] + "w" + toGuess[5:]
			if word[5] == "W" or word[5] == "w" :
				toGuess = toGuess[:5] + "w" + toGuess[6:]
			if word[6] == "W" or word[6] == "w" :
				toGuess = toGuess[:6] + "w" + toGuess[7:]
			if word[1] != "W" and word[1] != "w" and word[2] != "W" and word[2] != "w" and word[3] != "W" and word[3] != "w" and word[4] != "W" and word[4] != "w" and word[5] != "W" and word[5] != "w" and word[6] != "W" and word[6] != "w" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "w" + ", "
		if guessChar == "X" or guessChar == "x" :
			if word[1] == "X" or word[1] == "x" :
				toGuess = toGuess[:1] + "x" + toGuess[2:]
			if word[2] == "X" or word[2] == "x" :
				toGuess = toGuess[:2] + "x" + toGuess[3:]
			if word[3] == "X" or word[3] == "x" :
				toGuess = toGuess[:3] + "x" + toGuess[4:]
			if word[4] == "X" or word[4] == "x" :
				toGuess = toGuess[:4] + "x" + toGuess[5:]
			if word[5] == "X" or word[5] == "x" :
				toGuess = toGuess[:5] + "x" + toGuess[6:]
			if word[6] == "X" or word[6] == "x" :
				toGuess = toGuess[:6] + "x" + toGuess[7:]
			if word[1] != "X" and word[1] != "x" and word[2] != "X" and word[2] != "x" and word[3] != "X" and word[3] != "x" and word[4] != "X" and word[4] != "x" and word[5] != "X" and word[5] != "x" and word[6] != "X" and word[6] != "x" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "x" + ", "
		if guessChar == "Y" or guessChar == "y" :
			if word[1] == "Y" or word[1] == "y" :
				toGuess = toGuess[:1] + "y" + toGuess[2:]
			if word[2] == "Y" or word[2] == "y" :
				toGuess = toGuess[:2] + "y" + toGuess[3:]
			if word[3] == "Y" or word[3] == "y" :
				toGuess = toGuess[:3] + "y" + toGuess[4:]
			if word[4] == "Y" or word[4] == "y" :
				toGuess = toGuess[:4] + "y" + toGuess[5:]
			if word[5] == "Y" or word[5] == "y" :
				toGuess = toGuess[:5] + "y" + toGuess[6:]
			if word[6] == "Y" or word[6] == "y" :
				toGuess = toGuess[:6] + "y" + toGuess[7:]
			if word[1] != "Y" and word[1] != "y" and word[2] != "Y" and word[2] != "y" and word[3] != "Y" and word[3] != "y" and word[4] != "Y" and word[4] != "y" and word[5] != "Y" and word[5] != "y" and word[6] != "Y" and word[6] != "y" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "y" + ", "
		if guessChar == "Z" or guessChar == "z" :
			if word[1] == "Z" or word[1] == "z" :
				toGuess = toGuess[:1] + "z" + toGuess[2:]
			if word[2] == "Z" or word[2] == "z" :
				toGuess = toGuess[:2] + "z" + toGuess[3:]
			if word[3] == "Z" or word[3] == "z" :
				toGuess = toGuess[:3] + "z" + toGuess[4:]
			if word[4] == "Z" or word[4] == "z" :
				toGuess = toGuess[:4] + "z" + toGuess[5:]
			if word[5] == "Z" or word[5] == "z" :
				toGuess = toGuess[:5] + "z" + toGuess[6:]
			if word[6] == "Z" or word[6] == "z" :
				toGuess = toGuess[:6] + "z" + toGuess[7:]
			if word[1] != "Z" and word[1] != "z" and word[2] != "Z" and word[2] != "z" and word[3] != "Z" and word[3] != "z" and word[4] != "Z" and word[4] != "z" and word[5] != "Z" and word[5] != "z" and word[6] != "Z" and word[6] != "z" :
				print("\nWrong!\n")
				numberOfErrors = numberOfErrors + 1
				wrongChars = wrongChars + "z" + ", "
		if numberOfErrors == 0 :
			print("\t___________")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 1 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 2 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|         |")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 3 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 4 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|")
			print("\t|")
			print("\t|")
		if numberOfErrors == 5 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / ")
			print("\t|")
			print("\t|")
		if numberOfErrors == 6 :
			print("\t___________")
			print("\t|         |")
			print("\t|         O")
			print("\t|        /|\\")
			print("\t|        / \\")
			print("\t|")
			print("\t|")
			print("\nYou lose! GAME OVER\n")
			print("The answer was \"" + word + "\"")
			loser = True
		if not loser :
			print("\n\tWord: " + toGuess)
			print("\tMisses: " + wrongChars)
	if not "_" in toGuess :
		print("\nCONGRATULATIONS! You win!!!")
