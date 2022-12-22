from hangman_words import word_list

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives=6




import random
chosen_word = random.choice(word_list)
print(f"the sol is {chosen_word}")
display=[]
for n in range(len(chosen_word)):
   display+='_'
print(display)
word_len=len(chosen_word)

game_end=False




while not game_end:
    guess = input("Guess a letter: ").lower()
    if guess in display:
          print("you have guessed the letter again")
    for position in range(word_len):
        letter = chosen_word[position]
    
        if letter == guess:
            display[position] = letter
        
        
    if guess not in chosen_word:
        print("error.....you have lost a life")
        lives-=1
        if(lives==0):
            print("you have lost all the lives!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("game over!!!!!!!!!!!!!!!!!!!!")
            game_end= True
        
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        game_end= True
        print("YOU WIN!!!!!!!!")

    print(stages[lives])