from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import urllib.request
from urllib.request import Request, urlopen

def metaFromWebsite(appID):
    URL = "https://play.google.com/store/apps/details?id="+appID+"&hl=en_AU"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    print("we get here")
    links = getDeveloperLinks(soup)
    print("we dont get here")

    titleForResult = [e.get_text(separator=" ").strip() for e in soup.find_all("div",{"class":"BgcNfc"})]
    result = [e.get_text(separator=" ").strip() for e in soup.find_all("div",{"class":"hAyfc"})]
    rating = soup.find("div",{"class":"BHMmbe"}).get_text(separator=" ").strip()
    description = soup.find("div",{"class":"DWPxHb"}).get_text(separator=" ").strip()


    Meta = []
    #Meta.append(titleForResult)
    #Meta.append(result)
    mergedMetaList = mergeLists(titleForResult, result)
    Meta.append(mergedMetaList.get('result'))
    Meta.append(rating)
    Meta.append(description)
    Meta.append(links)
    Meta.append(mergedMetaList.get('numInstalls'))
    Meta.append(mergedMetaList.get('developer'))


    print('Meta')
    print(Meta)
    print("Merged meta List")
    print(mergedMetaList)
    print(mergedMetaList.get('Updated'))
    MetaDict = {'Installs':mergedMetaList.get('numInstalls'),'Developer':mergedMetaList.get('developer'),'Description':description, 'Rating':rating,
    'UpdatedDate': mergedMetaList.get('result').get('Updated'), 'CurrentVersion': mergedMetaList.get('result').get('Current Version'),
    'RequiresAndroid':mergedMetaList.get('result').get('Requires Android'),'PrivacyPolicyLink': links.get("Privacy Policy"),
    'DeveloperWebsite': links.get("Developer Website"), 'DeveloperEmail': links.get("Developer Email") }
    return MetaDict


def getDeveloperLinks(soup):

    string = ""

    #print(soup)
    for test in soup.find_all("div",{"class":"hAyfc"}):
        stringTest = str(test)


        DeveloperWebsite = ""
        DeveloperEmail = ""
        PrivacyPolicy = ""
        #print("we get here")
        if "<div class=\"BgcNfc\">Developer" in stringTest:
            if stringTest.find("hrTbp\" href=") > 1:
                websitePos = stringTest.find(">Visit website")
                QuoteLast = stringTest.rfind('\"',0,websitePos)

                QuoteSecond = stringTest.rfind('\"',0,QuoteLast)

                DeveloperWebsite = stringTest[QuoteSecond+1:QuoteLast]
                print(DeveloperWebsite)

            if stringTest.find("hrTbp euBY6b\" href=") > 1:
                websitePos = stringTest.find("hrTbp euBY6b\" href=")+27
                endWebPost =stringTest.find('"',websitePos+2)

                DeveloperEmail = stringTest[websitePos:endWebPost]

            if stringTest.find(">Privacy Policy") > 1:
                PrivacyPos = stringTest.find(">Privacy Policy")

                QuoteLast = stringTest.rfind('\"',0,PrivacyPos)

                QuoteSecond = stringTest.rfind('\"',0,QuoteLast)

                PrivacyPolicy = stringTest[QuoteSecond+1:QuoteLast]
                #print(PrivacyPolicy)
                #now i need to find last two substrings before PrivacyPos (" " "), and get the reference there


        links = {"Developer Website":DeveloperWebsite,"Developer Email":DeveloperEmail,"Privacy Policy":PrivacyPolicy}


    return links


def mergeLists(listA, listB):
    numInstalls = 0
    developer = ""
    result = {}
    for a in listA:
        for b in listB:


            editedString = b.replace(a+" ", "")

            if(a == "Installs"):
                editedString = editedString.replace(",","")
                editedString = editedString.replace("+","")
                numInstalls = int(editedString)

            if(a == "Offered By"):
                editedString = editedString.replace(",","")
                developer = editedString

            result[a] = editedString

            listB.remove(b)
            break
    dict = {'result':result, 'numInstalls':numInstalls, 'developer':developer}
    return dict


def getPrivacyPolicyText(link):
    PPAccess = True
    if link == '' or link == None:
        print("non existent link")
        PPAccess = False
        return "No Privacy Policy", PPAccess
    print("link: "+link)
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) '
                  'Version/9.1.2 Safari/601.7.5 '})
    try:

        # need to do this because: https://stackoverflow.com/questions/50085366/permissionerror-winerror-31-a-device-attached-to-the-system-is-not-functioning

        html = text_from_html(urllib.request.urlopen(req).read())
        #print("Text from HTML File ----------------")
        #print(html)
        #print("end of HTML Text -------------------")
        return html.replace("\n", " ").replace("\t", " ").replace("     ", " ").replace(",", " ").replace("\"", ""), PPAccess
    except Exception as e:
        print("ERROR TRYING TO GET TEXT FROM HTML--------------")
        html = str(e)
        print("error: "+html)
        PPAccess = False
        return html, PPAccess


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
