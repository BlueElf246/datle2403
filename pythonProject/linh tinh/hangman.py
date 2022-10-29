import random
name=input('what file store the puzzle words?')
while True:
    decide=input('Would you like to play hangman?(y/n)')
    if decide=='y':
        file=open(name,'r')
        string=''
        for line in file:
            line=line.strip()
            string+=line+' '
        lst=string.split(' ')
        random_num=random.randint(0,len(lst))
        random_word=lst[random_num]
        num=len(random_word)
        print('Here is your puzzle')
        string=list()
        for i in range(num):
            string.append('_')
        interface=''.join(string)
        print(interface)
        wrong_count = 0
        #make user guess
        while True:
            print(f'you currently have {wrong_count} wrong guesses!')
            count = 0
            while True:
                wrong = 0
                word_guess=input('choose you guess character')
                for x in string:
                    if x==word_guess:
                        print('this word already guessed, please try another word, now it count as a miss')
                        wrong+=1
                        wrong_count+=1
                        break
                if wrong==0:
                    break
            for x in range(len(random_word)):
                if random_word[x] == word_guess:
                    string[x]=word_guess
                    count+=1
            if count==0:
                print('sorry, your character do not have in answer')
                wrong_count+=1
            if count>0:
                print(f'Congratulation, you have {count} correct character')
            interface= ''.join(string)
            print(interface)
            if wrong_count==5:
                print('Sorry you have made 5 incorrect guesses, you lose')
                print(f'here is the answer {random_word}')
                break
            if '_' not in interface:
                print(f'Well done, you won the game, the answer is {interface}')
                break
    elif decide=='n':
        exit()
    else:
        print('please try again')
        continue







