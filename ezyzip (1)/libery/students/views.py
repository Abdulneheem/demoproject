from django.shortcuts import render

from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from students.models import StudentDetails
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def user_logout(request):
    logout(request)
    return user_login(request)


# Create your views here.
def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user = authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('books:home')
        else:
            messages.error(request,"Inavalid credentials")



    return render(request, 'login.html',{'n':'john',  'j': 'jaik'})


def register(request):
      if(request.method=="POST"):
          u = request.POST['u']
          p= request.POST['p']
          p1 = request.POST['p1']
          e = request.POST['f']
          f = request.POST['l']
          l = request.POST['c']
          u = User.objects.create_user(username=u,password=p,first_name=e,last_name=f,email=l)
          u.save()
          return redirect('books:home')
      return render(request,'register.html')





@login_required
def studentDetails(request):
    StudentDetail = StudentDetails.objects.all()
    return render(request,'details.Html.html',{'StudentDetail':StudentDetail})


@login_required
def addstudentDetails(request):
    if (request.method == "POST"):
        T = request.POST['T']
        A = request.POST['A']
        P = request.POST['P']
        b = StudentDetails.objects.create(name =T, address=A, place =P)
        b.save()
        return studentDetails(request)
    return render(request, 'addstudents.html', {'n': 'john', 'j': 'jaik'})


@login_required
def factorial(request):
    if (request.method =="POST"):
        T = request.POST['T']
        j = 1
        for i in range(1,(int(T) + 1)):
            j = j * i
        return render(request, 'factorial.html', {'k': j})
    return render(request, 'factorial.html')

