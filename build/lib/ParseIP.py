from html.parser import HTMLParser
import urllib.request

class MyHTMLParser(HTMLParser):

    def __init__(self,*, convert_charrefs: bool = ...) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.body = False
        self.ip = ''

    def handle_starttag(self, tag, attr):
        if tag == 'body':
            #print("Found a start tag:", tag)
            self.body = True

    def handle_endtag(self, tag):
        if tag == 'body':
            #print("Found end tag :", tag)
            self.body = False

    def handle_data(self, data):
        if self.body is True:
            #print("Found some data :", data)
            self.ip = data

myparser = MyHTMLParser()
with urllib.request.urlopen('http://checkip.dyndns.org/') as response:
    # html = str(response.read())
    html = response.read().decode('utf-8')
myparser.feed(html)
ipaddress = myparser.ip.split(': ')[1]
print(ipaddress)