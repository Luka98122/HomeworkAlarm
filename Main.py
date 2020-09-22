import requests

url = "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d1%88%d0%bf%d0%b0%d0%bd%d1%81%d0%ba%d0%b8-%d1%98%d0%b5%d0%b7%d0%b8%d0%ba/"

def getNewestAssignment (url):
    response = requests.get(url)
    html = response.text
    #FindsOpeningTag
    stringSearchedFor = 'class="post-text">'
    indexOfString = html.find(stringSearchedFor)
    l = indexOfString + len(stringSearchedFor)

    # Find closing tag
    indexOfClosing = html.find('</p>', indexOfString)
    return (html[indexOfString+len(stringSearchedFor):indexOfClosing])

a = getNewestAssignment(url)
print(a)