import os
from os import chdir, system
import sys


filepaths_projectPath = r"C:\Users\jake_\OneDrive\Desktop\Web-Apps\App Garadyi\AppGaradyi"
filepaths_APKFolder = r"APKDownloads"
filepaths_CERTFolder = r"APKCertificates"
filepaths_OpenSSL = r"OpenSSL"
filepaths_NeuralNetworkModel = r"MachineLearning\finalized_model.sav"
#filepaths_APKList = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\media\APK_List\ManyApks.txt"
#filepaths_ResultsCSV = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\ThesisStuff\results.csv"
#filepaths_returnAPKPathCD = r"Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownload"
#filepaths_CERTFolder = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\certificate"
#filepaths_CertPemFolder = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\Cert Pem Files"
#filepaths_GeneralTrackingURLS = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\urlHeaderTextFiles\GeneralTrackingSystems.txt"
#filepaths_thesisList = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\ThesisStuff\thesisList.txt"
#filepaths_ManyAPKList = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\media\APK_List\ManyApks.txt"
#filepaths_AndroidMonkeyBin = r"C:\Users\jake_\AppData\Local\Android\Sdk\tools\bin"
#filepaths_NeuralNetworkModel = r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\corpus\Scikit_Model\finalized_model_91_percent.sav'

#filepaths_path = r""

def joinProjectPath(path):
    return os.path.join(filepaths_projectPath, path)

def returnAPKPath(app_id):
    return r"APKDownloads\%s.apk"%app_id
    #return os.path.join(r"APKDownloads", app_id+".apk")
def returnXAPKPath(app_id):
    return r"APKDownloads\%s.xapk"%app_id

def returnAPKZIP(app_id):
    return r"APKDownloads\%s.zip"%app_id
    #return os.path.join(r"ZIPDownloads\", app_id+".zip")

def returnAPKManifestPath(app_id):
    return r"APKDownloads\%s\AndroidManifest.xml"%app_id

def returnAPKFolder(app_id):
    return r"APKDownloads\%s"%app_id

def returnXAPKZIP(app_id):
    return r"APKDownloads\%s.xapk"%app_id

def returnJsonDumps(app_id):
    return r"JsonDumps\%s.txt"%app_id
