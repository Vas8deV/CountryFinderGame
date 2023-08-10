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

def check(c):
    '''this function checks for the validity of rules of the game'''
    c=c.replace(' ','')
    if c.isdigit() or len(c)!=1:
        print('Enter only single alphabet, Try Again\n'
              'Numbers,Spaces & Null values are not considered as input')
        c=input('Guess:')
        check(c)
    else:
        c=c.lower()
        return c

# Main program
countries=[ 'Ethiopia', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola'
            ,'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 
            'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium'
            , 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Botswana', 'Brazil', 
            'Brunei', 'Bulgaria', 'Burkina', 'Burma', 'Burundi', 'Cambodia', 
            'Cameroon', 'Canada', 'Chad', 'Chile', 'China','Colombia',  'Cyprus'
            ,'Danzig','Denmark', 'Djibouti', 'Dominica',  'Ecuador', 'Egypt',
            'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon',  
            'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 
            'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 
            'Ireland','Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Morocco',
            'Mozambique', 'Namibia', 'Nauru', 'Nepal','Newfoundland', 
            'Netherlands', 'NewZealand', 'Nicaragua', 'Niger', 'Nigeria', 
            'Oman', 'Ottoman' ,'Empire', 'Pakistan', 'Palau', 'Panama', 
            'NorwayParaguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 
            'Somalia',  'Spain', 'SriLanka', 'Sudan','Swaziland', 'Sweden', 
            'Switzerland', 'Syria', 'Tajikistan','Tanzania', 'Thailand', 'Togo',
            'Tonga',  'Tunisia','Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 
            'Ukraine', 'Uruguay','Uzbekistan', 'Vanuatu', 'Venezuela','Vietnam',
            'Yemen', 'Zambia','zimbabwe']

# part which randomly selects from list and extracts necessary info
word=random.choice(countries);l=len(word)
word=word.lower()
ans=word[:]
print(f'It is a {l} letter word')
sample=l*'-'
count=0

# Loop which repeatedly calls the function to proceed the game and end the game 
# when the necessary conditions are satisfied
while count<10:
    if ans==sample:
        # part which ends the game reporting win and displaying answer
        print('You Win')
        print('You guessed all correct')
        print(f'It was {ans.center(l+6,"*")}')
        break
    n=input('Guess:')
    n=check(n)

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
    elif count==5:
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
### End of the program ###

