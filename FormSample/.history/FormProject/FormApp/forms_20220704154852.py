from django import forms

class UserInfo(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    mail = forms.EmailField()
    is_married = forms.BooleanField()
    birthday = forms.DateField()
    salary = forms.DecimalField()
    job = forms.ChoiceField(choices =(
        (1,製写真)
    ))