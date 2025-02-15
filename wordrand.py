import random as rand
print('WORD GAME')

words = ['size','camel','came','gone','back','jazz']
choice_word = rand.choice(words)
print(choice_word)
lenght = len(choice_word)
print(type(lenght))

live = 3
show = []
for alpha in choice_word:
    if alpha not in show:
        show.append('_')
print(show)
'''for every position in the range of lenght, replace the space with an alpha and input by the user'''
while True:
    user = input('enter an alphabet\n>')
    if user in show:
        print('you have already enter this alphabet')
    for position in range(lenght):
        alpha = choice_word[position]
        if user in alpha:
            show[position] = alpha       
    print(f"{' '.join(show)}")
    
    if user not in choice_word:
        live-=1
        if live == 0:
            print('Wrooong')
        break

    if '_' not in show:
        print('Correct')
        break        
            



        

