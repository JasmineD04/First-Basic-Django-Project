from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view
    (template_name='productsapp/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view
    (template_name='productsapp/logout.html'),name='logout'),
    path('home/',views.home,name='home'),
    path('view/',views.view,name='view-prod'),
    path('viewcat/',views.viewcategories,name='viewcategories'),
    path('create/',views.create,name='create'),
    path('createcat/',views.createcategories,name='createcategories'),
    path('insert/',views.insert,name='add'),
    path('insertcat/',views.insertcategories,name='addcat'),
    path('edit/<pk>',views.edit,name='edit'),
    path('update',views.update,name='update'),
    path('delete/<pk>',views.delete,name="delete"),
    path('addtocart/<pk>/<pd>',views.addtocart,name='addtocart'),
    path('viewcart/<pk>',views.viewcart,name="viewcart"),
    # path('removeprod/<pk>',views.removeprod,name="delete-prod")
]