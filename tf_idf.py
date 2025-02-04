import math
import os


def getMatrix_TF_IDF() -> dict:
    fileNames = getCleanTxtNamesFromDirectory("docs-txt-cleaned")
    words = getAllWords(fileNames)

    fileName_Words_tf = {}
    for fileName in fileNames:
        text = readTxtFile("docs-txt-cleaned/" + fileName)
        fileName_Words_tf[fileName] = getTFFromText(text, words)

    return calculateTF_IDF(fileName_Words_tf, getAllIDF(fileName_Words_tf, words))


def calculateTF_IDF(fileName_Words_tf: dict, idfs: dict) -> dict:
    matrix_TF_IDF = {}
    for fileName in fileName_Words_tf.keys():
        matrix_TF_IDF[fileName] = {}
        tf_idf = {}
        for word in idfs:
            tf_idf[word] = {
                "tf": fileName_Words_tf[fileName][word],
                "idf": idfs[word],
                "tf-idf": fileName_Words_tf[fileName][word] * idfs[word]
            }
        matrix_TF_IDF[fileName] = tf_idf
    return matrix_TF_IDF


def getAllWords(fileNames) -> list[str]:
    words = []
    for fileName in fileNames:
        text = readTxtFile("docs-txt-cleaned/" + fileName)
        words = list(set(words + getAllWordsFromText(text)))
    return words


def getTFFromText(text: str, words: [str]) -> dict:
    words_tf = {}

    for word in words:
        words_tf[word] = countWordInText(text, word)
    return words_tf


def getAllWordsFromText(text: str) -> list[str]:
    words = set(text.split(' '))
    if '' in words:
        words.remove('')
    return list(words)


def countWordInText(text: str, word: str) -> int:
    return text.count(word + " ")


def readTxtFile(txtFileName) -> str:
    with open(txtFileName, "r", encoding="utf-8") as file:
        text = file.read()
        file.close()
        return text


def writeTxtFile(text: str, txtFileName: str):
    with open(txtFileName, "w", encoding="utf-8") as file:
        file.write(text)
        file.close()


def getCleanTxtNamesFromDirectory(directoryName: str) -> list[str]:
    txtFileNames = []
    for file in os.listdir(directoryName):
        if file.endswith(".txt"):
            txtFileNames.append(file)

    return txtFileNames


def countFiles(directoryName: str) -> int:
    nbFiles = 0
    for file in os.listdir(directoryName):
        if file.endswith(".txt"):
            nbFiles += 1

    return nbFiles


def countFilesWithWord(fileName_Words_tf: dict, word: str) -> int:
    nbFiles = 0
    for fileName in fileName_Words_tf.keys():
        if fileName_Words_tf[fileName][word] > 0:
            nbFiles += 1
    return nbFiles


def calcIDF(nbTotalFiles: int, nbFilesContainingWord: int) -> float:
    if nbFilesContainingWord == 0:
        return 0
    return math.log10(nbTotalFiles / nbFilesContainingWord)


def getAllIDF(fileName_Words_tf: dict, words: list[str]) -> dict:
    idfs = {}
    nbTotalFiles = countFiles("docs-txt-cleaned")
    for word in words:
        idfs[word] = calcIDF(nbTotalFiles, countFilesWithWord(fileName_Words_tf, word))
    return idfs

# d = getMatrix_TF_IDF()
# for e in d.keys():
#     print(e)
#     print(d[e])
# print("Documents : ", countFiles("docs-txt-cleaned"))
# print("Présent :", countFilesWithWord(d, "courses"))
# print(calcIDF(countFiles("docs-txt-cleaned"), countFilesWithWord(d, "courses")))
