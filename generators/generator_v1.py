def art(error, tabs):
	art = ""
	for i in range(tabs):
		art += "\t"
	art += "print(\"\\t___________\")\n"
	for i in range(tabs):
		art += "\t"
	art += "print(\"\\t|         |\")\n"
	for i in range(tabs):
		art += "\t"
	if error > 0 :
		art += "print(\"\\t|         O\")\n"
	else :
		art += "print(\"\\t|\")\n"
	for i in range(tabs):
		art += "\t"
	if error > 3 :
		art += "print(\"\\t|        /|\\\\\")\n"
	elif error > 2 :
		art += "print(\"\\t|        /|\")\n"
	elif error > 1 :
		art += "print(\"\\t|         |\")\n"
	else :
		art += "print(\"\\t|\")\n"
	for i in range(tabs):
		art += "\t"
	if error > 5 :
		art += "print(\"\\t|        / \\\\\")\n"
	elif error > 4 :
		art += "print(\"\\t|        / \")\n"
	else :
		art += "print(\"\\t|\")\n"
	for i in range(tabs):
		art += "\t"
	art += "print(\"\\t|\")\n"
	for i in range(tabs):
		art += "\t"
	art += "print(\"\\t|\")\n"
	if error > 5 :
		for i in range(tabs):
			art += "\t"
		art += "print(\"\\nYou lose! GAME OVER\\n\")\n"
		for i in range(tabs):
			art += "\t"
		art += "print(\"The answer was \\\"\" + word + \"\\\"\")\n"
		for i in range(tabs):
			art += "\t"
		art += "loser = True\n"
	return art
                      
s = open('hangman_v1.py', 'w')
s.write("import os\n\n")
s.write("word = \"\"\n")
s.write("loser = False\n")
s.write("_ = os.system('cls' if os.name=='nt' else 'clear')\n")
s.write("while not word.isalpha() :\n\tword = input(\"Hi, Player 1! It's a game 'Hangman'! Write your word below:\\n(Note that word must be between 5 and 12 letters & without spaces!)\\n\")\n")
s.write("_ = os.system('cls' if os.name=='nt' else 'clear')\n")
s.write("print(\"Hi, Player 2! it's a game 'Hangman'! This is the word you need to guess:\\n\")\n")
# :num: how much letters in the word
for num in range(5, 13) :
	s.write("\nif len(word) == " + str(num) +" :\n")
	s.write("\ttoGuess = str(word[0]) + \"")
	for i in range(num-2) :
		s.write("_")
	s.write("\" + str(word[" + str(num-1) + "])\n")
	s.write("\tnumberOfErrors = 0\n\twrongChars=\"\"\n")
	s.write(art(0,1))
	s.write("\tprint(\"\\n\\tWord: \" + toGuess)\n")
	s.write("\tprint(\"\\tMisses: \" + wrongChars)\n")
	# :numOfLoop: maximum possible number of Guesser's turns 
	for numOfLoop in range(num+3) :
		s.write("\tif \"_\" in toGuess and not loser :\n")
		s.write("\t\tguessChar = \"\"\n")
		s.write("\t\twhile not guessChar.isalpha() :\n\t\t\tguessChar = input(\"\\n---------------------------------\\nEnter your letter: \")\n")
		s.write("\t\t_ = os.system('cls' if os.name=='nt' else 'clear')\n")
		for letter in range(65, 91) :
			s.write("\t\tif guessChar == \"" + chr(letter) + "\" or guessChar == \"" + chr(letter+32) + "\" :\n")
			# Checks if :letter: equals any (starts from 2nd) character from word
			for guessCount in range(1, num-1) :
				s.write("\t\t\tif word[" + str(guessCount) + "] == \"" + chr(letter) + "\" or word[" + str(guessCount) + "] == \"" + chr(letter+32) + "\" :\n")
				s.write("\t\t\t\ttoGuess = toGuess[:" + str(guessCount) + "] + \"" + chr(letter+32) + "\" + toGuess[" + str(guessCount+1) + ":]\n")
			s.write("\t\t\tif")
			for i in range(1, num-1) :
				s.write(" word[" + str(i) + "] != \"" + chr(letter) + "\" and word[" + str(i) + "] != \"" + chr(letter+32) + "\"")
				if i == num-2 :
					continue
				s.write(" and")
			s.write(" :\n")
			s.write("\t\t\t\tprint(\"\\nWrong!\\n\")\n")
			s.write("\t\t\t\tnumberOfErrors = numberOfErrors + 1\n")
			s.write("\t\t\t\twrongChars = wrongChars + \"" + chr(letter+32) + "\" + \", \"\n")
		# Writes 'if' statements for ASCII art
		for i in range(numOfLoop+2) :
			if i>6 :
			 	continue
			s.write("\t\tif numberOfErrors == " + str(i) + " :\n")
			s.write(art(i, 3))
		if numOfLoop >= 5 :
			s.write("\t\tif not loser :\n")
			s.write("\t\t\tprint(\"\\n\\tWord: \" + toGuess)\n")
			s.write("\t\t\tprint(\"\\tMisses: \" + wrongChars)\n")
		else :
			s.write("\t\tprint(\"\\n\\tWord: \" + toGuess)\n")
			s.write("\t\tprint(\"\\tMisses: \" + wrongChars)\n")
	s.write("\tif not \"_\" in toGuess :\n\t\tprint(\"\\nCONGRATULATIONS! You win!!!\")\n")
s.close()