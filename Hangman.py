
import random
import urllib.request

print ('time to play hangman')
words = urllib.request.urlopen('http://davidbau.com/data/words').read().decode("utf-8").split()

secret = random.choice(words)
guesses = 'aeiou'
turns = 5

while turns > 0:
  print()
  missed = 0
  for letter in secret:
    if letter in guesses:
      print (letter, end=" ")
    else:
      print ('_', end=" ")
      missed += 1
  print()
  print()
  
  if missed == 0:
    print ('You win!')
    break

  guess = input('guess a letter: ')
  guesses += guess
  
  if guess not in secret:
    turns -= 1
    print ('Nope.')
    print (turns, 'more turns')
    if turns < 5: print (' O ')
    if turns < 4: print (' \_|_/ ')
    if turns < 3: print (' | ')
    if turns < 2: print (' / \ ')
    if turns < 1: print (' d b ')
    print()
    if turns == 0:
      print ('The answer is', secret)