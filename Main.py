import requests

subjects = {
    "Srpski" : "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d1%81%d1%80%d0%bf%d1%81%d0%ba%d0%b8-%d1%98%d0%b5%d0%b7%d0%b8%d0%ba/",
    "Matematika" : "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d0%bc%d0%b0%d1%82%d0%b5%d0%bc%d0%b0%d1%82%d0%b8%d0%ba%d0%b0/",
    "Spanski" : "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d1%88%d0%bf%d0%b0%d0%bd%d1%81%d0%ba%d0%b8-%d1%98%d0%b5%d0%b7%d0%b8%d0%ba/",
    "Istorija" : "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d0%b8%d1%81%d1%82%d0%be%d1%80%d0%b8%d1%98%d0%b0/",
    "Biologija" : "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d0%b1%d0%b8%d0%be%d0%bb%d0%be%d0%b3%d0%b8%d1%98%d0%b0/",
    "Geografija" : "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d0%b3%d0%b5%d0%be%d0%b3%d1%80%d0%b0%d1%84%d0%b8%d1%98%d0%b0/",
    "Likovno" : "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d0%bb%d0%b8%d0%ba%d0%be%d0%b2%d0%bd%d0%b0-%d0%ba%d1%83%d0%bb%d1%82%d1%83%d1%80%d0%b0/",
    "Fizicko" : "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d1%84%d0%b8%d0%b7%d0%b8%d1%87%d0%ba%d0%be-%d0%b2%d0%b0%d1%81%d0%bf%d0%b8%d1%82%d0%b0%d1%9a%d0%b5/",
    "Tehnika" : "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d1%82%d0%b5%d1%85%d0%bd%d0%b8%d0%ba%d0%b0-%d0%b8-%d1%82%d0%b5%d1%85%d0%bd%d0%be%d0%bb%d0%be%d0%b3%d0%b8%d1%98%d0%b0/",
    "Informatika" : "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d0%b8%d0%bd%d1%84%d0%be%d1%80%d0%bc%d0%b0%d1%82%d0%b8%d0%ba%d0%b0/",
    "Engleski" : "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d0%b5%d0%bd%d0%b3%d0%bb%d0%b5%d1%81%d0%ba%d0%b8-%d1%98%d0%b5%d0%b7%d0%b8%d0%ba/",
    "Francuski" : "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d1%84%d1%80%d0%b0%d0%bd%d1%86%d1%83%d1%81%d0%ba%d0%b8-%d1%98%d0%b5%d0%b7%d0%b8%d0%ba/",
    "Muzicko" : "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d0%bc%d1%83%d0%b7%d0%b8%d1%87%d0%ba%d0%b0-%d0%ba%d1%83%d0%bb%d1%82%d1%83%d1%80%d0%b0/",
    "Veronauka" : "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d0%b2%d0%b5%d1%80%d0%be%d0%bd%d0%b0%d1%83%d0%ba%d0%b0/"
}

url = "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d1%88%d0%bf%d0%b0%d0%bd%d1%81%d0%ba%d0%b8-%d1%98%d0%b5%d0%b7%d0%b8%d0%ba/"

def getNewestAssignment (url):
    response = requests.get(url)
    html = response.text
    #FindsOpeningTag
    stringSearchedFor = 'class="post-text">'
    indexOfString = html.find(stringSearchedFor)

    # Find closing tag
    indexOfClosing = html.find('</p>', indexOfString)
    return (html[indexOfString+len(stringSearchedFor):indexOfClosing])

a = getNewestAssignment(url)
print(a)
