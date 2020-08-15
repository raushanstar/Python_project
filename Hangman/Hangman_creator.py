import random
import re
class Hangman:
    def __init__(self,wordlist):
        self.wordlist=wordlist
        self.attempts_remaining=6    #number of attempt
        self.current_letter=' '
        self.choosen_word=' '
        self.guessed_letters=[]

    def choosen_the_word(self):
        file=open(self.wordlist)
        words=file.read().split()
        word_count=len(words)
        self.choosen_word=words[random.randrange(0,word_count)]
        self.word_status = ['-' for i in range(len(self.choosen_word))]

    def fill_the_word_status(self):
        nos=random.randrange(1,3)
        for i in range(nos):
            position=random.randrange(0,len(self.choosen_word))
            self.word_status[position]=self.choosen_word[position]

    def guess_the_letter(self):
        letter=input("Guess the letter: ")
        if(letter in self.guessed_letters):
            print("You have already guessed that letter . your guesses: {}".format(''.join(self.guessed_letters)))
            return
        self.guessed_letters.append(letter)
        occ=[]
        occurence=re.finditer(letter,self.choosen_word)
        for m in occurence:
            occ.append(m.start())

        if(len(occ)==0):
            self.attempts_remaining-=1
            print("your guess was wrong. Attempts remanining is {} ".format(self.attempts_remaining))
        else:
            for position in occ:
                self.word_status[position]=self.choosen_word[position]
            print("Correct word! ")

    def get_word_status(self):
        print("Current status : {}\n".format(''.join(self.word_status)))