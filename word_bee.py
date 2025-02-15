print('WORD GAME')
words = ['size','camel','came','gone','back','jazz','psychologies','apology']
lenght = len(words)
try:
    for word in words:
        user = int(input('enter next>'))
        if user in range(lenght):
            print(word)
            # if words[0]:
            #     print('s','o','z','p','e','i')
            # if words[1]:
            #     print('a','l','c','p','e','m')
            # if words[2]:
            #     print('m','o','c','a','e','c')
            # if words[3]:
            #     print('n','o','z','g','e','i')
            # if words[4]:
            #     print('a','c','b','k','e','i')
            # if words[5]:
            #     print('j','z','z','m','a')
            # if words[6]:
            #     print('s','o','z','p','e','i')
            # if words[7]:   
            #     print('s','o','z','p','e','i') 
        else:
            print('out of range')
            break
    
        show = []
        for _ in word:
            if _ not in show:
                show.append("_")
        print(show)
    
        while True:
            user = input('enter an alpha >')
            if user in show:
                print('Already exist')
            for posi in range(len(word)):
                alpha = word[posi]
                if user == word:
                    show[posi] = alpha
            print(' '.join(show))
            
            if ' ' not in show and user == word:
                print('win...')
                break
except:
    print('error')
