import random
name = input("What's your name:")
print("Good Luck! ",name)

words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

guesses = ''
turns = 12

while turns>0:
  fail = 0
  for char in word:
    if char in guesses:
      print(char)
    else:
      print("_")
      fail += 1

  if fail == 0:
      print("you win")
      print("the word is:",word)
      break;

  print("---------------------------")
  guess = input("guess a character:")
  guesses += guess


  if guess not in word:
    turns -= 1
    if turns == 0:
        print("you lose")
        break
    print("you entered incorrect ")
    print("you have ",turns," turns left")
    print("---------------------------")
