import urllib.request
webUrl=urllib.request.urlopen('https://wordpress.org/plugins/about/readme.txt')
print("result code:"+str(webUrl.getcode()))
data=webUrl.read()
print(data)
