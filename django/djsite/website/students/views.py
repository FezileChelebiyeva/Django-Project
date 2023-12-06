from django.shortcuts import render
from students.models import Studens
# Create your views here.


menu = [{'title': 'Əsas Səhifə', 'url_name': 'home'},
        {'title': 'Məlumat', 'url_name': 'about'},
        {'title': 'Əlaqə', 'url_name': 'contact'},
        {'title': 'Məqalə əlavə etmə', 'url_name': 'add_page'},
        {'title': 'Daxil olun', 'url_name': 'login'}]

posts = Studens.objects.all()


def index(request):
    data = {'title': 'Əsas Səhifə', "menu": menu, "posts": posts}
    return render(request, 'students/index.html', context=data)


def about(request):
    data = {'title': 'Məlumat', "menu": menu}
    return render(request, 'students/about.html', context=data)


def addpage(request):
    data = {'title': 'Məqalə əlavə etmə', "menu": menu}
    return render(request, 'students/addpage.html', context=data)


def contact(request):
    data = {'title': 'Əlaqə', "menu": menu}
    return render(request,  'students/contact.html', context=data)


def login(request):
    data = {'title': 'Daxil olun', "menu": menu}
    return render(request,  'students/login.html', context=data)
