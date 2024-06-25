from django.shortcuts import render,redirect
from . models import Students

# Create your views here.

def display(request):
    frm=StudentsForm()
    displayDetails=Students.objects.all()
    return render (request , 'index.html',{'StdDet':displayDetails,'frm':frm})

def create(request):
    if request.method == 'POST':
        frm=StudentsForm(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('home')
        #This is Future
    else:
        frm=StudentsForm()
    return render(request,'create.html',{'frm':frm})
from . forms import StudentsForm

def edit(request,pk):
    edit_instance=Students.objects.get(pk=pk)
    if request.POST:
        frm=StudentsForm(request.POST,instance=edit_instance)
        if frm.is_valid():
            edit_instance.save()
            return redirect('home')
        
    frm=StudentsForm(instance=edit_instance)
    return render (request ,'edit.html',{'frm':frm})

def delete(request,pk):#pk primary key
    instance=Students.objects.get(pk=pk)
    instance.delete()
    displayDetails=Students.objects.all()
    return render (request , 'index.html',{'StdDet':displayDetails})