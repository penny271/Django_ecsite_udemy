from django.forms import forms
.models import Students


class Students(forms.ModelForm):

    class Meta:
        model=