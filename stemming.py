# from nltk.stem import PorterStemmer

# stemmer = PorterStemmer()

# words = ["hindered", "played", "playfully", "studies", "study", "studying", "better"]

# for word in words:
#     stemmer_word = stemmer.stem(word)
#     print(word, "->", stemmer_word)

import re
pattern = r"\w+(?:’\w+)?|\d+|[^\w\s]"
print(re.findall(pattern, "I’m learning NLP in 2026!"))