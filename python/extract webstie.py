from urllib import urlopen
import re
pat = re.compile('<h2><a .*? href="(.*?)">(.*?)</a>')
text = urlopen('http://www.python.org/community/jobs').read()
for url,name in pat.findall(text):
    print '%s: %s' %(name,url)
