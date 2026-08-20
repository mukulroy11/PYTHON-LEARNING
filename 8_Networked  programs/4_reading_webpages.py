import urllib.request

url = 'https://www.dr-chuck.com/page1.htm'
fhand = urllib.request.urlopen(url)

for line in fhand:
    print(line.decode().strip())