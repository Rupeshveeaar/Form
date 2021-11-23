from django import forms
class StudentsRegistration(forms.Form):
    names = froms.CharField()
    email = froms.EmailField()
