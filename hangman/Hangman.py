from random import choice
data=open('words.txt','r')
word=choice(data.read().splitlines())
guessed=[]
wrong=[]
tries=10
while tries>0:
    out=''
    for letter in word:
        if letter in guessed:
            out=out+letter
        else:
            out=out+"-"
    if out==word:
        break
    print('Guess your letter',out)
    print(tries, "chances left")
    guess=input()
    if guess in guessed or guess in wrong:
        print('You have already guessed the word!!!Bad memory*=*')
    elif guess in word:
        print('Yay!!!')
        guessed.append(guess)
    else:
        print('Meh -_-')
        tries=tries-1
        wrong.append(guess)
    print()
if tries:
    print('You are genius.You got it!Gracias!',word)
else:
    print('You couldnt guess!',word,'Better luck next time!')
