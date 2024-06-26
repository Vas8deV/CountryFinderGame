# a simple module to simulate a word guessing game
import random

def modify(c,words,samples):
    '''this func() modifies the sample string such that only correct guess
    are visible to user and other remain the same"-" '''
    l=len(words)
    i=words.count(c)
    k=words.find(c)
    for j in range(i):
        pos=words.find(c,k)
        x=samples[:pos]+c+samples[pos+1:]
        samples=x
        k+=1
    return x    

#import words from text file
with open(r'F:\vasu ECE\python_work\country.txt', 'r') as file:
    countries = file.read().splitlines()

# part which randomly selects from list and extracts necessary info
words=random.choice(countries)
words=words.lower()


# Loop which repeatedly calls the function to proceed the game and end the game 
# when the necessary conditions are satisfied
def game(word):
    ans=word[:]
    l=len(word)
    print(f'It is a {l} letter word')
    sample=l*'_'
    count=0
    limit=l+3
    
    while count<limit:
        if ans==sample:
            # part which ends the game reporting win and displaying answer
            print('You Win')
            print('You guessed all correct')
            print(f'It was {ans.center(l+6,"*")}')
            break
        
        while True:
            n = input('Guess:')
            if n.isalpha() and len(n) == 1:
                break
            else:
                print('Enter only single alphabet, Try Again')

        # part which calls the function and string is altered
        if n in word and n!='':
            y=modify(n,ans,sample)
            sample=y
            print(sample)
            word=word.replace(n,'')
            continue
        
        # part which ensure that guesses are not repeated
        if n in sample and n!='':
            print('Already guessed')
            continue
        
        # part which ends the game and displays the answer
        elif count==limit-1:
            print('Wrong guess')
            print(f'Nice try {sample}')
            print('You lose')
            print(f'Answer was {ans.center(l+6,"*")}')    
            break

        # part which reports the user that the guess was wrong
        else:
            count+=1
            print('wrong guess, try another\n')
            print(sample)  
            continue  

game(words)
### End of the program ###

