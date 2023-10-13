

# Create your views here.
from django.shortcuts import render
from books.models import Books
from books.forms import BookForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):

    return render(request,'home.html',)

@login_required
def addbookss(request):
     if(request.method =="POST"):
          T = request.POST['T']
          A = request.POST['A']
          P = request.POST['P']
          o = request.FILES['o']
          q = request.FILES['i']
          b = Books.objects.create(title=T,author=A,price=P, pdf=o, image=q)
          b.save()
          return viw(request)
     return render(request, 'addbooks.html',{'n':'john',  'j': 'jaik'})

# def addbookss(request):
#     if(request.method=="POST"):
#         form=BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return viw(request)
#     form = BookForm()
#     return render(request,'add1html.html',{'form':form})


@login_required
def viw(request):
    books = Books.objects.all()
    return render(request, 'view.html',{'books': books})

@login_required
def viewbook(request,p):
    b=Books.objects.get(id=p)
    return render(request, 'viewbooksforbook.html',{'b':b})

@login_required
def delete(request,p):
    b = Books.objects.get(id=p)
    b.delete()
    return viw(request)

@login_required
def editbook(request,p):
    b = Books.objects.get(id=p)
    if(request.method=="POST"):
            form=BookForm(request.POST,request.FILES,instance=b)
            if form.is_valid():
                form.save()
                return viw(request)


    form = BookForm(instance=b)
    return render(request,'editbooks.html',{'b':form})