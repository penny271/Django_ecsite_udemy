from django import forms

class UserInfo(forms.Form):
    name = forms.CharField()