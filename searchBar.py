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
    searchCleaned = cleanWordsInSearch(search, words) + " "
    searchTF = tf_idf.getTFFromText(searchCleaned, words)
    searchTF_IDF = {}
    for word in words:
        searchTF_IDF[word] = searchTF[word] * words_idf[list(words_idf.keys())[0]][word]["idf"]
    return searchTF_IDF


def scalar(vector1: dict, vector2: dict) -> float:
    result = 0
    for key in vector1.keys():
        result += vector1[key] * vector2[key]
    return result


def norm(vector: dict) -> float:
    result = 0
    for key in vector.keys():
        result += vector[key] ** 2
    return result ** 0.5


def similarity(vector1: dict, vector2: dict) -> float:
    normVector1 = norm(vector1)
    if normVector1 == 0:
        return 0
    normVector2 = norm(vector2)
    if normVector2 == 0:
        return 0
    return scalar(vector1, vector2) / (normVector1 * normVector2)


def extractVectorFromTF_IDF(tf_idf: dict) -> dict:
    result = {}
    for word in tf_idf.keys():
        result[word] = tf_idf[word]["tf-idf"]
    return result


def getAnswerFromSearch(search):
    global answer, fileName
    words_idf = tf_idf.getMatrix_TF_IDF()
    searchVector = vectorizeSearch(search, words_idf)
    answer = {}
    for fileName in words_idf.keys():
        fileVector = extractVectorFromTF_IDF(words_idf[fileName])
        answer[fileName] = similarity(searchVector, fileVector)
    return answer
