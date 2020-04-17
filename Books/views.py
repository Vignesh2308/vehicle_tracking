from django.shortcuts import render,redirect
from django.http import HttpResponse
from Books.models import Book,Data,Buttons

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
    context =\
    {
        'location':Data.objects.all(),
        'button':Buttons.objects.all()
    }
    # send = Data.objects.all()
    # but = Button.objects.all()
    print(request.GET)
    if request.method == 'POST':
        num1 = request.POST['lat']
        num2 = request.POST['lon']
        dat = Data()
        dat.data1 = num1
        dat.data2 = num2
        dat.save()

    return render(request,'Home.html',context)

def delete(request):
    print("delete request")
    Data.objects.all().delete()
    context = \
        {
            'location': Data.objects.all()
        }
    return render(request,'result.html',context)

def add(request):
    num1 = request.GET['lat']
    num2 = request.GET['lon']
    dat=Data()
    dat.data1=num1
    dat.data2=num2
    dat.save()
    context = \
        {
            'location': Data.objects.all()
        }
    return render(request, 'Home.html',context)

def button(request):
    a=0
    but = Buttons.objects.get()
    print(but)

    if but.button1:
        but.button1=False
        a=0
        print('1')
    else:
        but.button1=True
        a=1
        print('2')
    but.save()
    print(but)

    return render (request,'index.html')

def result(request):
    but = Buttons.objects.get()
    print(but)
    if but.button1:
        a=0
        print('11')
    else:
        a=1
        print('22')

    return render(request,'button.html',{'res':a})