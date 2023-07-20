import nltk
from nltk.corpus import wordnet

def get_synonyms(string):
    synonyms = []
    words = string.split()
    for word in words:
        synsets = wordnet.synsets(word)
        for synset in synsets:
            lemmas = synset.lemmas()
            for lemma in lemmas:
                synonym = lemma.name()
                if synonym not in synonyms:
                    synonyms.append(synonym)
    return synonyms

string = "hat"
synonyms = get_synonyms(string)

print(synonyms[:10])
