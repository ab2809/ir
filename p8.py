from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
import json

class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for (key, value) in attrs:
                if key == "href":
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links.append(newUrl)

    def getLinks(self, url):
        self.links = []
        self.baseUrl = url
        try:
            response = urlopen(url)
            content_type = response.getheader("Content-Type")
            if content_type and "text/html" in content_type:
                htmlBytes = response.read()
                htmlString = htmlBytes.decode("utf-8")
                self.feed(htmlString)
                response.close()
                return htmlString, self.links
        except:
            return "", []
        return "", []


def crawl(url, word):
    foundUrl = []
    visitedURL = []
    numberVisited = 0
    foundWord = False
    parser = LinkParser()
    data, links = parser.getLinks(url)
    links.append(url)
    for link in links:
        if link not in visitedURL:
            numberVisited += 1
            visitedURL.append(link)
            print(numberVisited, "Scanning URL:", link)
            data, li = parser.getLinks(link)
            if word.lower() in data.lower():
                foundWord = True
                foundUrl.append(link)
                print("Word found at:", link)
            else:
                print("Match not found")
    if not foundWord:
        print("The word", word, "was not found!")
    print("Finished, crawled", numberVisited, "pages")
    print(json.dumps(foundUrl, indent=2))
# Use a crawl-friendly site
crawl("https://www.instagram.com", "login")
