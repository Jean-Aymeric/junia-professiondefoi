import os
import sys

from pypdf import PdfReader


def transformPdfToTxt(pdfFileName: str, txtFileName: str) -> None:
    reader = PdfReader(pdfFileName)
    sys.stdout.reconfigure(encoding='utf-8')
    outputTxt = ""
    for page in reader.pages:
        outputTxt += page.extract_text()

    with open(txtFileName, "w", encoding="utf-8") as file:
        file.write(outputTxt)
        file.close()


def deleteAllTxtInDirectory(directoryName: str) -> None:
    for file in os.listdir(directoryName):
        if file.endswith(".txt"):
            os.remove(directoryName + "/" + file)


def getPdfNamesFromDirectory(directoryName: str) -> list[str]:
    pdfFileNames = []
    for file in os.listdir(directoryName):
        if file.endswith(".pdf"):
            pdfFileNames.append(file)

    return pdfFileNames


def getTxtFileNameFromPdfFileName(pdfFileName: str) -> str:
    return pdfFileName.replace(".pdf", ".txt")


def transformAllPdfToTxt():
    pdfFileNames = getPdfNamesFromDirectory("docs-start")
    deleteAllTxtInDirectory("docs-txt")
    for pdfFileName in pdfFileNames:
        transformPdfToTxt("docs-start/" + pdfFileName,
                          "docs-txt/" + getTxtFileNameFromPdfFileName(pdfFileName))
