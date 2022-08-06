#- ★順番どおりにimportしていかないと以下のようなエラーが出る
#! django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
#- setup()してからモデルを呼び出す!
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
from django import setup
setup()

from ModelApp.models import Students, Classes

student_a = Students.objects.get(pk=1)
print(student_single)

