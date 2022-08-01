from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Hello World</h1>")
    cursor=connection.cursor()
    cursor.execute("SELECT * from products ")
    columns = [col[0] for col in cursor.description]
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    context={
        'keyposts':posts
    }
    print(posts)
    return render(request,'productsapp/home.html',context)
    
