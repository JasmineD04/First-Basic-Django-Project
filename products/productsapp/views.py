from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def home(request):
    return render(request,'productsapp/main.html')

def viewcategories(request):
    cursor=connection.cursor()
    cursor.execute("SELECT * from categories")
    columns = [col[0] for col in cursor.description]
    keys =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    context={
        'rows':keys
    }
    print(keys)
    return render(request,'productsapp/view2.html',context)






# def viewproducts(request):
#     cursor=connection.cursor()
#     cursor.execute("SELECT * from product where softdelete=0")
#     columns = [col[0] for col in cursor.description]
#     posts =  [
#         dict(zip(columns, row))
#         for row in cursor.fetchall()
#     ]
#     context={
#         'keyposts':posts
#     }
#     print(posts)
#     return render(request,'productsapp/view.html',context)



def view(request):
    # return HttpResponse("<h1>Hello World</h1>")
    cursor=connection.cursor()
    cursor.execute("SELECT * from product where softdelete=0")
    columns = [col[0] for col in cursor.description]
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    context={
        'keyposts':posts
    }
    print(posts)
    return render(request,'productsapp/view.html',context)
    
def insert(request):
    pname = request.POST['productName']
    psummary = str(request.POST['productSummary'])
    pcolor=str(request.POST['productColor'])
    psize=str(request.POST['productSize'])
    pprice=int(request.POST['productPrice'])
    cursor = connection.cursor()
    # print(content)
    cursor.execute("INSERT INTO product (`name`,`summary`,`color`,`size`,`prize`) VALUES ( %s,%s,%s,%s,%s );",(pname,psummary,pcolor,psize,pprice))
    return redirect('/products/view')

def create(request):
    return render(request,'productsapp/insert.html')

def edit(request,pk):
    print(pk)
    cursor=connection.cursor()
    cursor.execute(f"SELECT * from product where id={pk}")
    columns=[col[0] for col in cursor.description]
    posts=[
        dict(zip(columns,row))
        for row in cursor.fetchall()
    ]
    print(posts)
    context={
        'keyposts':posts[0]
    }
    return render(request,'productsapp/editform.html',context)


def update(request):
    name=str(request.POST['name'])
    summary=str(request.POST['summary'])
    color=str(request.POST['color'])
    size=str(request.POST['size'])
    prize=int(request.POST['prize'])
    id=request.POST['id']
    cursor = connection.cursor()
    # print(content)
    cursor.execute("UPDATE product set name=%s,summary=%s,color=%s,size=%s,prize=%s where id=%s",(name,summary,color,size,prize,id))
    cursor = connection.cursor()
    return redirect('/products/view')


def delete(request,pk):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE product set softdelete=1 where id={pk}")
    return redirect('/products/view')