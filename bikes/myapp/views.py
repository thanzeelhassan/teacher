from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import PurchaseDetails,ProductDetails,UserDetails

from . import forms

def add(request):
    owner=request.GET['a']
    name=request.GET['b']
    star=request.GET['c']
    #star2=request.POST['star2']
    row=ProductDetails.objects.get(ProductName=name)
    fun=0
    if(star=='1') :
        fun=row.onestar
    elif(star=='2'):
        fun=row.twostar
    elif(star=='3') :
        fun=row.threestar
    elif(star=='4') :
        fun=row.fourstar
    elif(star=='5') :
        fun=row.fivestar
    else:
        text='Invalid star value'
    text='The number of '+str(star)+' stars for '+name+' is '+str(fun)
    return HttpResponse(text)
    #return render(request, 'result.html', {'result': fun} )

def regform(request):
    return render(request, 'home.html', {'name': 'Thanzeel'})

def hello(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)

def create(request):
    text = """<h2>Creating !</h2>"""
    return HttpResponse(text)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def viewArticle(request, articleId):
    text = "Displaying article Number : %s"%articleId
    return HttpResponse(text)

def viewArticles(request, month, year):
    text = "Displaying articles of : %s year /%s month "%(year, month)
    return HttpResponse(text)

def star_with_custom_name(request,star,name):
    row=ProductDetails.objects.get(ProductName=name)
    fun=0
    if(star=='1') :
        fun=eval('row.onestar')
    elif(star=='2'):
        fun=eval('row.twostar')
    elif(star=='3') :
        fun=eval('row.threestar')
    elif(star=='4') :
        fun=eval('row.fourstar')
    elif(star=='5') :
        fun=eval('row.fivestar')
    else:
        text='Invalid star value'
    text='The number of '+str(star)+' stars for '+name+' is '+str(fun)
    return HttpResponse(text)
'''
def star_with_custom_owner(request,star,owner):
    row=ProductDetails.objects.filter(ProductOwner=owner)
    fun=0
    if(star=='1'):
	    fun=fun+eval('row.onestar')
	elif(star=='2'):
		fun=fun+eval('row.twostar')
   	elif(star=='3') :
		fun=fun+eval('row.threestar')
    elif(star=='4') :
		fun=fun+eval('row.fourstar')
   	elif(star=='5') :
		fun=fun+eval('row.fivestar')
  	else:
		text='Invalid star value'
    text='The number of '+str(star)+' stars for '+owner+' is '+str(fun)
    return HttpResponse(text)
'''
