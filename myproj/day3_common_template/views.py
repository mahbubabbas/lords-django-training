from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(req):
  t1 = loader.get_template("index.htm")
  return HttpResponse(t1.render())

def list(req):
  students = [
    {'fname': 'Absdks', 'lname': 'sdfkkdsf', 'roll': 1},
    {'fname': 'Adsf', 'lname': 'sdfkkdsf', 'roll': 2},
    {'fname': 'Asdfkk', 'lname': 'sdfkkdsf', 'roll': 3},
    {'fname': 'Asdkkdf', 'lname': 'sdfkkdsf', 'roll': 4},
  ]
  return render(req, "list.htm", {'students': students})

def add(req):
  return render(req, "add.htm")
