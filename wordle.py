won = False
while won == False:
    word = "word"
    wordlist = list(word)
    inp = input("enter guess:")
    inputlist = list(inp)
    inppos = 0
    wordpos = 0
    userword = []
    for x in wordlist:
        if inputlist[inppos] == wordlist[wordpos]:
            userword.append(inputlist[inppos])
        elif inputlist[inppos] in wordlist:
            userword.append(inputlist[inppos]+"\u0332")
        wordpos += 1
        inppos += 1
    print("Your word:", userword)
    if userword == wordlist:
        won = True
        print("YOU WON")