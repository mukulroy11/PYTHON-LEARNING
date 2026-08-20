#Making HTTP Easier using urllib
#Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a files


import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#for line in fhand:
#    print(line.decode().strip()) #strip is used to remove line blw two line

counts = {}
for l in fhand:
    words = l.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
