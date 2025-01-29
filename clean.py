import os


def getTxtNamesFromDirectory(directoryName: str) -> list[str]:
    txtFileNames = []
    for file in os.listdir(directoryName):
        if file.endswith(".txt"):
            txtFileNames.append(file)

    return txtFileNames


def deleteAllSpecialCharacterFromStr(textToClean) -> str:
    charactersToDelete = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<",
                          "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~", "\t", "’", "0", "1",
                          "2", "3", "4", "5", "6", "7", "8", "9", "•", "–"]
    for character in charactersToDelete:
        textToClean = textToClean.replace(character, " ")
    return textToClean


def deleteAllCRFromStr(textToClean: str) -> str:
    return textToClean.replace("\n", " ")


def replaceUpperCaseWithLowerCase(textToClean: str) -> str:
    return textToClean.lower()


def readTxt(txtFileName: str) -> str:
    with open(txtFileName, "r", encoding="utf-8") as file:
        return file.read()


def saveStrToTxt(textToSave, txtFileName):
    with open(txtFileName, "w", encoding="utf-8") as file:
        file.write(textToSave)
        file.close()


def cleanAllTxtFiles():
    txtFileNames = getTxtNamesFromDirectory("docs-txt")
    for txtFileName in txtFileNames:
        textToClean = readTxt("docs-txt/" + txtFileName)
        textToClean = deleteAllSpecialCharacterFromStr(textToClean)
        textToClean = deleteAllCRFromStr(textToClean)
        textToClean = replaceUpperCaseWithLowerCase(textToClean)
        saveStrToTxt(textToClean, "docs-txt-cleaned/" + txtFileName)
