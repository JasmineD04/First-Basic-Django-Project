from django.urls import path
from .import views
urlpatterns=[
    path('view/',views.view,name='view'),
    # # path('about/',views.about),
    # path('create/',views.create,name='create'),
    # path('insert/',views.insert,name='add')
]