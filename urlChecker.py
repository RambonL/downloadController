import requests

def main():
    #print("Started")
    url = 'https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe'
    url2 = 'https://drive.google.com/uc?id=1QOmVDpd8hcVYqqUXDXf68UMDWQZP0wQV&export=download'
    url3 = 'https://www.google.com/'

    data = '"Content-Type": "value"'

    response = requests.get(url3, data)
    #print(response.status_code)
    #print(response.headers['Content-Type'])

    rHeaders = response.headers['Content-Type']

    tmpArray = rHeaders.split("/")
    #print(tmpArray[0])

    if tmpArray[0] == "application":
        return True
    else:
        return False
     
        #print("true")
    
    

    #headers=requests.head(url2).headers
    #downloadable = 'attachment' in headers.get('Content-Type', 'application/')
    #print(downloadable)
    #print("Part 2:revenge arc")
    #r = requests.get(url3,stream=True)
    #print(r.headers)

if __name__ == "__main__":
    main()
