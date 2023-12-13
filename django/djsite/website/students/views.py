from django.shortcuts import render
from students.models import *
from django.http import HttpResponse

# Create your views here.


menu = [{'title': 'Əsas Səhifə', 'url_name': 'home'},
        {'title': 'Məlumat', 'url_name': 'about'},
        {'title': 'Əlaqə', 'url_name': 'contact'},
        {'title': 'Məqalə əlavə etmə', 'url_name': 'add_page'},
        {'title': 'Daxil olun', 'url_name': 'login'},
        ]


def index(request):
    posts = Studens.objects.all()
    cats = Category.objects.all()
    data = {'title': 'Əsas Səhifə', "menu": menu,
            "posts": posts, 'cats': cats, 'cat_selected': 0, }
    return render(request, 'students/index.html', context=data)


def show_post(request, post_id):
    posts = Studens.objects.filter(id = post_id)
    data = {'title': 'Əsas Səhifə', "menu": menu,
            "posts": posts, 'post_id': post_id, }
    return render(request, 'students/index.html', context=data)
    # return HttpResponse(f"Məqalənin id ilə göstərilməsi = {post_id}")


def show_category(request, cat_id):
    posts = Studens.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    data = {'title': 'Əsas Səhifə', "menu": menu,
            "posts": posts, 'cats': cats, 'cat_selected': cat_id, }
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
