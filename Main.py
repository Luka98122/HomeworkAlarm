import requests
import pprint
import json

FILENAME = 'assigments.txt'

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
    "Veronauka" : "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d0%b2%d0%b5%d1%80%d0%be%d0%bd%d0%b0%d1%83%d0%ba%d0%b0/",
    "Gradansko" : "https://podrska.ossmarkovic.edu.rs/v-%d1%80%d0%b0%d0%b7%d1%80%d0%b5%d0%b4-%d0%b3%d1%80%d0%b0%d1%92%d0%b0%d0%bd%d1%81%d0%ba%d0%be/"
}





def debugGetLocalAssignments():
    newDict = {'Srpski': ['https://podrska.ossmarkovic.edu.rs/2020/10/14/%d0%b2%d0%b0%d0%b6%d0%bd%d0%be-%d0%be%d0%b1%d0%b0%d0%b2%d0%b5%d1%88%d1%82%d0%b5%d1%9a%d0%b5-%d0%b7%d0%b0-%d1%83%d1%87%d0%b5%d0%bd%d0%b8%d0%ba%d0%b5-5-1-5-2-%d0%b8-5-4-%d0%be%d0%b4%d0%b5%d1%99%d0%b5',
            'Важно обавештење за ученике 5/1, 5/2 и 5/4 одељења'],
 'Matematika': ['https://podrska.ossmarkovic.edu.rs/2020/10/12/5-15-35-4-%d0%be%d0%b1%d0%b0%d0%b2%d0%b5%d1%88%d1%82%d0%b5%d1%9a%d0%b5-%d0%b7%d0%b0-%d1%83%d1%87%d0%b5%d0%bd%d0%b8%d0%ba%d0%b5-%d0%bd%d0%b0-online-%d0%bd%d0%b0%d1%81%d1%82%d0%b0%d0%b2%d0%b8',
                '5-1,5-3,5-4 &#8211; Обавештење за ученике на online настави'],
 'Spanski': ['https://podrska.ossmarkovic.edu.rs/2020/10/13/10-%d0%b8-11-%d1%87%d0%b0%d1%81-%d0%b0%d0%b1%d0%b5%d1%86%d0%b5%d0%b4%d0%b0',
             '10. И 11. час Абецеда'],
 'Istorija': ['https://podrska.ossmarkovic.edu.rs/2020/10/06/%d0%bf%d1%80%d0%b0%d0%b8%d1%81%d1%82%d0%be%d1%80%d0%b8%d1%98%d0%b0',
              'Праисторија'],
 'Biologija': ['https://podrska.ossmarkovic.edu.rs/2020/10/08/%d1%85%d1%80%d0%b0%d0%bd%d0%b0-%d0%ba%d0%b0%d0%be-%d0%b8%d0%b7%d0%b2%d0%be%d1%80-%d0%b5%d0%bd%d0%b5%d1%80%d0%b3%d0%b8%d1%98%d0%b5-%d0%b8-%d0%b3%d1%80%d0%b0%d0%b4%d0%b8%d0%b2%d0%bd%d0%b8%d1%85-%d1%81',
               'Храна као извор енергије и градивних супстанци'],
 'Geografija': ['https://podrska.ossmarkovic.edu.rs/2020/10/06/%d0%be%d0%b1%d0%bb%d0%b8%d0%ba-%d0%b7%d0%b5%d0%bc%d1%99%d0%b5-%d0%b8-%d1%9a%d0%b5%d0%bd%d0%b0-%d1%81%d1%82%d1%80%d1%83%d0%ba%d1%82%d1%83%d1%80%d0%b0',
                'Облик Земље и њена структура'],
 'Likovno': ['https://podrska.ossmarkovic.edu.rs/2020/09/09/%d1%83%d0%b2%d0%be%d0%b4-%d1%83-%d0%bb%d0%b8%d0%ba%d0%be%d0%b2%d0%bd%d1%83-%d0%ba%d1%83%d0%bb%d1%82%d1%83%d1%80%d1%83',
             'Увод у ликовну културу'],
 'Fizicko': ['https://podrska.ossmarkovic.edu.rs/2020/09/25/%d0%bf%d1%80%d0%b0%d0%b2%d0%b8%d0%bb%d0%bd%d0%b0-%d0%b8%d1%81%d1%85%d1%80%d0%b0%d0%bd%d0%b0-%d0%b7%d0%b0-%d1%83%d1%87%d0%b5%d0%bd%d0%b8%d0%ba%d0%b5-%d0%be%d0%b4-5-8-%d1%80%d0%b0%d0%b7%d1%80%d0%b5',
             'ПРАВИЛНА ИСХРАНА'],
 'Tehnika': ['https://podrska.ossmarkovic.edu.rs/2020/10/12/%d1%81%d0%b0%d0%be%d0%b1%d1%80%d0%b0%d1%9b%d0%b0%d1%98-%d0%b2%d1%80%d1%81%d1%82%d0%b5-%d0%b8-%d1%81%d1%82%d1%80%d1%83%d0%ba%d1%82%d1%83%d1%80%d0%b0',
             'Саобраћај, врсте и структура'],
 'Informatika': ['https://podrska.ossmarkovic.edu.rs/2020/09/21/%d0%bd%d0%b0%d1%81%d1%82%d0%b0%d0%b2%d0%b0-%d0%bd%d0%b0-%d0%b4%d0%b0%d1%99%d0%b8%d0%bd%d1%83-%d0%b8%d0%b7-%d0%b8%d0%bd%d1%84%d0%be%d1%80%d0%bc%d0%b0%d1%82%d0%b8%d0%ba%d0%b5-%d0%b8-%d1%80%d0%b0',
                 'Настава на даљину из Информатике и рачунараства 5 разред'],
 'Engleski': ['https://podrska.ossmarkovic.edu.rs/2020/10/06/%d0%b4%d0%be%d0%bc%d0%b0%d1%9b%d0%b8-%d0%b7%d0%b0%d0%b4%d0%b0%d1%82%d0%b0%d0%ba-%d0%b7%d0%b0-%d0%bf%d0%b5%d1%80%d0%b8%d0%be-5-10-17-10-2020',
              'Домаћи задатак за перио 5.10.-17.10.2020.'],
 'Francuski': ["Didn't find this", 'No title'],
 'Muzicko': ['https://podrska.ossmarkovic.edu.rs/2020/10/10/%d0%bc%d1%83%d0%b7%d0%b8%d0%ba%d0%b0-%d0%bf%d1%80%d0%b0%d0%b8%d1%81%d1%82%d0%be%d1%80%d0%b8%d1%98%d0%b5-%d0%b4%d0%be%d0%bc%d0%b0%d1%9b%d0%b8-%d0%b7%d0%b0%d0%b4%d0%b0%d1%82%d0%b0%d0%ba',
             'Музика праисторије-домаћи задатак'],
 'Veronauka': ["Didn't find this", 'No title'],
 'Gradansko': ['https://podrska.ossmarkovic.edu.rs/2020/10/05/%d0%ba%d0%be%d0%bc%d0%b1%d0%b8%d0%bd%d0%be%d0%b2%d0%b0%d0%bd%d0%b0-%d0%bd%d0%b0%d1%81%d1%82%d0%b0%d0%b2%d0%b0-%d0%bf%d0%b0%d0%bd%d0%b4%d0%b5%d0%bc%d0%b8%d1%98%d0%b0-%d0%b8%d1%81%d0%ba%d1%83',
               'Комбинована настава, пандемија – искуства ђака  5/1, 5/2, 5/3, '
               '5/4']}
    return newDict

def getNewestAssignmentFromAll ():
    return debugGetLocalAssignments() # Don't talk to the server while developing
    subjectPrieviews = {}
    for subject in subjects.keys():
        a = getTitleText(subjects[subject])
        subjectPrieviews[subject]= a
    return subjectPrieviews

newDict = getNewestAssignmentFromAll()

print("-------------------------------------------------")

def getNewestAssignment (url):
    response = requests.get(url)
    html = response.text
    #FindsOpeningTag
    stringSearchedFor = 'class="post-text">'
    indexOfString = html.find(stringSearchedFor)

    # Find closing tag
    indexOfClosing = html.find('</p>', indexOfString)

    location = (html[indexOfString+len(stringSearchedFor):indexOfClosing])
    if indexOfString == -1:
        return "Nema lekcije"
    return location.replace("&hellip;", "").replace("&nbsp", "")



def dictDiff(oldDict,newDict):
    changes = {}
    for subject in oldDict.keys():
        if oldDict[subject] != newDict[subject]:
            changes[subject] = newDict[subject]
    
    return changes

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

def saveToFile (Filename, objecct):
    fp = open(Filename, "w")
    json.dump(objecct, fp)
    fp.close()

def readFromFile (Filename):
    try:
        fp = open(Filename, "r")
        parsedDict = json.load(fp)
        fp.close()
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
    return parsedDict

secondDict = {'Srpski': ['https://podrska.ossmarkovic.edu.rs/2020/10/14/%d0%b2%d0%b0%d0%b6%d0%bd%d0%be-%d0%be%d0%b1%d0%b0%d0%b2%d0%b5%d1%88%d1%82%d0%b5%d1%9a%d0%b5-%d0%b7%d0%b0-%d1%83%d1%87%d0%b5%d0%bd%d0%b8%d0%ba%d0%b5-5-1-5-2-%d0%b8-5-4-%d0%be%d0%b4%d0%b5%d1%99%d0%b5',
            'Важно обавештење за ученике 5/1, 5/2 и 5/4 одељења'],
 'Matematika': ['https://podrska.ossmarkovic.edu.rs/2020/10/12/5-15-35-4-%d0%be%d0%b1%d0%b0%d0%b2%d0%b5%d1%88%d1%82%d0%b5%d1%9a%d0%b5-%d0%b7%d0%b0-%d1%83%d1%87%d0%b5%d0%bd%d0%b8%d0%ba%d0%b5-%d0%bd%d0%b0-online-%d0%bd%d0%b0%d1%81%d1%82%d0%b0%d0%b2%d0%b8',
                '5-1,5-3,5-4 &#8211; Обавештење за ученике на online настави'],
 'Spanski': ['https://podrska.ossmarkovic.edu.rs/2020/10/13/10-%d0%b8-11-%d1%87%d0%b0%d1%81-%d0%b0%d0%b1%d0%b5%d1%86%d0%b5%d0%b4%d0%b0',
             '10. И 11. час Абецеда'],
 'Istorija': ['https://podrska.ossmarkovic.edu.rs/2020/10/06/%d0%bf%d1%80%d0%b0%d0%b8%d1%81%d1%82%d0%be%d1%80%d0%b8%d1%98%d0%b0',
              'Праисторија'],
 'Biologija': ['https://podrska.ossmarkovic.edu.rs/2020/10/08/%d1%85%d1%80%d0%b0%d0%bd%d0%b0-%d0%ba%d0%b0%d0%be-%d0%b8%d0%b7%d0%b2%d0%be%d1%80-%d0%b5%d0%bd%d0%b5%d1%80%d0%b3%d0%b8%d1%98%d0%b5-%d0%b8-%d0%b3%d1%80%d0%b0%d0%b4%d0%b8%d0%b2%d0%bd%d0%b8%d1%85-%d1%81',
               'Храна као извор енергије и градивних супстанци'],
 'Geografija': ['https://podrska.ossmarkovic.edu.rs/2020/10/06/%d0%be%d0%b1%d0%bb%d0%b8%d0%ba-%d0%b7%d0%b5%d0%bc%d1%99%d0%b5-%d0%b8-%d1%9a%d0%b5%d0%bd%d0%b0-%d1%81%d1%82%d1%80%d1%83%d0%ba%d1%82%d1%83%d1%80%d0%b0',
                'Облик Земље и њена структура'],
 'Likovno': ['https://podrska.ossmarkovic.edu.rs/2020/09/09/%d1%83%d0%b2%d0%be%d0%b4-%d1%83-%d0%bb%d0%b8%d0%ba%d0%be%d0%b2%d0%bd%d1%83-%d0%ba%d1%83%d0%bb%d1%82%d1%83%d1%80%d1%83',
             'Увод у ликовну културу'],
 'Fizicko': ['https://podrska.ossmarkovic.edu.rs/2020/09/25/%d0%bf%d1%80%d0%b0%d0%b2%d0%b8%d0%bb%d0%bd%d0%b0-%d0%b8%d1%81%d1%85%d1%80%d0%b0%d0%bd%d0%b0-%d0%b7%d0%b0-%d1%83%d1%87%d0%b5%d0%bd%d0%b8%d0%ba%d0%b5-%d0%be%d0%b4-5-8-%d1%80%d0%b0%d0%b7%d1%80%d0%b5',
             'ПРАВИЛНА ИСХРАНА'],
 'Tehnika': ['https://podrska.ossmarkovic.edu.rs/2020/10/12/%d1%81%d0%b0%d0%be%d0%b1%d1%80%d0%b0%d1%9b%d0%b0%d1%98-%d0%b2%d1%80%d1%81%d1%82%d0%b5-%d0%b8-%d1%81%d1%82%d1%80%d1%83%d0%ba%d1%82%d1%83%d1%80%d0%b0',
             'Саобраћај, врсте и структура'],
 'Informatika': ['https://podrska.ossmarkovic.edu.rs/2020/09/21/%d0%bd%d0%b0%d1%81%d1%82%d0%b0%d0%b2%d0%b0-%d0%bd%d0%b0-%d0%b4%d0%b0%d1%99%d0%b8%d0%bd%d1%83-%d0%b8%d0%b7-%d0%b8%d0%bd%d1%84%d0%be%d1%80%d0%bc%d0%b0%d1%82%d0%b8%d0%ba%d0%b5-%d0%b8-%d1%80%d0%b0',
                 'Настава на даљину из Информатике и рачунараства 5 разред'],
 'Engleski': ['https://podrska.ossmarkovic.edu.rs/2020/10/06/%d0%b4%d0%be%d0%bc%d0%b0%d1%9b%d0%b8-%d0%b7%d0%b0%d0%b4%d0%b0%d1%82%d0%b0%d0%ba-%d0%b7%d0%b0-%d0%bf%d0%b5%d1%80%d0%b8%d0%be-5-10-17-10-2020',
              'Домаћи задатак за перио 5.10.-17.10.2020.'],
 'Francuski': ["Didn't find this", 'No title'],
 'Muzicko': ['https://podrska.ossmarkovic.edu.rs/2020/10/10/%d0%bc%d1%83%d0%b7%d0%b8%d0%ba%d0%b0-%d0%bf%d1%80%d0%b0%d0%b8%d1%81%d1%82%d0%be%d1%80%d0%b8%d1%98%d0%b5-%d0%b4%d0%be%d0%bc%d0%b0%d1%9b%d0%b8-%d0%b7%d0%b0%d0%b4%d0%b0%d1%82%d0%b0%d0%ba',
             'Музика праисторије-домаћи задатак'],
 'Veronauka': ["Didn't find this", 'No title'],
 'Gradansko': ['https://podrska.ossmarkovic.edu.rs/2020/10/05/%d0%ba%d0%be%d0%bc%d0%b1%d0%b8%d0%bd%d0%be%d0%b2%d0%b0%d0%bd%d0%b0-%d0%bd%d0%b0%d1%81%d1%82%d0%b0%d0%b2%d0%b0-%d0%bf%d0%b0%d0%bd%d0%b4%d0%b5%d0%bc%d0%b8%d1%98%d0%b0-%d0%b8%d1%81%d0%ba%d1%83',
               'Комбинована настава, пандемија – искуства ђака  5/1, 5/2, 5/3, '
               '5/4']}

oldDict = readFromFile(FILENAME)
if len(oldDict) == 0:
    saveToFile(FILENAME, newDict)
    oldDict = readFromFile(FILENAME)

theDiff = dictDiff(newDict, oldDict)
print(theDiff)
saveToFile(FILENAME,newDict)

print("-----------------------")