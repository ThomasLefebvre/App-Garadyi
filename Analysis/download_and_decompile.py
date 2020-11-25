from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import requests
import os
import shutil
import zipfile
from .filepaths import *


def search(query):
    res = requests.get('https://apkpure.com/search?q={}&region='.format(quote_plus(query)), headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) '
                      'Version/9.1.2 Safari/601.7.5 '
    }).text
    soup = BeautifulSoup(res, "html.parser")
    search_result = soup.find('div', {'id': 'search-res'}).find('dl', {'class': 'search-dl'})
    app_tag = search_result.find('p', {'class': 'search-title'}).find('a')
    download_link = 'https://apkpure.com' + app_tag['href']
    return download_link

def checkIfXAPK(soupString):
    lowerString = soupString.lower()

    xapkPos = lowerString.find("/b/xapk")
    print("xapk Position: "+str(xapkPos))
    if xapkPos == -1:
        return False
    else:
        return True


def download(link,app_id):
    print("Split: "+link.split('/')[-1])
    print("Length: "+str(len(link.split('/')[-1])))
    print("App ID: "+app_id)
    print("Length: "+str(len(app_id)))

    proxy = "49.135.46.8"

    if link.split('/')[-1] == app_id:
        res = requests.get(link + '/download?from=details', headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',

        }).text


        soup = BeautifulSoup(res, "html.parser").find('a', {'id': 'download_link'})


        if soup['href']:
            r = requests.get(soup['href'], stream=True, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) '
                              'Version/9.1.2 Safari/601.7.5 '
            })

            print("JUst before checking")
            if checkIfXAPK(str(soup)):
                print("Just after checking")
                with open(joinProjectPath(returnXAPKPath(link.split('/')[-1])), 'wb') as file:
                    print("opens xapk File")
                    for chunk in r.iter_content(chunk_size=1024):
                        #print("CHUNK")
                        if chunk:
                            file.write(chunk)
                            #print("WRITE")


                print("Before Extracting to ZIP")
                changeXAPKtoZIP(app_id)
                print("EXTRACTED TO ZIP")
                extractAPK(app_id)
                print("EXTRACTED CORRECT APK")
                #extract .apk file
                #delete other stuff
                return {'Download':True, 'XAPK': True}
            else:
                print("It is an APK")
                print("Extracting APK - Doing chunk stuff")
                appPath = returnAPKPath(link.split('/')[-1])
                print(appPath)
                #return r"ZIPDownloads\%s.apk"%app_id
                with open(joinProjectPath(appPath), 'wb') as file:
                    #print("Do we get in the loop")
                    #count = 0
                    for chunk in r.iter_content(chunk_size=1024):
                    #    print("chunk: "+str(count))
                    #    count = count+1
                        #print("Do we get in chunk loop the loop")
                        if chunk:
                            #print("do we get in the if statement")
                            file.write(chunk)
                            #print(chunk)
                            #print("do we be writing done")
                print("Done downloading APK.....Yay!")
                return {'Download':True, 'XAPK': False}

    else:
        print("Couldn't find app")
        return {'Download':False, 'XAPK': False}

def changeXAPKtoZIP(app_id):

    xapkPATH = joinProjectPath(returnXAPKZIP(app_id))
    apkPATH = joinProjectPath(returnAPKPath(app_id))
    zipPATH = joinProjectPath(returnAPKZIP(app_id))

    try:
        os.rename(xapkPATH, zipPATH)
        print("Changing XAPK to ZIP")
    except:
        print("zip file aready exists - in changeXAPKtoZip")




def extractAPK(app_id):

        apkPATH = joinProjectPath(returnAPKPath(app_id))
        zipPATH = returnAPKZIP(app_id)
        with zipfile.ZipFile(joinProjectPath(zipPATH)) as z:
            print(z)
            with z.open(app_id+".apk") as zf, open(apkPATH, 'wb') as f:
                shutil.copyfileobj(zf, f)


def download_apk(app_id):
    download_link = search(app_id)
    print("download_link: "+str(download_link))
    if download_link is not None:
        print('Downloading {}.apk ...'.format(download_link))
        print("download link: ")
        print(download_link)
        print(app_id)

        return download(download_link, app_id)


    else:
        print('No results')
        return False



def checkApkDownloaded(apkCode):
    apkPATH = returnAPKPath(apkCode)
    return os.path.exists(apkPATH)


def decompileAPK(apkCode):
    print(apkCode)
    if os.path.exists(joinProjectPath(returnAPKPath(apkCode))):
        os.chdir(joinProjectPath(filepaths_APKFolder))
        os.system("java -jar apktool.jar d "+apkCode +".apk")
        print("Decompile path")
        print(joinProjectPath(returnAPKFolder(apkCode)))
        if os.path.exists(joinProjectPath(returnAPKFolder(apkCode))):
            return True
        else:
            return False
        return True
    else:
        print("apk does not exist")
        print("path: "+str(returnAPKPath(apkCode)))
        return False
