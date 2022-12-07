import urllib.request
# print('Download is starting')
url=input('Enter a valid url: ')
urllib.request.urlretrieve(url,'./sample.html')
print('File donwloaded')