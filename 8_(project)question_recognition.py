def question_finder(sentence):

    parameters = ("when", "why", "how", "what","where")

    capital = sentence.capitalize()
    # capital only starting letter of 1st word,,,,but title() capital the 1st letter of all words

    if sentence.startswith(parameters):
        return "{}?".format(capital)
    else:
        return "{}.".format(capital)

# print(question_finder("how are you"))


data = []
while True:
    yourdata = input("Type a sentence: ")

    if yourdata == 'stop':
        break
    else:
        data.append(question_finder(yourdata))
print(" ".join(data))
