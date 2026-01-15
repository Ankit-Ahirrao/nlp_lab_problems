from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "played", "playfully", "studies", "study", "studying", "better"]

for word in words:
    stemmer_word = stemmer.stem(word)
    print(word, "->", stemmer_word)