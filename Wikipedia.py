import wikipedia
while True:
    a=input('Welcome to information finder! ("exit" to quit): ')
    if a.lower()=='exit':
        break
    else:
        b=wikipedia.summary(a)
        print(b)
exit()
