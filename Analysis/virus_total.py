import os, sys, codecs, fnmatch, time, binascii, requests, json, sqlite3, hashlib
from bs4 import BeautifulSoup
from subprocess import call
from .filepaths import *

def getSha(app_id):
    filename = returnAPKPath(app_id)
    print('here')
    with open(joinProjectPath(filename),"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
    return readable_hash

def vt_uploadfile(app_id):
    #this will search on virustotal by the Sha256 of the .apk file, I will need to figure out a way so that if the sha256
    #doesnt work because nobody has uploaded that .apk to VT before, then it uploads the file to VT
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'

    params = {'apikey': '1162652624083e2616b2200d64c68d4ae92722b952c88418d46e46c14383ccae'}

    #filename = os.path.join("C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", app_id+".apk")
    print("Do we get the declare filename")
    filename = returnAPKPath(app_id)
    files = {'file': ('%s' % app_id, open(filename, 'rb'))}
    print("files: ")
    print(str(files))

    response = requests.post(url, files=files, params=params)

    print("do we get a response:")
    print(response)


    print(str(response.json()))
    print(str(type(response.json())))
    print("done uploading file to virustotal")
    return response.json()

def vt_scan(app_id):
    #this will search on virustotal by the Sha256 of the .apk file, I will need to figure out a way so that if the sha256
    #doesnt work because nobody has uploaded that .apk to VT before, then it uploads the file to VT
    unsuccessfulSha = False
    url = 'https://www.virustotal.com/vtapi/v2/file/report'

    APKPath = returnAPKPath(app_id)
    #params = {'apikey': '1162652624083e2616b2200d64c68d4ae92722b952c88418d46e46c14383ccae', 'resource':APKPath }

    sha = str(getSha(app_id))
    print("App id: "+app_id)
    print("Sha: "+sha)

    params = {'apikey': '1162652624083e2616b2200d64c68d4ae92722b952c88418d46e46c14383ccae', 'resource':sha }

    try:
        response = requests.get(url, params=params)
    except Exception as e:
        print("Couldn't get response from virustotal")
        print("e")
        unsuccessfulSha = True
    js = response.json()


    jsonPath = returnAPKVirusTotal(app_id)
    jsonFile = open(jsonPath, "w")
    json.dump(response.json(), jsonFile, indent = 2)

    try:
        permalink = js['permalink']
        sha1 = js['sha1']
        resource = js['resource']
        response_code = js['response_code']
        scan_id = js['scan_id']
        verbose_msg = js['verbose_msg']
        sha256 = js['sha256']
        md5 = js['md5']
        total = js['total']
        positives = js['positives']
    except:
        #If file hasnt been uploaded before, upload it and check again later
        unsuccessfulSha = True
        try:
            print("----------------uploading APK to VT")
            uploadResponse = vt_uploadfile(app_id)
            try:
                hash = uploadResponse.get('resource')
                return vt_scan_onlyHashLookup(uploadResponse.get('resource'))
            except:
                print("cant get resource")


        except Exception as e:
            #If couldnt upload, don't worry about it
            print("----------------Error uploading to VT")
            print(e)

            unsuccessfulSha = False


        permalink = "NA"
        sha1 = "NA"
        resource = "NA"
        response_code = "NA"
        scan_id = "NA"
        verbose_msg = "NA"
        sha256 = "NA"
        md5 = "NA"
        total = "NA"
        positives = "NA"


    list = [permalink,sha1,resource,response_code,scan_id,verbose_msg,sha256,md5,total, positives]
    dictionary ={'list':list, 'checkVTLater':unsuccessfulSha}
    return dictionary


def vt_scan_onlyHashLookup(hash):
    #this will search on virustotal by the Sha256 of the .apk file, I will need to figure out a way so that if the sha256
    #doesnt work because nobody has uploaded that .apk to VT before, then it uploads the file to VT

    url = 'https://www.virustotal.com/vtapi/v2/file/report'


    #params = {'apikey': '1162652624083e2616b2200d64c68d4ae92722b952c88418d46e46c14383ccae', 'resource':APKPath }

    sha = hash

    print("Sha: "+sha)

    params = {'apikey': '1162652624083e2616b2200d64c68d4ae92722b952c88418d46e46c14383ccae', 'resource':sha }

    try:
        response = requests.get(url, params=params)
    except Exception as e:
        print("Couldn't get response from virustotal")
        print("e")

    js = response.json()

    return js

def get_permissions(app_id):
    '''Path to AndroidManifest File'''
    #base_path = '/Users/ikr001/VPNdroid/googleplay-api/adblockingApps/xmls/%s-xml.txt'% app_id
    #base_path = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\AndroidManifest.xml"

    soup = BeautifulSoup(open(base_path, "rb").read(), "lxml")

    apps_all_features = {}
    feature_list = []
    try:
        for x in soup.findAll('uses-feature'):
            feature_list.append(x.attrs['android:name']+"::"+x.attrs['android:required'])
    except:
        pass

    apps_all_features.update({app_id:feature_list})

    apps_all_permissions = {}
    perm_list = []
    try:
        for x in soup.findAll('uses-permission'):
            perm_list.append(x.attrs['android:name'])

        for x in soup.findAll('service'):
            try:
                perm_list.append(x.attrs['android:permission'])
            except:
                pass
    except:
        pass

    apps_all_permissions.update({app_id:perm_list})

    return app_id, apps_all_permissions, apps_all_features

def isFileSizeLessthan32MB(path):
    if os.path.getsize(path) < 32000000:
        return True
    else:
        return False

def Virus_total_complete(appID):
    hash = getSha(appID)
    path = returnAPKPath(appID)
    response = vt_scan_onlyHashLookup(hash)
    print(str(type(response)))
    print(response)
    print(response.get('verbose_msg'))
    if response.get('verbose_msg') == 'The requested resource is not among the finished, queued or pending scans':
        print("File not uploaded")
        if isFileSizeLessthan32MB(joinProjectPath(path)):
            print("Is less than 32mb")
            return vt_uploadfile(appID)

        return response
    else:
        print("File uploaded")
        return response
