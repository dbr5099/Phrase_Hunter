
class Phrase:
	def __init__(self, phrase):
		self.phrase = phrase.lower()
	
	def display(self, guesses):
		"""Displays an underscore for every letter in the phrase"""
		for letter in self.phrase:
			if letter in guesses:
				print(f"{letter}", end=" ")
			else:
				print("_", end=" ")
		print()
		
	def check_guess(self, guess):
		"""Checks if the letter guessed by the user is in the phrase"""
		if guess.lower() in self.phrase:
			return True
		else:
			return False
	
	def check_complete(self, guesses):
		"""Checks if the user has guessed all the characters or not."""
		for letter in self.phrase:
			if letter not in guesses:
				return False
		return True
		