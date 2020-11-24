from django import forms
from .models import AndroidApp

class CreateAndroidApp(forms.ModelForm):
    appHandle = forms.CharField(label='appHandle', max_length=200)
    class Meta:
        model = AndroidApp
        fields = ['handle']
