print('WORD GAME')
words = ['size','camel','came','gone','back','jazz','psychologies','apology']
lenght = len(words)

try:

    for word in words:
        user = int(input('Enter number 1 >'))
        if user in range(lenght+1):
            print(word)
            lent = len(word)
            print(lent)
        
        else:
            print('out ot range')
            break
    
        display = []
        for alpha in range(lent):
            if alpha not in display:
                display.append('_')
        print(' '.join(display))
        
    

        while True:
            user = input('spell>')
            if user in display:
                print('you have already enter this alphabet')
            for pos in range(lent):
                letter = word[pos]
                if user == letter:
                    display[pos] = letter
            print(' '.join(display))

            if '_' not in display:
                print('win...')
                break


except ValueError as error:
    print('enter digit within the range')
    print(error)

