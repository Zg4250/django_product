from django.db import models
import re
import datetime
import bcrypt

class UserManager(models.Manager):
    def reg_validator(self, form):

        errors = {}

        name = form['name']
        username = form['username']
        datehired = form['datehired']
        password = form['password']
        confirm_pw = form['confirm_password']
        

        if len(name) < 3:
            errors['name'] = "Name must be atleast 3 characters"
        elif not name.isalpha():
            errors['name'] = "Name cannot contain number or special characters!"
        if len(username) < 3:
            errors['username'] = "Username must be atleast 3 characters"
        elif not username.isalpha():
            errors['username'] = "Username cannot contain number or special characters!"
        else:
            users = User.objects.filter(username=username)
            if len(users) > 0:
                errors['username'] = "Username already exists. Please login."
        if not datehired:
            errors['datehired'] = "Please enter a date"
        elif datehired > str(datetime.datetime.now()):
            errors['datehired'] = "Impossible"
        if len(password) < 1:
            errors['password'] = "Password must be longer"
        elif password != confirm_pw:
            errors['confirm_pw'] = "Passwords do not match"
        

        return errors
            
    
    def loginvalidator(self, form):
        errors = {}
        username = form['username']
        password = form['password']


        if len(username) < 0:
            errors["username"] = "Please enter Username"
        elif len(User.objects.filter(username = username)) < 1:
            errors['username'] = "Username not in database please register!"
        else:
            if not bcrypt.checkpw(password.encode(), User.objects.get(username = username).password.encode()):
                errors['username'] = "cannot login"
                
        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    datehired = models.DateField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    
    objects = UserManager()

class ItemManager(models.Manager):
    def item_validator(self, form):

        errors = {} 
        title = form['title']

        if len(title) < 3:
            errors["title"] = "Title is too short"
        return errors       

    
    objects = UserManager()


class Item(models.Model):
    title = models.CharField(max_length=255)
    addedby = models.ForeignKey(User, related_name="added_item", on_delete=models.CASCADE)
    wishlist=models.ManyToManyField(User,related_name="wishlist")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    objects = ItemManager()