import random

def num_dashes(secret_word):
    for i in range(len(secret_word)):
        if secret_word[i] == ' ':
            dashes.append(' ')
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
    
def which_word():
    while True:
        enter = input('Would you like to enter a word? ').lower()
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

print ' _    _          _   _  _____ __  __          _   _' 
print '| |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |'
print '| |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |'
print '|  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |'
print '| |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |'
print '|_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|'
secret_word = which_word()
dashes = num_dashes(secret_word)
for i in range(10):
    print ' '
while True:
    print ' _    _          _   _  _____ __  __          _   _' 
    print '| |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |'
    print '| |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |'
    print '|  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |'
    print '| |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |'
    print '|_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|'
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
print ' _    _          _   _  _____ __  __          _   _' 
print '| |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |'
print '| |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |'
print '|  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |'
print '| |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |'
print '|_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|'
print ' '
if win == True:
    noose(guesses_left)
    print 'Congrats! You win. The word was: ' + secret_word
else:
    noose(guesses_left)
    print 'You lose. The word was: ' + secret_word
