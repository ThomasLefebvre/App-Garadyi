from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import ListCharField
from django.db.models import CharField

# Create your models here.

class AndroidApp(models.Model):
    handle = models.CharField(max_length=200)
    date_analysed = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    fileSize = models.CharField(max_length=30, blank=True, null=True)
    sha256 = models.CharField(max_length=200, blank=True, null=True)
    download_successful = models.BooleanField(blank=True, null=True)
    xapk = models.BooleanField(blank=True, null=True)
    decompile_successful = models.BooleanField(blank=True, null=True)
    VT_Link = models.CharField(max_length=100, blank=True, null=True)
    VT_responseCode = models.CharField(max_length=100, blank=True, null=True)
    VT_resource = models.CharField(max_length=100, blank=True, null=True)
    VT_scanId = models.CharField(max_length=100, blank=True, null=True)
    VT_msg = models.CharField(max_length=100, blank=True, null=True)
    VT_total_engines = models.CharField(max_length=100, blank=True, null=True)
    VT_positive_engines = models.CharField(max_length=100, blank=True, null=True)
    privacy_policy_link = models.CharField(max_length=200, blank=True, null=True)
    privacy_policy_text = models.CharField(max_length=10000, blank=True, null=True)
    privacy_policy_language = models.CharField(max_length=5, blank=True, null=True)
    privacy_policy_classification = models.BooleanField(blank=True, null=True)
    privacy_policy_access = models.BooleanField(blank=True, null=True)
    dangerous_permission = models.BooleanField(blank=True, null=True)
    PermissionsList = ListCharField(
        base_field=CharField(max_length=99),
        size=50,
        max_length=(100 * 50),  # 6 * 10 character nominals, plus commas
        blank = True,
        null = True
    )
    PermissionsProtectionLevelList = ListCharField(
        base_field=CharField(max_length=99),
        size=50,
        max_length=(100 * 50),  # 6 * 10 character nominals, plus commas
        blank = True,
        null = True
    )
    ThirdPartyTrackingLibrary = models.BooleanField(blank=True, null=True)
    ThirdPartyLibraryList = ListCharField(
        base_field=CharField(max_length=99),
        size=50,
        max_length=(100 * 50),  # 6 * 10 character nominals, plus commas
        blank = True,
        null = True
    )
    ThirdPartyLibraryCategoryList = ListCharField(
        base_field=CharField(max_length=99),
        size=50,
        max_length=(100 * 50),  # 6 * 10 character nominals, plus commas
        blank = True,
        null = True
    )
    meta_info_rating = models.CharField(max_length=100, blank=True, null=True)
    meta_info_installs = models.CharField(max_length=100, blank=True, null=True)
    meta_info_developer = models.CharField(max_length=100, blank=True, null=True)
    meta_info_developer_email = models.CharField(max_length=100, blank=True, null=True)
    meta_info_developer_website = models.CharField(max_length=100, blank=True, null=True)
    meta_info_last_update = models.CharField(max_length=100, blank=True, null=True)
    meta_info_size = models.CharField(max_length=100, blank=True, null=True)
    meta_info_current_version = models.CharField(max_length=100, blank=True, null=True)
    meta_info_android_version = models.CharField(max_length=100, blank=True, null=True)
    meta_info_description = models.CharField(max_length=1000, blank=True, null=True)
