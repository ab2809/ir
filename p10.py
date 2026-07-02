import csv
import requests
import xml.etree.ElementTree as ET

def load_rss(url, filename):
    resp = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(resp.content)
    print(f"RSS feed loaded and saved to '{filename}'.")

def parse_xml(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    newsitems = []

    allowed_fields = {'guid', 'title', 'pubDate', 'description', 'link'}

    for item in root.findall('.//item'):
        news = {}

        for child in item:
            tag = child.tag.split('}')[-1] 

            if tag in allowed_fields:
                news[tag] = child.text

            if tag == 'content' and 'url' in child.attrib:
                news['media'] = child.attrib['url']
        newsitems.append(news)
    return newsitems

def save_to_csv(newsitems, filename):
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(newsitems)

    print(f"Data saved to '{filename}'.")

# Main function
def main():
    # Choose any one RSS link
    rss_url = 'http://feeds.bbci.co.uk/news/rss.xml'
    # rss_url = 'https://timesofindia.indiatimes.com/rssfeedstopstories.cms'
    # rss_url = 'https://feeds.feedburner.com/50WordStories'

    xml_filename = 'news.xml'
    csv_filename = 'news.csv'

    load_rss(rss_url, xml_filename)
    newsitems = parse_xml(xml_filename)
    save_to_csv(newsitems, csv_filename)

if __name__ == "__main__":
    main()

#news.xml

<?xml version="1.0" encoding="UTF-8"?>

<rss>
    <channel>

        <item>
            <guid>1</guid>
            <title>Python Practical</title>
            <pubDate>10 June 2026</pubDate>
            <description>Learning XML Parsing</description>
            <link>https://example.com/python</link>
        </item>

        <item>
            <guid>2</guid>
            <title>Information Retrieval</title>
            <pubDate>11 June 2026</pubDate>
            <description>RSS Feed Example</description>
            <link>https://example.com/ir</link>
        </item>

    </channel>
</rss>

#news.csv
guid,title,pubDate,description,link,media
guid,title,pubDate,description,link,media
1,Python Practical,10 June 2026,Learning XML Parsing,https://example.com/python,
2,Information Retrieval,11 June 2026,RSS Feed Example,https://example.com/ir,
