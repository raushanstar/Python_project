import Hangman_creator
hangman=Hangman_creator.Hangman('E:\\python project\wordlist.txt')
hangman.choosen_the_word()
hangman.fill_the_word_status()
while True:
	hangman.get_word_status()
	hangman.guess_the_letter()
	if(hangman.attempts_remaining==0):
		print("out of attempts . The word was ' {} '. game over ! ".format(hangman.choosen_word))
		break
	elif(hangman.choosen_word==''.join(hangman.word_status)):
		print(" Hurray ! You won the game ")
		break