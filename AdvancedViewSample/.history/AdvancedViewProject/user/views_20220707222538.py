from django.shortcuts import render
from user.forms import UserForm, ProfileForm

# Create your views here.
def user_list(request):
    return render(request, 'user/user_list.html', context={})

def index(request):
    return render(request, 'user/index.html')

def register(request):
    user_form = UserForm(request.POST or None)
    profile_name = ProfileForm(request.POST or None, request.FILES or None)
    if user_form.is_valid():
        