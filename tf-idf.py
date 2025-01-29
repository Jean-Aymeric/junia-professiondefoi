import os


def getAllTF() -> dict:
    fileNames = getCleanTxtNamesFromDirectory("docs-txt-cleaned")
    words = []
    for fileName in fileNames:
        text = readTxtFile("docs-txt-cleaned/" + fileName)
        words = list(set(words + getAllWordsFromText(text)))

    fileName_Words_tf = {}
    for fileName in fileNames:
        text = readTxtFile("docs-txt-cleaned/" + fileName)
        fileName_Words_tf[fileName] = getTFFromText(text, words)

    return fileName_Words_tf


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


d = getAllTF()
for e in d.keys():
    print(e)
    print(d[e])
