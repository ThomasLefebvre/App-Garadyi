from django.shortcuts import render
from django.http import HttpResponse
from .download_and_decompile import download_apk, decompileAPK
from .forms import CreateAndroidApp
from .static_analysis_functions import *
from .meta_info_functions import *
from .machine_learning_model_functions import *
from .virus_total import *
from . import forms
from .models import AndroidApp
from .filters import *
import json
from django.core import serializers




def home(request):


    #download_apk('com.lesmillsondemand')
    return render(request, 'Analysis/home.html')

def please_wait(request):
    appID = request.POST.get("handle")

    NewAndroidApp = AndroidApp(handle = appID)
    #NewAndroidApp.save()
    #print(AndroidApp.objects.all())
    #downloads APK

    downloadSuccessBoolean = download_apk(appID)
    NewAndroidApp.download_successful = downloadSuccessBoolean.get('Download')
    if downloadSuccessBoolean.get('Download') == True:
        NewAndroidApp.fileSize = os.path.getsize(joinProjectPath(returnAPKPath(appID)))

    NewAndroidApp.xapk = downloadSuccessBoolean.get('XAPK')
    #decompiles APK
    NewAndroidApp.decompile_successful = decompileAPK(appID)
    #gets permissions
    
    permissionList = getPermissionsList(appID)
    NewAndroidApp.PermissionsList = permissionList.get('PermissionList')
    NewAndroidApp.PermissionsProtectionLevelList = permissionList.get('ProtectionLevelList')
    if "dangerous" in permissionList.get('ProtectionLevelList'):
        NewAndroidApp.dangerous_permission = True
    else:
        NewAndroidApp.dangerous_permission = False

    print(permissionList)
    #returns two lists, one for their TPL's and one for what type of library
    thirdPartyReults = returnSmaliKey(appID)
    NewAndroidApp.ThirdPartyLibraryList = thirdPartyReults.get('library')
    NewAndroidApp.ThirdPartyLibraryCategoryList = thirdPartyReults.get('libraryCategory')
    if "Targeted ads" in thirdPartyReults.get('libraryCategory') or "Analytics" in thirdPartyReults.get('libraryCategory') or "Mobile Analytics" in thirdPartyReults.get('libraryCategory'):
        NewAndroidApp.ThirdPartyTrackingLibrary = True
    else:
        NewAndroidApp.ThirdPartyTrackingLibrary = False

    #gets certificate file - doesn't work
    #makeCertificateFile(appID)
    #gets meta info from website

    appMeta = metaFromWebsite(appID)
    NewAndroidApp.meta_info_installs = appMeta.get('Installs')
    NewAndroidApp.meta_info_rating = appMeta.get('Rating')
    NewAndroidApp.meta_info_description = appMeta.get('Description')
    NewAndroidApp.meta_info_developer = appMeta.get('Developer')
    NewAndroidApp.meta_info_last_update = appMeta.get('UpdatedDate')
    NewAndroidApp.meta_info_current_version = appMeta.get('CurrentVersion')
    NewAndroidApp.meta_info_android_version = appMeta.get('RequiresAndroid')
    NewAndroidApp.meta_info_developer_email = appMeta.get('DeveloperEmail')
    NewAndroidApp.meta_info_developer_website = appMeta.get('DeveloperWebsite')
    NewAndroidApp.privacy_policy_link = appMeta.get('PrivacyPolicyLink')


    #
    PrivacyPolicyResults = getPrivacyPolicyText(appMeta.get('PrivacyPolicyLink'))
    PrivacyPolicyText = PrivacyPolicyResults[0]
    PrivacyPolicyAccess = PrivacyPolicyResults[1]

    NewAndroidApp.privacy_policy_text = PrivacyPolicyText
    NewAndroidApp.privacy_policy_access = PrivacyPolicyAccess
    NewAndroidApp.privacy_policy_classification = PPShares3rdParty(PrivacyPolicyText)
    NewAndroidApp.privacy_policy_language = DetectLanguage(PrivacyPolicyText)


    NewAndroidApp.sha256 = getSha(appID)
    Virus_Total_Results = Virus_total_complete(appID)
    print(str(type(Virus_Total_Results)))
    print(Virus_Total_Results)
    NewAndroidApp.VT_msg = Virus_Total_Results.get('verbose_msg')
    NewAndroidApp.VT_Link = Virus_Total_Results.get('permalink')
    NewAndroidApp.VT_total_engines = Virus_Total_Results.get('total')
    NewAndroidApp.VT_positive_engines = Virus_Total_Results.get('positives')
    NewAndroidApp.VT_responseCode = Virus_Total_Results.get('response_code')
    NewAndroidApp.VT_resource = Virus_Total_Results.get('resource')


    NewAndroidApp.save()



    return render(request, 'Analysis/please_wait.html')

def database(request):
    print("in database")

    filter = AppFilter(request.GET, queryset = AndroidApp.objects.all().order_by('-id'))
    print("AndroidApp.objects.all():")
    print(AndroidApp.objects.all())


    test = "normie"
    #print("filter: ")
    #print(filter)
    #queryset = filter.qs
    #print("queryset: ")
    #print(queryset)

    context = {
        "object_list": queryset,
        "filter":filter,
        "test":test
    }

    return render(request, 'Analysis/database.html', context)


def getObject(request, id):
    obj = AndroidApp.objects.get(pk=id)
    data = serializers.serialize('json', [obj,])
    serialJSON = data
    jsonFile = open(joinProjectPath(returnJsonDumps('test')), "w")
    json.dump(serialJSON, jsonFile, indent = 2)
    jsonFile.close()
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data, mimetype='application/json')

# Create your views here.
