import random

def num_dashes(secret_word, spaces):
    for i in range(len(secret_word)):
        if secret_word[i] == ' ':
            dashes.append(' ')
            spaces = True
        else:
            dashes.append('-')
    return "".join(dashes)

def get_guess():
    while True:
        guess = input('Guess: ').lower()
        if len(guess) == 1:
            if guess in guesses:
                print 'You have already guessed that letter!'
            else:
                guesses.append(guess)
                return guess
        else:
            print 'Your guess must be one character!'

def update_dashes(dashes, guess, guesses_left):
    new_dashes = []
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            new_dashes.append(guess)
        else:
            new_dashes.append(dashes[i])
    return "".join(new_dashes)
    
def noose(guesses_left):
    if guesses_left == 6:
        print '    ____'
        print '   |    |'
        print '   |'
        print '   |'
        print '   |'
        print '   |'
        print '___|___'
    elif guesses_left == 5:
        print '    ____'
        print '   |    |'
        print '   |    o'
        print '   |'
        print '   |'
        print '   |'
        print '___|___'
    elif guesses_left == 4:
        print '    ____'
        print '   |    |'
        print '   |    o'
        print '   |    |'
        print '   |    |'
        print '   |'
        print '___|___'
    elif guesses_left == 3:
        print '    ____'
        print '   |    |'
        print '   |    o'
        print '   |   /|'
        print '   |    |'
        print '   |'
        print '___|___'
    elif guesses_left == 2:
        print '    ____'
        print '   |    |'
        print '   |    o'
        print '   |   /|\\'
        print '   |    |'
        print '   |'
        print '___|___'
    elif guesses_left == 1:
        print '    ____'
        print '   |    |'
        print '   |    o'
        print '   |   /|\\'
        print '   |    |'
        print '   |   /'
        print '___|___'
    elif guesses_left == 0:
        print '    ____'
        print '   |    |'
        print '   |    o'
        print '   |   /|\\'
        print '   |    |'
        print '   |   / \\'
        print '___|___'

def print_hangman():
    print ' _    _          _   _  _____ __  __          _   _' 
    print '| |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |'
    print '| |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |'
    print '|  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |'
    print '| |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |'
    print '|_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|'
    
def which_word():
    while True:
        enter = input('Press 1 to enter a word, Press 2 for one to be selected: ').lower()
        if enter == 'yes':
            wrd = input('Enter your word:').lower()
            return wrd
        elif enter == 'no':
            return random.choice(words)
        else:
            print 'That is not a valid answer!'
    
words = ['powboy', 'kill me', 'weaboo cunt', 'xd', 'lil bean', 'snoop dogg']
secret_word = ''
dashes = []
win = False
guesses_left = 6
guesses = []
spaces = False

print_hangman()
secret_word = which_word()
dashes = num_dashes(secret_word, spaces)
for i in range(10):
    print ' '
while True:
    print_hangman()
    print ' '
    noose(guesses_left)
    print dashes
    guess = get_guess()
    dashes = update_dashes(dashes, guess, guesses_left)
    if guess not in secret_word:
        guesses_left -= 1
    for i in range(17):
        print ' '
    if secret_word == dashes:
        win = True
        break
    if guesses_left == 0:
        break
print_hangman()
print ' '
if win == True:
    noose(guesses_left)
    if spaces == true:
        print 'Congrats! You win. The phrase was: ' + secret_word
    else:
        print 'Congrats! You win. The word was: ' + secret_word
else:
    noose(guesses_left)
    if spaces == true:
        print 'You lose. The phrase was: ' + secret_word
    else:
        print 'You lose. The word was: ' + secret_word
