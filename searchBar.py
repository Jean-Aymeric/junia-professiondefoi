import clean
import tf_idf


def getSearch() -> str:
    print("Entrez votre recherche :")
    return input()


def cleanSearch(search: str) -> str:
    return clean.cleanText(search)


def cleanWordsInSearch(search: str, words: []) -> str:
    wordsInSearch = search.split(' ')
    wordsInSearch = list(set(wordsInSearch).intersection(set(words)))
    return ' '.join(wordsInSearch)


def vectorizeSearch(search: str, words_idf: dict) -> dict:
    words = words_idf[list(words_idf.keys())[0]].keys()
    searchCleaned = cleanWordsInSearch(search, words)
    searchTF = tf_idf.getTFFromText(searchCleaned, words)
    searchTF_IDF = {}
    for word in words:
        searchTF_IDF[word] = searchTF[word] * words_idf[list(words_idf.keys())[0]][word]["idf"]
    return searchTF_IDF


search = getSearch()
search = cleanSearch(search)
words_idf = tf_idf.getMatrix_TF_IDF()
searchVector = vectorizeSearch(search, words_idf)
print(searchVector)
