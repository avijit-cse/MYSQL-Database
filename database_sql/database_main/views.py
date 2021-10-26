from django.shortcuts import render
from django.http import HttpResponse
from database_main import forms
from database_main.models import mugisian,album


def index(request):
    list=mugisian.objects.order_by('first_name')
    diction={"title":"Index page",'name':list}
    return render(request,'index.html',context=diction)

def album_list(request,a_id):
    arist_info=mugisian.objects.get(pk=a_id)
    album_list=album.objects.filter(pk=a_id)
    diction={"title":"album List",'arist_info':arist_info,'album_list':album_list}
    return render(request,'albuml.html',context=diction)


def misician_form(request):
    form=forms.newfrom()

    if request.method=='POST':
        form=forms.newfrom(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)


    
    diction={"title":"musician form ",'mfrom':form}
    return render(request,'addm.html',context=diction)

def album_form(request):
    form=forms.albumfrom()

    if request.method=='POST':
        form=forms.albumfrom(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)


    diction={"title":"album form",'aform':form}
    return render(request,'addalbum.html',context=diction)            



def editview(request,a_id):
    arist_info=mugisian.objects.get(pk=a_id)
    form=forms.newfrom(instance=arist_info)
    if request.method =='POST':
        form=forms.newfrom(request.POST,instance=arist_info)
        if form.is_valid():
            form.save(commit=True)

            return album_list(request,a_id)



    diction={'form':form}
    return render(request,'edit.html',context=diction)

def edit_album(request,b_id):
    album_info=album.objects.get(pk=1)
    form=forms.albumfrom(instance=album_info)
    if request.method =='POST':
        form=forms.albumfrom(request.POST,instance=album_info)
        if form.is_valid():
            form.save(commit=True)

            
    
    diction={'form':form,'list':b_id}
    return render(request,'edit_album.html',context=diction)


def delectview(request,album_id):
    ab=album.objects.get(pk=album_id).delete()

    diction={"delete_sucess":"Album delect suceesully"}
    return render(request,'delect.html',context=diction)

def mdelectview(request,ab_id):
    arist=mugisian.objects.get(pk=ab_id).delete(0)

    diction={"delete_sucess":"Musician delect suceesully"}
    return render(request,'delect.html',context=diction)

