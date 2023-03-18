from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from day3_models.forms import LoginForm, StudentForm
from day3_models.models import Student

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

def mylogin(req):
  form = LoginForm()

  if req.method == 'POST':
    form = LoginForm(req.POST)
    if form.is_valid(): 
      user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
      if user is None:
        return redirect('/login')
      else:
        login(req, user)
        req.session['name'] = form.cleaned_data['username']
        return redirect('/')

  return render(req, "login.htm", {'form': form})

@login_required(login_url='/login')
def mylogout(req):
  logout(req)
  return redirect('/login')

@login_required(login_url='/login')
def index(req):
  data = {
    'name': req.session['name']
  }
  t1 = loader.get_template("index.htm")
  return HttpResponse(t1.render(data))

@login_required(login_url='/login')
def list(req):
  students = Student.objects.all()
  return render(req, "list.htm", {'students': students})

@login_required(login_url='/login')
def details(req, id):
  student = Student.objects.get(id=id)
  return render(req, "details.htm", {'stu': student})  

@login_required(login_url='/login')
def add(req):
  msg = None
  stu_form = StudentForm()
  
  if req.method == 'POST':
    form = StudentForm(req.POST)
    if form.is_valid():
      try:
        s = Student(
          fname=form.cleaned_data['fname'],
          lname= form.cleaned_data['lname']
        )
        s.save()   
        msg = 'Added successfully, Alhamdulillaah'
        return redirect('/list')
      except:
        msg = 'Ah .. some error!'
        pass
      
  return render(req, "add.htm", {'form': stu_form, 'msg': msg})

@login_required(login_url='/login')
def delete(req, id):
  msg = None
  try:
    student = Student.objects.get(id=id)
    student.delete()
    msg = 'Successfully deleted!'
  except:
    msg = 'Unable to delete'

  students = Student.objects.all()  
  return render(req, "list.htm", {'students': students, 'msg': msg})

