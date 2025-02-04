import clean
import searchBar
import transform

transform.transformAllPdfToTxt()
clean.cleanAllTxtFiles()

search = searchBar.getSearch()
while search != 'exit':

    search = searchBar.cleanSearch(search)
    answer = searchBar.getAnswerFromSearch(search)
    answer = dict(sorted(answer.items(), key=lambda item: item[1], reverse=True))

    for fileName in answer:
        print(fileName, ":", answer[fileName])
    search = searchBar.getSearch()
