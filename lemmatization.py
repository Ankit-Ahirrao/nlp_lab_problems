import spacy

nlp = spacy.load("en_core_web_sm")

text = "The children were playing happily and studies were completed."

doc = nlp(text)

for token in doc:
    print(f"{token.text:12} -> {token.lemma_}")