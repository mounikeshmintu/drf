from django.shortcuts import render


def djangular(request,path=None):
    return render(request,'ang/app/blog-list.html',{})
