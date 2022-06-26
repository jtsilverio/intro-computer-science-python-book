from urllib.request import urlopen

r = urlopen("http://www.w3c.org/Consortium/facts.html") # type(r) == <class 'http.client.HTTPResponse'>

# HTTP response headers
for header in r.getheaders():
    print(header)

# Get HTML
html = r.read()
html = html.decode()
html.count("Web")

# Function to return html source
def getSource(url):
    response = urlopen(url)
    html = response.read().decode()
    return html

getSource("http://www.w3c.org/Consortium/facts.html")


## Parsing HTML
from html.parser import HTMLParser

class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    print(attr[1])
    
    def handle_endtag(self, tag)
                

parser = LinkParser()                     
parser.feed(html)
