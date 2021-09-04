import requests

url = ''

def checkUrl(url):

    data = '"Content-Type": "value"'

    response = requests.get(url, data)
    #print(response.status_code)
    #print(response.headers['Content-Type'])

    rHeaders = response.headers['Content-Type']

    tmpArray = rHeaders.split("/")
    #print(tmpArray[0])

    if tmpArray[0] == "application":
        print(__name__ + " : " + tmpArray[0]) 
        return True
    else:
        print(__name__ + " : Not Application")
        return False


print(__name__)