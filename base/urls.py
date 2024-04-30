from django.urls import path
from base import views as base_views 

urlpatterns = [
    path("" , base_views.homePage , name = "home-page") ,
    path("create-item/"  , base_views.createItem , name = "create-item") , 
    path("delete-item/<int:item_id>/" , base_views.deleteItem  , name = "delete-item") , 
    path("update-item/<int:item_id>/" , base_views.updateItem , name = "update-item") , 
    path("login/" , base_views.loginUser , name = "login-user") , 
    path("register/" , base_views.registerUser , name = "register-user") , 
]