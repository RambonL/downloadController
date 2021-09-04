import urllib.request

url = "https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe"

def Download_Progress(block_num, block_size, total_size):
    downloaded = block_num * block_size
    progress = int((downloaded/total_size)*100)
    print ("Download Progress",str(progress),"%")



def startDownload(url):
    tmpArray = url.split("/")
    i = len(tmpArray) - 1

    urllib.request.urlretrieve(url, 'D:/Downloads/' + tmpArray[i], reporthook=Download_Progress)
    print ("Finished")
