import urllib.request

url = input("Enter valid url ")
urllib.request.urlretrieve(url, './sample.html')