from django.forms import forms
from .models import Students


class Students_form(forms.ModelForm):

    class Meta:
        model=Students