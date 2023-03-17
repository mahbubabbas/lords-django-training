from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from day3_models.forms import StudentForm

from day3_models.models import Student

def index(req):
  t1 = loader.get_template("index.htm")
  return HttpResponse(t1.render())

def list(req):
  students = Student.objects.all()
  return render(req, "list.htm", {'students': students})

def details(req, id):
  student = Student.objects.get(id=id)
  return render(req, "details.htm", {'stu': student})  

def add(req):
  stu_form = StudentForm()
  
  if req.method == 'POST':
    stu = StudentForm(req.POST)
    s = Student(fname = stu, lname=stu['lname'])
    s.save()
    redirect('/list')
      
  return render(req, "add.htm", {'form': stu_form})
