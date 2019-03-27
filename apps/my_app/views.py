from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, 'index.html')

def register(request):
    result = User.objects.reg_validator(request.POST)
    if len(result) > 0:
        for key, value in result.items():
            messages.add_message(request, messages.ERROR, value)
        return redirect('/')
    else: 
        hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(name=request.POST['name'], username=request.POST['username'], datehired = request.POST['datehired'], password=hash.decode())
        request.session['userid'] = user.id
        return redirect('/')


def login(request):
    result = User.objects.loginvalidator(request.POST)
    if len(result) > 0:
        for key, value in result.items():
            messages.add_message(request, messages.ERROR, value)
        return redirect('/')
    else:
        user = User.objects.get(username = request.POST['username'])
        request.session['userid'] = user.id
        return redirect('/displaywishlist')


def displaywishlist(request):
    if 'userid' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['userid'])
        items = user.wishlist.all()
        nonwishlist = []
        allitems=Item.objects.all()
        for i in allitems:
            if i not in items:
                nonwishlist.append(i)
        context = {
            'user': user,
            'items': items,
            'nonwishlist': nonwishlist
        }
        
        return render(request, 'displaywishlist.html', context)

def additem(request):
    return render(request, 'additem.html')    

def createitem(request):   
    result = Item.objects.item_validator(request.POST)
    print(result)
    if len(result) > 0:
        for key, value in result.items():
            messages.add_message(request, messages.ERROR, value)
        return redirect('/additem')
    else:
        item = Item.objects.create(title=request.POST['title'], addedby_id=request.session['userid'])
        user = User.objects.get(id = request.session['userid'])
        user.wishlist.add(item)
        return redirect('/displaywishlist')

def showitem(request, id):
    context={
        "item" : Item.objects.get(id=id),
        "wishlist": Item.objects.get(id=id).wishlist.all()
    }
    return render(request, "showitem.html", context)

def delete(request, id):
    i = Item.objects.get(id=id)
    i.delete()
    return redirect('/displaywishlist')


def wishlist(request, id):
    user = User.objects.get(id = request.session['userid'])
    item = Item.objects.get(id=id)
    user.wishlist.add(item)
    return redirect('/displaywishlist')


def nonwishlist(request, id):
    user = User.objects.get(id = request.session['userid'])
    item = Item.objects.get(id=id)
    user.wishlist.remove(item)
    return redirect('/displaywishlist')

def logout(request):
    request.session.clear()
    return redirect ('/')