from django.shortcuts import render
from django.http import HttpResponse
from Books.models import Book,Data,Button

# Create your views here.
# def index(request):
#     all_books = Book.objects.all()
#     html = ''
#     for book in all_books:
#         url = '/' + str(book.id) + '/'
#         html+= '<a href="' + url + '">' + str(book.name) + '</a></br>'
#
#     return HttpResponse(html)
#
# def detail(request,book_id):
#     return render(request,'index.html',{'book':book_id,'name':'vicka'})

def index(request):
    send = Data.objects.all()
    but = Button.objects.all()
    return render(request,'index.html',{'abc':send,'status':but})

def delete(request):
    print("delete request")
    Data.objects.all().delete()
    send = Data.objects.all()
    return render(request,'index.html',{'abc':send})

def add(request):
    num1 = request.GET['lat']
    num2 = request.GET['lon']
    dat=Data()
    dat.data1=num1
    dat.data2=num2
    dat.save()
    return render(request, 'result.html')

def button(request):
    but = Button.objects.all()
    return render (request,'button.html',{'status':but})