import requests
import urllib
import requests
import downloader


def checkUrl(url):
    data = '"Content-Type": "value"'
    response = requests.get(url, data)
    rHeaders = response.headers['Content-Type']

    tmpArray = rHeaders.split("/")

    if tmpArray[0] == "application":
        print(__name__ + " : " + tmpArray[0]) 
        downloader.startDownload(url)
        return True
    else:
        print(__name__ + " : Not Application")
        return False

#checkUrl('https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe')