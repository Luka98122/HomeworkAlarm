import requests
import pprint

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



def getNewestAssignment (url):
    response = requests.get(url)
    html = response.text
    #FindsOpeningTag
    stringSearchedFor = 'class="post-text">'
    indexOfString = html.find(stringSearchedFor)

    # Find closing tag
    indexOfClosing = html.find('</p>', indexOfString)

    a = (html[indexOfString+len(stringSearchedFor):indexOfClosing])
    if indexOfString == -1:
        return "Nema lekcije"
    return a.replace("&hellip;", "").replace("&nbsp", "")

def getTitleText (url):
    response = requests.get(url)
    html = response.text
    #FindsOpeningTag
    stringSearchedFor = '<h2 class="entry-title fw-400">'
    indexOfString = html.find(stringSearchedFor)
    if indexOfString == -1:
        print("Didnt find this class")
        return ["Didn't find this", "No title"]
    indexOfClosing = html.find('</h2>')
    x = (html[indexOfString+len(stringSearchedFor):indexOfClosing])
    beginigLink = x.find("https:")
    endLink = x.find('/"')
    link = (x[beginigLink:endLink])

    titleSearchedFor = 'title="'
    titleStart = x.find(titleSearchedFor)
    titleEnd = x.find('">')
    title = x[titleStart+len(titleSearchedFor):titleEnd]

    returns = [link, title]

    return returns

def debugGetLocalAssignments():
    y = {'Srpski': ['https://podrska.ossmarkovic.edu.rs/2020/10/02/%d1%81%d0%b0%d0%be%d0%bf%d1%88%d1%82%d0%b5%d1%9a%d0%b5',
            '5. недеља, одељења 5/1, 5/2, 5/4'],
            'Matematika': ['https://podrska.ossmarkovic.edu.rs/2020/10/03/5-2-5-5-%d1%80%d0%b0%d1%81%d1%82%d0%b0%d0%b2%d1%99%d0%b0%d1%9a%d0%b5-%d0%b1%d1%80%d0%be%d1%98%d0%b5%d0%b2%d0%b0-%d0%bd%d0%b0-%d0%bf%d1%80%d0%be%d1%81%d1%82%d0%b5-%d1%87%d0%b8%d0%bd%d0%b8%d0%be%d1%86',
                            '5/2, 5/5 Растављање бројева на просте чиниоце и највећи '
                            'заједнички делилац'],
            'Spanski': ['https://podrska.ossmarkovic.edu.rs/2020/10/02/8-%d1%87%d0%b0%d1%81-%d0%be%d0%b4%d0%b3%d0%be%d0%b2%d0%b0%d1%80%d0%b0%d1%9a%d0%b5-%d0%b7%d0%b0-%d1%81%d0%b5%d0%bf%d1%82%d0%b5%d0%bc%d0%b1%d0%b0%d1%80-5-1-%d0%b8-5-2',
                        '8. час &#8211; Одговарање за септембар 5-1 и 5-2'],
            'Istorija': ['https://podrska.ossmarkovic.edu.rs/2020/09/28/%d0%b7%d0%b0%d0%b4%d0%b0%d1%86%d0%b8',
                        'Задаци'],
            'Biologija': ['https://podrska.ossmarkovic.edu.rs/2020/10/01/%d0%b8%d1%81%d1%85%d1%80%d0%b0%d0%bd%d0%b0-%d0%b8-%d1%82%d0%b8%d0%bf%d0%be%d0%b2%d0%b8-%d0%b8%d1%81%d1%85%d1%80%d0%b0%d0%bd%d0%b5',
                        'Исхрана и типови исхране'],
            'Geografija': ['https://podrska.ossmarkovic.edu.rs/2020/09/23/4-%d1%87%d0%b0%d1%81-%d1%81%d1%83%d0%bd%d1%87%d0%b5%d0%b2-%d1%81%d0%b8%d1%81%d1%82%d0%b5%d0%bc-26-31-%d1%81%d1%82%d1%80%d0%b0%d0%bd%d0%b0-%d1%83-%d1%83%d1%9f%d0%b1%d0%b5%d0%bd%d0%b8%d0%ba%d1%83',
                            '4. час: Сунчев систем (26-31. страна у уџбенику)'],
            'Likovno': ['https://podrska.ossmarkovic.edu.rs/2020/09/09/%d1%83%d0%b2%d0%be%d0%b4-%d1%83-%d0%bb%d0%b8%d0%ba%d0%be%d0%b2%d0%bd%d1%83-%d0%ba%d1%83%d0%bb%d1%82%d1%83%d1%80%d1%83',
                        'Увод у ликовну културу'],
            'Fizicko': ['https://podrska.ossmarkovic.edu.rs/2020/09/25/%d0%bf%d1%80%d0%b0%d0%b2%d0%b8%d0%bb%d0%bd%d0%b0-%d0%b8%d1%81%d1%85%d1%80%d0%b0%d0%bd%d0%b0-%d0%b7%d0%b0-%d1%83%d1%87%d0%b5%d0%bd%d0%b8%d0%ba%d0%b5-%d0%be%d0%b4-5-8-%d1%80%d0%b0%d0%b7%d1%80%d0%b5',
                        'ПРАВИЛНА ИСХРАНА'],
            'Tehnika': ['https://podrska.ossmarkovic.edu.rs/2020/09/28/%d0%b7%d0%b0%d0%bd%d0%b8%d0%bc%d0%b0%d1%9a%d0%b0-%d1%83-%d1%81%d0%b2%d0%b5%d1%82%d1%83-%d1%82%d0%b5%d1%85%d0%bd%d0%b8%d0%ba%d0%b5',
                        'Занимања у свету технике'],
            'Informatika': ['https://podrska.ossmarkovic.edu.rs/2020/09/21/%d0%bd%d0%b0%d1%81%d1%82%d0%b0%d0%b2%d0%b0-%d0%bd%d0%b0-%d0%b4%d0%b0%d1%99%d0%b8%d0%bd%d1%83-%d0%b8%d0%b7-%d0%b8%d0%bd%d1%84%d0%be%d1%80%d0%bc%d0%b0%d1%82%d0%b8%d0%ba%d0%b5-%d0%b8-%d1%80%d0%b0',
                            'Настава на даљину из Информатике и рачунараства 5 разред'],
            'Engleski': ['https://podrska.ossmarkovic.edu.rs/2020/10/02/%d0%bc%d0%b0%d1%82%d0%b5%d1%80%d0%b8%d1%98%d0%b0%d0%bb-%d0%b7%d0%b0-%d0%bd%d0%b5%d0%b4%d0%b5%d1%99%d1%83-5-10-9-10-2020',
                        'Материјал за недељу 5.10.-9.10.2020.'],
            'Francuski': ["Didn't find this", 'No title'],
            'Muzicko': ['https://podrska.ossmarkovic.edu.rs/2020/09/26/%d0%bc%d1%83%d0%b7%d0%b8%d0%ba%d0%b0-%d0%b0%d0%bd%d1%82%d0%b8%d1%87%d0%ba%d0%b5-%d0%b3%d1%80%d1%87%d0%ba%d0%b5-2',
                        'Музика Античке Грчке'],
            'Veronauka': ["Didn't find this", 'No title']}
    return y

def getNewestAssignmentFromAll ():
    return debugGetLocalAssignments() # Don't talk to the server while developing
    subjectPrieviews = {}
    for subject in subjects.keys():
        a = getTitleText(subjects[subject])
        subjectPrieviews[subject]= a
    return subjectPrieviews

y = getNewestAssignmentFromAll()
pprint.pp(y)
#print(y)
#x = getTitleText(subjects["Srpski"])
print("-------------------------------------------------")
#print(x)
