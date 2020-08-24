from phrasehunter.phrase import Phrase
import random

class Game:
	def __init__(self):
		self.missed = 0
		self.active_phrase = self.get_random_phrase()
		self.guesses = [" "]
	
	def get_random_phrase(self):
		phrases = [
		Phrase('The best of both worlds'),
		Phrase('Speak of the devil'),
		Phrase('Once in a blue moon'),
		Phrase('When pigs fly'),
		Phrase('Kill two birds with one stone')
		]
		phrase_object = random.choice(phrases)
		return phrase_object
	
	def start(self):
		self.welcome()
		while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
			print("\nNumber missed: ", self.missed)
			self.active_phrase.display(self.guesses)
			self.user_guess = self.get_guess()
			self.guesses.append(self.user_guess)
			if not self.active_phrase.check_guess(self.user_guess):
				self.missed += 1
				print("\nYou have {} out of 5 lives remaining!".format(5 - self.missed))
			self.game_over()
			
	def welcome(self):
		print("\n==================================="
			  "\nWelcome to the Phrase Hunter Game"
			  "\n===================================")
		
	def get_guess(self):
		self.guess = input("Choose a letter: ")
		if not self.guess.isalpha() or len(self.guess) > 1:
			print("\nPlease enter only one letter A-Z")
		return self.guess
	
	def game_over(self):
		if self.active_phrase.check_complete(self.guesses) == True:
			print("\nCongratulations, You Won The Game!!\n")
		if self.missed == 5:
			print("\nGame Over\n")
		if self.active_phrase.check_complete(self.guesses) == True or self.missed == 5:
			play_again = input("\nWould you like to play again? y/n ")
			if play_again.lower() == "y":
				self.__init__()
				self.start()
