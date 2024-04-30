from django.shortcuts import render , redirect
from base.models import TodoList
from django.contrib.auth import authenticate , login , logout
from  django.contrib.auth.models import User

def homePage(request , *args , **kwargs):
    if not request.user.is_authenticated :
        return redirect("login-user")
    items = TodoList.objects.filter(user = request.user) 
    return render(request , "base/homePage.html" , context = {"items" : items})

def createItem(request , *args , **kwargs):
    if not request.user.is_authenticated :
        return redirect("login-user")
    if request.method == "POST" : 
        title = request.POST.get("title")
        desc = request.POST.get("description")
        
        item = TodoList.objects.create(
            title = title , 
            description = desc ,
            user = request.user , 
        )
        return redirect("home-page")
    return render(request , "base/createItem.html")

def deleteItem(request , item_id , *args , **kwargs):
    if not request.user.is_authenticated :
        return redirect("login-user")
    if request.method == "POST" :
        try : 
            todo_item = TodoList.objects.get(id = item_id)
            todo_item.delete()
            return redirect("home-page")
        except :
            ...
    return render(request , "base/deleteItem.html")

def updateItem(request ,  item_id , *args , **kwargs):
    if not request.user.is_authenticated :
        return redirect("login-user")
    if request.method == "POST" :
        new_title = request.POST.get("title")
        print(request.POST.get("completed"))
        new_completed = True if request.POST.get("completed") == "on" else False
        print(f"This is new completed : {new_completed}")
        new_description = request.POST.get("description")
        todo_item = TodoList.objects.get(id = item_id)
        todo_item.title = new_title
        todo_item.completed = new_completed
        todo_item.description = new_description
        todo_item.save()
        print(todo_item)
        return redirect("home-page")
    todo_item = TodoList.objects.get(id = item_id)
    return render(request , "base/updateItem.html" ,  context = {"item" : todo_item})

def loginUser(request , *args , **kwargs):
    if request.method == "POST" :
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username , password = password)
        if user :
            login(request , user)
            return redirect("home-page")
        else :
            message = "The credentials are invalid !"
            return render(request , "base/loginPage.html" , context = {"message" : message})
    return render(request , "base/loginPage.html")

def registerUser(request ,  *args , **kwargs):
    if request.method == "POST" :
        username = request.POST.get("username")
        password = request.POST.get("password")
        user , created = User.objects.get_or_create(username = username , password = password)
        if not created :
            message = f"User with the username : {username} already exists !"
            return render(request , "base/registerUser.html" , context = {"message" : message})
        else :
            login(request , user)
            return redirect("home-page")
    return render(request , "base/registerUser.html" )