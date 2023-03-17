from django import forms

class StudentForm(forms.Form):
  fname = forms.CharField(max_length=50, label="First name")
  lname = forms.CharField(max_length=50, label="Last name")