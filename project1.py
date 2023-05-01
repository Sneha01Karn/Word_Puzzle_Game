print("  ************     WORD PUZZLE GAME     ************  ")
print("              ***INSTRUCTIONS OF GAME***")
print(". You have to solve the puzzle for 5 words.")
print(". At a time one word will be displayed.")
print(". The word will be jumbled, you have to arrange letters to form a meaningful word.")
print(". Type answers in CAPITAL LETTERS.")
print(". For each right answer you will get 1 mark.")
print(". For each wrong answer -1 mark will be added to your score.")
print(". Blank answer will be concidered as wrong answer.")
print("\n\nAre you ready???\n**ALL THE BEST**\nPress 'ENTER' to start...\n\n")
input()
words_list={('R','A','F','E','H','T'),('K','A','B','R','E'),('C','Y','R','O','T','N','U'),('R','E','N','E','G'),('O','A','E','R','E','L','A','N','P'),('I','N','C','K','C','H','E'),('E','C','I','L','R','C'),('T','M','U','N','I','A','O','N'),('A','S','K','N','E'),('U','H','L','G','A')}
i=1
score=0
neg_score=0
for word in words_list:
    for letters in word:
        print(letters,end=" ")
    ans=input("\nArrange the letters to form a valid word:\n")
    match ans:
        case "FATHER":
            print("WELLDONE")
            score+=1
        case "BRAKE":
            print("WELLDONE")
            score+=1
        case "BREAK":
            print("WELLDONE")
            score+=1
        case "COUNTRY":
            print("WELLDONE")
            score+=1
        case "GREEN":
            print("WELLDONE")
            score+=1
        case "GENRE":
            print("WELLDONE")
            score+=1
        case "AEROPLANE":
            print("WELLDONE")
            score+=1
        case "CHICKEN":
            print("WELLDONE")
            score+=1
        case "CIRCLE":
            print("WELLDONE")
            score+=1
        case "MOUNTAIN":
            print("WELLDONE")
            score+=1
        case "SNAKE":
            print("WELLDONE")
            score+=1
        case "SNEAK":
            print("WELLDONE")
            score+=1
        case "LAUGH":
            print("WELLDONE")
            score+=1
        case _:
            print("ALAS!!, WRONG ANSWER")
            neg_score-=1
    i+=1
    if i>5:
        break
print("Your Final Score=",score+neg_score)
print("      ***PLAY AGAIN***      ")
print("      ***THANK YOU***     ")