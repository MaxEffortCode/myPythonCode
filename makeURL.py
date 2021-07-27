def makeURL(sentence):
    new_sentence=""
    sentence_split=sentence.split()
    for word in sentence_split:
        new_sentence+=word
        new_sentence+="%20"
    return new_sentence

print(makeURL("this is now a URL"))
