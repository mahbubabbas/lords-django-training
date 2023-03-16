from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from day3_models.models import Student

# Create your views here.

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
  return render(req, "add.htm")

