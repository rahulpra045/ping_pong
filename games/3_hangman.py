

MAX_GUESSES = 10
tries = 0

word = "Country"
word = word.lower()
print(word)


while True:
    key = input("Guess letter: ")
    if key in word:
        print(word + " contains " + key)
        word = word.replace(key,"")
        if len(word) == 0:
            print("YOU WIN!!!")
            break
    else:
        print("Wrong")    
        tries = tries + 1
        if tries >= MAX_GUESSES:
            print("YOU LOST!!!")
            break
