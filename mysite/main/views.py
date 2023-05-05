from django.shortcuts import render, redirect
from .models import *


def index(request):
    index_list = Index.objects.all()
    services_list = IndexServices.objects.all()
    price_list = IndexPrice.objects.all()
    blog_list = IndexBlog.objects.all()
    about_list = IndexAbout.objects.all()
    customers_list = IndexCustomers.objects.all()

    return render(request, 'index.html', context={
        'index_list':index_list,
        'services_list':services_list,
        'price_list':price_list,
        'blog_list':blog_list,
        'about_list': about_list,
        'customers_list': customers_list

    })


def about(request):
    about_list=IndexAbout.objects.all()
    return render(request, 'index.html', context={
        'about_list':about_list
    })

def blog(request):
    blog_list = IndexBlog.objects.all()
    return render(request, 'index.html', context={
        'blog_list':blog_list
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        Contact.objects.create(name=name, text = text)
        return redirect('index')
    return render(request, 'contact.html')


def service(request):
    service_list = IndexServices.objects.all()
    return render(request, 'service.html', context={
        'service_list':service_list
    })

