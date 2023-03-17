from django import forms

class StudentForm(forms.Form):
  fname = forms.CharField(max_length=50, label="First name", widget=forms.TextInput(attrs={'class': 'form-control'}))
  lname = forms.CharField(max_length=50, label="Last name", widget=forms.TextInput(attrs={'class': 'form-control'}))