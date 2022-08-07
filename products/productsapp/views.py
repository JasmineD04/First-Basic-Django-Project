from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def view(request):
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
    
def insert(request):
    pname = request.POST['productName']
    psummary = str(request.POST['productSummary'])
    pcolor=str(request.POST['productColor'])
    psize=str(request.POST['productSize'])
    pprice=int(request.POST['productPrice'])
    cursor = connection.cursor()
    # print(content)
    cursor.execute("INSERT INTO products (`name`,`summary`,`color`,`size`,`price`) VALUES ( %s,%s,%s,%s,%s );",(pname,psummary,pcolor,psize,pprice))
    return redirect('/products/view')

def create(request):
    return render(request,'productsapp/insert.html')
