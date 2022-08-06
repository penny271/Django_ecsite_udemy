#- ★順番どおりにimportしていかないと以下のようなエラーが出る
#! django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
#- setup()してからモデルを呼び出す!
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
from django import setup
setup()

# from ModelApp.models import Students, TestResults, Tests, Classes
# from random import randint

from ModelApp.models import Students, Tests_results, Tests, Classes
from random import randint

for _ in range(1)


